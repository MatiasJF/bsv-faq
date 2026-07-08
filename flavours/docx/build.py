#!/usr/bin/env python3
"""BSVA-branded .docx flavour of the live FAQ.

Reads every question file under faq/ (the curated live core — archive/ is
never touched), and renders them on the official BSV Association Word
template via surgical XML editing, per the /bsva-docx skill rules.

Output: BSV_Blockchain_FAQ.docx next to this script.
"""

import re
import sys
import copy
import subprocess
from pathlib import Path

try:
    from docx import Document
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-docx", "lxml"])
    from docx import Document

from lxml import etree
from docx.oxml.ns import qn

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"

TEMPLATE_PATH = "/Users/matiasjackson/.claude/skills/bsva-docx/BSV Association Word template 2025.docx"
REPO = Path(__file__).resolve().parents[2]
FAQ_DIR = REPO / "faq"
OUT_PATH = Path(__file__).resolve().parent / "BSV_Blockchain_FAQ.docx"

TITLE = "BSV Blockchain FAQ"
SUBTITLE = "Plain answers to the basics"
VERSION = "Curated core — 11 questions"
DATE = "July 2026"
FOOTER_VERSION = "Version 1.0"

# Reading order: category → heading shown in the document, file ids in order.
SECTIONS = [
    ("00-basics", "The basics",
     ["what-is-bsv", "bitcoin-vs-bsv", "what-is-a-wallet"]),
    ("10-using-bsv", "Using BSV",
     ["where-to-get-bsv", "sending-bsv-basics", "what-are-fees",
      "keeping-bsv-safe", "lost-keys-recovery", "custodial-vs-own-wallet"]),
    ("20-exchanges-access", "Exchanges and access",
     ["exchange-closes-my-funds"]),
    ("40-ecosystem", "The ecosystem",
     ["what-is-the-bsv-association"]),
]


# ---------------------------------------------------------------- FAQ parsing

def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^(\w+):\s*(.+)$", line)
        if kv:
            fm[kv.group(1)] = kv.group(2).strip().strip('"')
    return fm, text[m.end():]


def load_questions():
    """id -> {question, category, body}"""
    questions = {}
    for path in sorted(FAQ_DIR.rglob("*.md")):
        fm, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        questions[fm["id"]] = {"question": fm["question"],
                               "category": fm["category"], "body": body}
    return questions


def resolve_refs(text, questions):
    """[[id]] → the quoted question text, readable on paper."""
    def pair(m):
        a = questions[m.group(1)]["question"]
        b = questions[m.group(2)]["question"]
        return f'see “{a}” and “{b}”'

    def single(m):
        return f'see “{questions[m.group(1)]["question"]}”'

    text = re.sub(r"\[\[([a-z0-9-]+)\]\],\s*\[\[([a-z0-9-]+)\]\]", pair, text)
    text = re.sub(r"\[\[([a-z0-9-]+)\]\]", single, text)
    return text


def to_segments(text):
    """'a **b** *c*' → [(text, bold, italic), ...]"""
    segments = []
    for part in re.split(r"(\*\*.+?\*\*)", text):
        if part.startswith("**") and part.endswith("**"):
            segments.append((part[2:-2], True, False))
        else:
            for sub in re.split(r"(\*[^*]+?\*)", part):
                if sub.startswith("*") and sub.endswith("*"):
                    segments.append((sub[1:-1], False, True))
                elif sub:
                    segments.append((sub, False, False))
    return segments


def parse_body(body, questions):
    """FAQ markdown body → (short_answer_segments, detail_blocks).

    Blocks: ("para", segments) | ("bullet", segments) | ("table", headers, rows)
    The '## Sources' section is dropped; the '## More detail' heading marks
    where the short answer ends and the long answer begins.
    """
    short = None
    blocks = []
    lines = body.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if line.startswith("## Sources"):
            break
        if line.startswith("**Short answer.**"):
            text = line[len("**Short answer.**"):].strip()
            short = to_segments(resolve_refs(text, questions))
            i += 1
            continue
        if not line or line.startswith("## "):
            i += 1
            continue
        if line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells):
                    rows.append([resolve_refs(c, questions) for c in cells])
                i += 1
            blocks.append(("table", rows[0], rows[1:]))
            continue
        if line.startswith("- "):
            blocks.append(("bullet", to_segments(resolve_refs(line[2:], questions))))
            i += 1
            continue
        blocks.append(("para", to_segments(resolve_refs(line, questions))))
        i += 1
    return short, blocks


# ------------------------------------------------------------- XML builders

BRAND_NAVY = "1B1EA9"  # Heading1's color in the template


def make_paragraph(style_id, segments, page_break=False, color=None, sz=None):
    """segments: (text, bold, italic) or (text, bold, italic, color)."""
    p = etree.SubElement(etree.Element("dummy"), qn("w:p"))
    pPr = etree.SubElement(p, qn("w:pPr"))
    etree.SubElement(pPr, qn("w:pStyle")).set(qn("w:val"), style_id)
    if page_break:
        etree.SubElement(pPr, qn("w:pageBreakBefore"))
    for seg in segments:
        text, bold, italic = seg[0], seg[1], seg[2]
        seg_color = seg[3] if len(seg) > 3 else color
        r = etree.SubElement(p, qn("w:r"))
        if bold or italic or seg_color or sz:
            rPr = etree.SubElement(r, qn("w:rPr"))
            if bold:
                etree.SubElement(rPr, qn("w:b"))
            if italic:
                etree.SubElement(rPr, qn("w:i"))
            if seg_color:
                etree.SubElement(rPr, qn("w:color")).set(qn("w:val"), seg_color)
            if sz:
                etree.SubElement(rPr, qn("w:sz")).set(qn("w:val"), str(sz))
                etree.SubElement(rPr, qn("w:szCs")).set(qn("w:val"), str(sz))
        t = etree.SubElement(r, qn("w:t"))
        t.text = text
        if text and (text[0] == " " or text[-1] == " "):
            t.set(XML_SPACE, "preserve")
    return p


def _set_cnf(parent, val, **kwargs):
    cnf = etree.SubElement(parent, qn("w:cnfStyle"))
    cnf.set(qn("w:val"), val)
    for k, v in kwargs.items():
        cnf.set(qn(f"w:{k}"), v)


def _add_cell(tr, segments, w, style_id, first_col=False, shaded=False, vAlign=None):
    tc = etree.SubElement(tr, qn("w:tc"))
    tcPr = etree.SubElement(tc, qn("w:tcPr"))
    if first_col:
        _set_cnf(tcPr, "001000000000", firstColumn="1")
    tw_el = etree.SubElement(tcPr, qn("w:tcW"))
    tw_el.set(qn("w:w"), str(w))
    tw_el.set(qn("w:type"), "pct")
    if shaded:
        shd = etree.SubElement(tcPr, qn("w:shd"))
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:color"), "auto")
        shd.set(qn("w:fill"), "EFF0F7")
        shd.set(qn("w:themeFill"), "background2")
    if vAlign:
        etree.SubElement(tcPr, qn("w:vAlign")).set(qn("w:val"), vAlign)

    p = etree.SubElement(tc, qn("w:p"))
    pPr = etree.SubElement(p, qn("w:pPr"))
    etree.SubElement(pPr, qn("w:pStyle")).set(qn("w:val"), style_id)
    for text, bold, italic in segments:
        r = etree.SubElement(p, qn("w:r"))
        if bold or italic:
            rPr = etree.SubElement(r, qn("w:rPr"))
            if bold:
                etree.SubElement(rPr, qn("w:b"))
            if italic:
                etree.SubElement(rPr, qn("w:i"))
        t = etree.SubElement(r, qn("w:t"))
        t.text = text
        if text and (text[0] == " " or text[-1] == " "):
            t.set(XML_SPACE, "preserve")


def make_table_xml(headers, data_rows):
    ncols = len(headers)
    base_w = 5000 // ncols
    col_widths = [base_w] * ncols
    col_widths[-1] = 5000 - base_w * (ncols - 1)

    tbl = etree.SubElement(etree.Element("dummy"), qn("w:tbl"))
    tblPr = etree.SubElement(tbl, qn("w:tblPr"))
    etree.SubElement(tblPr, qn("w:tblStyle")).set(qn("w:val"), "nChain")
    tw = etree.SubElement(tblPr, qn("w:tblW"))
    tw.set(qn("w:w"), "5000")
    tw.set(qn("w:type"), "pct")
    tl = etree.SubElement(tblPr, qn("w:tblLook"))
    for k, v in {"val": "04A0", "firstRow": "1", "lastRow": "0",
                 "firstColumn": "1", "lastColumn": "0", "noHBand": "0", "noVBand": "1"}.items():
        tl.set(qn(f"w:{k}"), v)

    tblGrid = etree.SubElement(tbl, qn("w:tblGrid"))
    for w in col_widths:
        etree.SubElement(tblGrid, qn("w:gridCol")).set(qn("w:w"), str(int(w * 9864 / 5000)))

    tr = etree.SubElement(tbl, qn("w:tr"))
    trPr = etree.SubElement(tr, qn("w:trPr"))
    _set_cnf(trPr, "100000000000", firstRow="1")
    etree.SubElement(trPr, qn("w:trHeight")).set(qn("w:val"), "432")
    for ci, (text, w) in enumerate(zip(headers, col_widths)):
        _add_cell(tr, to_segments(text), w, "BSVATableHeader",
                  first_col=(ci == 0), vAlign="center")

    for ri, row_data in enumerate(data_rows):
        shaded = (ri % 2 == 0)
        tr = etree.SubElement(tbl, qn("w:tr"))
        trPr = etree.SubElement(tr, qn("w:trPr"))
        if shaded:
            _set_cnf(trPr, "000000100000", oddHBand="1")
        etree.SubElement(trPr, qn("w:trHeight")).set(qn("w:val"), "455")
        for ci, (text, w) in enumerate(zip(row_data, col_widths)):
            _add_cell(tr, to_segments(text), w, "BSVATableText",
                      first_col=(ci == 0), shaded=shaded)
    return tbl


# ------------------------------------------------------------------ document

def build():
    questions = load_questions()
    expected = {qid for _, _, ids in SECTIONS for qid in ids}
    if set(questions) != expected:
        raise SystemExit(f"faq/ changed — update SECTIONS. "
                         f"missing={expected - set(questions)} new={set(questions) - expected}")

    doc = Document(TEMPLATE_PATH)
    body = doc.element.body
    children = list(body)

    # Cover
    cover_texts = {0: TITLE, 1: SUBTITLE, 2: VERSION, 3: DATE}
    for idx, new_text in cover_texts.items():
        para = children[idx]
        for r in para.findall(f"{{{W}}}r"):
            para.remove(r)
        run = etree.SubElement(para, qn("w:r"))
        t = etree.SubElement(run, qn("w:t"))
        t.text = new_text

    # Strip sample content, merge sections (per skill reference)
    to_remove = [children[i] for i in range(4, 90)] + [children[91]]
    for child in to_remove:
        body.remove(child)
    children = list(body)
    sectpr_para = children[4]
    embedded_sectpr = sectpr_para.find(f".//{{{W}}}sectPr")
    final_sectpr = children[5]
    for child in list(final_sectpr):
        final_sectpr.remove(child)
    for attr, val in embedded_sectpr.attrib.items():
        final_sectpr.set(attr, val)
    for child in list(embedded_sectpr):
        final_sectpr.append(copy.deepcopy(child))
    body.remove(sectpr_para)

    # Header / footer text
    for section in doc.sections:
        if not section.header.is_linked_to_previous:
            for para in section.header.paragraphs:
                for run in para.runs:
                    if "BSV Association Document Template" in (run.text or ""):
                        run.text = TITLE
        if not section.footer.is_linked_to_previous:
            for para in section.footer.paragraphs:
                for run in para.runs:
                    if "Version 1.1" in (run.text or ""):
                        run.text = FOOTER_VERSION

    # Content
    content = [
        make_paragraph("Heading1", [("About this FAQ", False, False)]),
        make_paragraph("BSVAIntroduction", [(
            "This FAQ answers the questions a newcomer actually asks — in plain "
            "words, with no jargon and no assumptions. It is deliberately small: "
            "a curated core of eleven questions, kept rock solid before anything "
            "is added to it.", False, False)]),
        make_paragraph("Normal", [(
            "The answers are neutral by design. They explain how things work; they "
            "do not give investment advice, discuss prices, or recommend specific "
            "companies. Where an answer touches on risk — scams, lost keys, an "
            "exchange closing — it says plainly what can and cannot be done.",
            False, False)]),
        make_paragraph("Normal", [(
            "You can read it front to back in one sitting, or jump straight to the "
            "question you came with.", False, False)]),
    ]

    for _, heading, ids in SECTIONS:
        content.append(make_paragraph("Heading1", [(heading, False, False)],
                                      page_break=True, sz=44))
        for qid in ids:
            q = questions[qid]
            content.append(make_paragraph("Heading2", [(q["question"], False, False)],
                                          color=BRAND_NAVY, sz=34))
            short, blocks = parse_body(q["body"], questions)
            content.append(make_paragraph(
                "BSVAIntroduction",
                [("Short answer — ", True, False, BRAND_NAVY)] + list(short)))
            content.append(make_paragraph("Heading4", [("In more detail", False, False)]))
            for block in blocks:
                if block[0] == "para":
                    content.append(make_paragraph("Normal", block[1]))
                elif block[0] == "bullet":
                    content.append(make_paragraph("ListBullet", block[1]))
                elif block[0] == "table":
                    content.append(make_table_xml(block[1], block[2]))

    content += [
        make_paragraph("Heading1", [("Sources", False, False)]),
        make_paragraph("Normal", [(
            "The answers in this document are drawn from the official BSV "
            "Blockchain site, bsvblockchain.org. Each question in the source "
            "repository lists its sources individually.", False, False)]),
    ]

    final_sectpr = list(body)[-1]
    for elem in content:
        body.insert(list(body).index(final_sectpr), elem)

    doc.save(OUT_PATH)
    print(f"Saved: {OUT_PATH}")


if __name__ == "__main__":
    build()
