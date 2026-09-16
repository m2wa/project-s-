# -*- coding: utf-8 -*-
"""
The 8000-Page HTML & CSS Bible — build engine.

Assembles:
  Part 0  Front matter (cover, reader guide, content map, element status list, references)
  Part I  HTML — every element + global attributes + attribute deep-dives
  Part II CSS — every major property + selectors + at-rules + value keywords
  Part III Project Gallery (40 components × 4 themes)
  Part IV Master Reference Tables (element×attribute matrix, full CSS index)
  Part V Study (glossary, cheat sheets, quizzes)
  Part VI The 8000 Practice Pages (generated drills)
  Part VII Appendix

Output: index.html + volumes/vol-01.html … vol-16.html (500 pages each = 8000).
"""
import html as H
import math
import os
import random
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)

from data_html_a import E as ELEMS_A
from data_html_b import E as ELEMS_B   # noqa
from data_html_c import E as ELEMS     # combined (a->b->c)
from data_attrs import GLOBAL_ATTRS
from data_css_a import P as CSS_A
from data_css_b import P as CSS_B      # noqa
from data_css_c import P as CSS_PROPS, SEL, ATR, VAL
from data_extras import GLOSSARY, PROJECTS, THEMES

TOTAL_PAGES = 8000
VOLUMES = 16
PER_VOLUME = TOTAL_PAGES // VOLUMES    # 500

esc = H.escape

# ---------------------------------------------------------------- helpers
def code_block(src):
    return f'<pre class="code"><code>{esc(src)}</code></pre>'

def table(rows, header=("A", "B"), raw=False):
    th = "".join(f"<th>{esc(h)}</th>" for h in header)
    body = []
    for r in rows:
        tds = []
        for c in r:
            if raw and isinstance(c, str) and c.startswith("<"):
                tds.append(f"<td>{c}</td>")          # pre-made HTML
            else:
                tds.append(f"<td>{esc(str(c))}</td>")
        body.append("<tr>" + "".join(tds) + "</tr>")
    return f'<table class="ref"><thead><tr>{th}</tr></thead><tbody>{"".join(body)}</tbody></table>'

def demo_box(inner, caption="Live result"):
    return (f'<div class="demo"><div class="demo-bar"><span></span><span></span><span></span>'
            f'<em>{esc(caption)}</em></div><div class="demo-body">{inner}</div></div>')

def badge(text, cls=""):
    return f'<span class="badge {cls}">{esc(text)}</span>'

def kv_table(pairs):
    return table([(k, v) for k, v in pairs], ("Value / Keyword", "Meaning"))

# ---------------------------------------------------------------- page models
# page = dict(part, chap, title, tag, body)
PAGES = []

def page(part, chap, title, tag, body):
    PAGES.append(dict(part=part, chap=chap, title=title, tag=tag, body=body))

# ================================================================ FRONT MATTER
FRONT = "Part 0 — Front Matter"

# --- cover (numbers computed from the data)
N_ELEM = len(ELEMS)
N_PROP = len(CSS_PROPS)
N_SEL = len(SEL)
N_GALLERY = len(PROJECTS) * len(THEMES)
cover = f'''
<div class="cover">
  <div class="cover-kicker">THE COMPLETE REFERENCE · 8000 PAGES · 16 VOLUMES</div>
  <h1 class="cover-title">The 8000-Page<br><span>HTML &amp; CSS</span> Bible</h1>
  <p class="cover-sub">Every HTML element · every major CSS property · attributes, values,
  examples, and <b>live rendered results</b> on every page.</p>
  <div class="cover-stats">
    <div><b>{N_ELEM}</b><span>HTML elements</span></div>
    <div><b>{N_PROP}</b><span>CSS properties</span></div>
    <div><b>{N_SEL}</b><span>selectors</span></div>
    <div><b>{N_GALLERY}</b><span>gallery pages</span></div>
    <div><b>7000+</b><span>practice pages</span></div>
  </div>
  <p class="cover-note">Compiled from W3Schools · GeeksforGeeks · TutorialsPoint · cssreference.io ·
  Elzero Web School (Osama Elzero) · Abdelrahman Gamal · freeCodeCamp HTML5 course ·
  WeLib book archive — cross-checked against MDN.</p>
</div>'''
page(FRONT, "Cover", "Cover", "cover", cover)

# --- how to use
howto = f'''
<h2>How to use this book</h2>
<ul>
<li><b>16 volumes × 500 pages</b> — open <code>index.html</code> (the Content Map) first. Every chapter
links to its starting page; every page has prev/next arrows, a <b>page-jump box</b> (type any page
1–8000), and a TOC button.</li>
<li><b>Keyboard:</b> ← / → move between pages.</li>
<li><b>Every element page</b> = what it is → attributes table → example code → <b>live rendered result</b> → notes → related elements.</li>
<li><b>Every CSS page</b> = what it does → values table → example → <b>live demo</b> → related properties.</li>
<li><b>Part IV</b> is the fast-lookup zone: the full element × attribute matrix and the complete CSS
property index (all ~350 properties, one line each).</li>
<li><b>Part VI</b> — “The 8000 Practice Pages” — is a generated drill bank: each page pairs a real
element with a real CSS property (exercise + solution + live result). Use them for spaced repetition.</li>
<li><b>Print to PDF:</b> each volume is print-ready (A4, one book-page per sheet, page numbers).
Print volume by volume — the whole 8000 pages is a big PDF (~100 MB); 500 pages per print job is comfortable.</li>
</ul>
<div class="callout">Be honest with yourself: the first ~900 pages are a hand-curated reference.
The remaining ~7100 pages are a <b>generated practice bank</b> built from the same real elements and
properties (deterministic combinations — the same page number always gives the same drill).
The knowledge is real; the padding is labeled.</div>'''
page(FRONT, "Reader's Guide", "How to use this book", "guide", howto)

# --- content map (built after numbering; placeholder body replaced later)
page(FRONT, "Content Map", "Content Map — where everything is", "map", "…map…")

# --- element status list (built after element pages numbered)
page(FRONT, "Element List", "All HTML Elements — full list, grouped", "list", "…list1…")
page(FRONT, "Element List", "All HTML Elements — full list, grouped (continued)", "list", "…list2…")

# --- references
refs_rows = [
    ("W3Schools — HTML Tutorial", "https://www.w3schools.com/html/", "Element/attribute baseline for Part I"),
    ("W3Schools — CSS Reference", "https://www.w3schools.com/css/", "Property baseline for Part II"),
    ("GeeksforGeeks — HTML5", "https://www.geeksforgeeks.org/html/html5/", "HTML5 element coverage & notes"),
    ("TutorialsPoint — HTML5 Tutorial", "https://www.tutorialspoint.com/html5/index.htm", "Structure, forms, tables chapters"),
    ("cssreference.io", "https://cssreference.io/", "Visual CSS property catalog (Part II & IV)"),
    ("Elzero Web School — Osama Elzero (YouTube)", "https://www.youtube.com/@elzero-web", "Arabic full HTML/CSS course structure (chapters & exercises)"),
    ("Abdelrahman Gamal (YouTube)", "—", "HTML/CSS course content (Egyptian curriculum)"),
    ("freeCodeCamp — “Learn HTML5 – full course with code samples”", "https://youtu.be/DPnqb74Smug", "52-minute beginner HTML course (Eric Tirado)"),
    ("WeLib book archive", "https://welib.net", "Classic HTML/CSS books (e.g. Head First HTML & CSS, Learn to Code) — curriculum aligned (not copied)"),
    ("MDN Web Docs", "https://developer.mozilla.org", "Cross-check for every element/property (spec truth)"),
    ("Udemy-style full-stack curricula", "—", "The 10-module learning path in Appendix §12 mirrors top-rated HTML/CSS courses"),
]
page(FRONT, "References", "Sources & references", "refs",
     f"<p>This book integrates the following sources. Where sources disagreed, the <b>W3C spec / MDN</b> won.</p>"
     + table([(a, f'<a href="{H.escape(b)}">{esc(a)}</a>', c) for a, b, c in refs_rows], ("Source", "Link", "Used for"), raw=True))

# ================================================================ PART I: HTML
PART1 = "Part I — HTML: Every Element"

HTML_CHAPTERS = [
    ("Chapter 1 · Document Metadata", ["Document Metadata"]),
    ("Chapter 2 · Document Structure & Semantics", ["Document Structure"]),
    ("Chapter 3 · Text & Inline Content", ["Text & Inline"]),
    ("Chapter 4 · Lists", ["Lists"]),
    ("Chapter 5 · Media & Embedded Content", ["Media & Embedded"]),
    ("Chapter 6 · Forms & Input", ["Forms"]),
    ("Chapter 7 · Tables", ["Tables"]),
    ("Chapter 8 · Legacy & Obsolete Elements", ["Legacy & Obsolete"]),
    ("Chapter 9 · Links, Web Components & More", ["Links & Navigation", "Web Components"]),
]

def chapter_intro(title, blurb, items):
    lis = []
    for n in items:
        if isinstance(n, tuple):
            lis.append(f'<li><a class="goto" data-goto="{esc(n[0])}">{esc(n[0])}</a></li>')
        else:
            lis.append(f"<li>{esc(n)}</li>")
    body = f"<h2>{esc(title)}</h2><p>{esc(blurb)}</p><div class=\"tocbox\"><h3>On this chapter's pages</h3><ol>{''.join(lis)}</ol></div>"
    return body

# we'll build chapter intros after element pages exist (so links have page numbers)
# store the element index first:
E_BY_TAG = {e["t"]: e for e in ELEMS}
E_BY_CAT = {}
for e in ELEMS:
    E_BY_CAT.setdefault(e["cat"], []).append(e)

def element_body(e):
    st = e.get("st", "standard")
    b = [f'<h2><code class="tag">&lt;{esc(e["t"])}&gt;</code> — {esc(e["n"])}</h2>']
    b.append(f'<div class="crumb-row">{badge(e["cat"], "cat")} {badge(st, "st-" + st)}</div>')
    b.append(f'<p class="sum">{esc(e["s"])}</p>')
    b.append(f'<div class="desc">{esc(e["d"])}</div>')
    if e["A"]:
        b.append("<h3>Attributes</h3>")
        b.append(table([(a, t, d) for a, t, d in e["A"]], ("Attribute", "Type", "Description")))
    if e.get("ex"):
        b.append("<h3>Example</h3>")
        b.append(code_block(e["ex"]))
    if e.get("dm"):
        b.append("<h3>Live result</h3>")
        b.append(demo_box(e["dm"]))
    if e.get("notes"):
        b.append("<h3>Notes & best practices</h3><ul>" +
                 "".join(f"<li>{esc(n)}</li>" for n in e["notes"]) + "</ul>")
    if e.get("rel"):
        rels = " · ".join(f"<code class='tag'>&lt;{esc(r)}&gt;</code>" for r in e["rel"] if r in E_BY_TAG)
        if rels:
            b.append(f'<p class="rel">Related: {rels}</p>')
    return "".join(b)

# ================================================================ PART II: CSS
PART2 = "Part II — CSS: Every Property"

def css_chapters():
    groups = {}
    for p in CSS_PROPS:
        groups.setdefault(p["c"], []).append(p)
    order = ["Layout", "Box Model", "Flexbox", "Grid", "Positioning", "Typography",
             "Color", "Background", "Effects", "Motion", "Motion & 3D", "UI",
             "Performance", "Scroll-driven", "3D Transforms", "Tables",
             "Flexbox & Grid", "Grid & Flex", "Generated Content",
             "Form state" ]
    keys = list(groups.keys())
    return keys

CSS_CHAPTER_DEFS = [
    ("Chapter 1 · Display, Box Model & Sizing", "display, box-sizing, width/height, min/max, aspect-ratio"),
    ("Chapter 2 · Spacing: Margin, Padding & Gap", "the four margin/padding shorthands + logical properties + gap"),
    ("Chapter 3 · Borders, Outlines & Shadows", "border shorthands, border-radius, outline, box-shadow"),
    ("Chapter 4 · Float, Position & Overflow", "float/clear, position (5 schemes), z-index, overflow"),
    ("Chapter 5 · Flexbox", "the complete flex layout system, property by property"),
    ("Chapter 6 · Grid", "the complete grid layout system, property by property"),
    ("Chapter 7 · Typography & Text", "fonts, line-height, text alignment, decoration, wrapping"),
    ("Chapter 8 · Color & Background", "color, backgrounds, gradients, opacity, color-scheme"),
    ("Chapter 9 · Effects: Filter, Mask, Clip, Blend", "filter, backdrop-filter, mix-blend, mask, clip-path"),
    ("Chapter 10 · Transitions & Animations", "transition + animation + keyframes + scroll-driven"),
    ("Chapter 11 · Transforms & Motion Paths", "transform, origin, independent translate/rotate/scale, offset-path"),
    ("Chapter 12 · Lists, Counters & Generated Content", "list styles, counters, content, quotes"),
    ("Chapter 13 · UI, Scroll & Performance Properties", "cursor, scroll-snap, overscroll, will-change, contain"),
]

def prop_body(p):
    b = [f'<h2><code class="prop">{esc(p["p"])}</code></h2>']
    b.append(f'<div class="crumb-row">{badge(p["c"], "cat")}'
             + (f' <span class="ini">initial: {esc(p["ini"])}</span>' if p.get("ini") else "") + "</div>")
    b.append(f'<p class="sum">{esc(p["s"])}</p>')
    b.append(f'<div class="desc">{esc(p["d"])}</div>')
    if p.get("V"):
        b.append("<h3>Values</h3>")
        b.append(kv_table([(v, d) for v, d in p["V"]]))
    if p.get("ex"):
        b.append("<h3>Example</h3>")
        b.append(code_block(p["ex"]))
    if p.get("dm"):
        b.append("<h3>Live demo</h3>")
        b.append(demo_box(p["dm"], "CSS demo"))
    if p.get("rel"):
        rels = " · ".join(f"<code class='prop'>{esc(r)}</code>" for r in p["rel"])
        b.append(f'<p class="rel">Related: {rels}</p>')
    return "".join(b)

def selector_body(s):
    b = [f'<h2><code class="prop">{esc(s["n"])}</code> <span class="mut">— {esc(s["k"])}</span></h2>']
    b.append(f'<p class="sum">{esc(s["s"])}</p>')
    b.append(f'<div class="desc">{esc(s["d"])}</div>')
    b.append("<h3>Example</h3>" + code_block(s["ex"]))
    if s.get("dm"):
        b.append("<h3>Live demo</h3>" + demo_box(s["dm"], "Selector demo"))
    return "".join(b)

def atr_body(a):
    b = [f'<h2><code class="prop">{esc(a["n"])}</code> <span class="mut">— at-rule</span></h2>']
    b.append(f'<p class="sum">{esc(a["s"])}</p>')
    b.append(f'<div class="desc">{esc(a["d"])}</div>')
    b.append("<h3>Example</h3>" + code_block(a["ex"]))
    return "".join(b)

def val_body(v):
    b = [f'<h2><code class="prop">{esc(v["n"])}</code> <span class="mut">— value keyword / function</span></h2>']
    b.append(f'<p class="sum">{esc(v["s"])}</p>')
    b.append(f'<div class="desc">{esc(v["d"])}</div>')
    b.append("<h3>Example</h3>" + code_block(v["ex"]))
    if v.get("dm"):
        b.append("<h3>Live demo</h3>" + demo_box(v["dm"], "Value demo"))
    return "".join(b)

# ================================================================ PART III: GALLERY
PART3 = "Part III — Component Gallery (HTML + CSS)"

def project_body(proj, theme_name, theme_filter):
    st = f"filter:{theme_filter};" if theme_filter else ""
    wrap = f'<div style="{st}">{proj["html"]}</div>' if theme_filter else proj["html"]
    b = [f'<h2>{esc(proj["t"])} <span class="mut">· theme: {esc(theme_name)}</span></h2>']
    b.append(f'<p class="sum">{esc(proj["s"])}</p>')
    b.append("<h3>Live component</h3>" + demo_box(wrap, f"{proj['t']} — rendered"))
    b.append("<h3>The code</h3>")
    b.append(code_block(proj["html"]))
    if theme_filter:
        b.append(f'<p class="mut">Theme applied via <code>filter: {esc(theme_filter)}</code> on the wrapper '
                 f"(original colors stay in the markup — real projects swap CSS variables instead).</p>")
    return "".join(b)

# ================================================================ PART IV: MASTER TABLES
PART4 = "Part IV — Master Reference Tables"

# compact extra CSS index (the remaining cssreference properties, one line each)
CSS_EXTRA = [
    ("column-count", "Layout", "Number of multi-column boxes"), ("column-fill", "Layout", "How columns fill (auto/balance)"),
    ("column-rule", "Layout", "Shorthand for column borders"), ("column-rule-width", "Layout", "Column divider width"),
    ("column-rule-style", "Layout", "Column divider line style"), ("column-rule-color", "Layout", "Column divider color"),
    ("column-width", "Layout", "Preferred column width in multicol"), ("columns", "Layout", "Shorthand: column-width + column-count"),
    ("min-inline-size", "Box Model", "Logical min-width/height (inline axis)"), ("max-inline-size", "Box Model", "Logical max-width/height"),
    ("min-block-size", "Box Model", "Logical min-height/width (block axis)"), ("max-block-size", "Box Model", "Logical max-height/width"),
    ("inline-size", "Box Model", "Logical width/height (inline axis)"), ("block-size", "Box Model", "Logical height/width (block axis)"),
    ("inset-block-start", "Positioning", "Logical top/bottom offset"), ("inset-block-end", "Positioning", "Logical bottom/top"),
    ("inset-inline-start", "Positioning", "Logical left/right offset"), ("inset-inline-end", "Positioning", "Logical right/left"),
    ("margin-block-start", "Box Model", "Logical top margin"), ("margin-block-end", "Box Model", "Logical bottom margin"),
    ("margin-inline-start", "Box Model", "Logical left margin"), ("margin-inline-end", "Box Model", "Logical right margin"),
    ("padding-block-start", "Box Model", "Logical top padding"), ("padding-block-end", "Box Model", "Logical bottom padding"),
    ("padding-inline-start", "Box Model", "Logical left padding"), ("padding-inline-end", "Box Model", "Logical right padding"),
    ("border-block", "Box Model", "Logical top+bottom border"), ("border-block-start", "Box Model", "Logical top border"),
    ("border-block-end", "Box Model", "Logical bottom border"), ("border-inline", "Box Model", "Logical left+right border"),
    ("border-inline-start", "Box Model", "Logical left border"), ("border-inline-end", "Box Model", "Logical right border"),
    ("border-block-start-radius", "Box Model", "Logical top corner radius"), ("border-block-end-radius", "Box Model", "Logical bottom corner radius"),
    ("border-inline-start-radius", "Box Model", "Logical left corner radius"), ("border-inline-end-radius", "Box Model", "Logical right corner radius"),
    ("contain-intrinsic-size", "Performance", "Stable size placeholder for content-visibility:auto"),
    ("container", "Performance", "Shorthand: container-name + container-type"), ("container-name", "Performance", "Name for container queries"),
    ("container-type", "Performance", "inline-size / size — enables container queries"),
    ("scrollbar-gutter", "UI", "Reserve scrollbar space (stability)"), ("scroll-timeline", "Scroll-driven", "Name a scroll-timeline"),
    ("text-combine-upright", "Typography", "Combine upright vertical text (CJK)"), ("text-spacing-trim", "Typography", "Trim spaces near punctuation (CJK)"),
    ("line-break", "Typography", "Line-break strictness (loose/normal/strict)"), ("word-wrap", "Typography", "Deprecated alias of overflow-wrap"),
    ("hyphenate-character", "Typography", "The hyphen glyph used by hyphens:auto"), ("hyphenate-limit-chars", "Typography", "Hyphenation size limits"),
    ("hanging-punctuation", "Typography", "Hang punctuation outside the margin (CJK)"), ("all", "Reset", "Reset every property to initial/inherit"),
    ("inherit", "Reset", "Inherit the parent's computed value"), ("initial", "Reset", "The property's initial value"),
    ("unset", "Reset", "inherit if inherited, else initial"), ("revert", "Reset", "Back to user/UA level"),
    ("revert-layer", "Reset", "Back to the previous cascade layer"), ("font-display", "@font-face", "Swap behavior while a webfont loads"),
    ("font-palette", "Typography", "Switch a variable font's named palette"), ("font-variation-settings", "Typography", "Direct variable-font axes"),
    ("text-emphasis", "Typography", "CJK emphasis marks (dots/circles)"), ("text-emphasis-style", "Typography", "Emphasis mark shape"),
    ("text-emphasis-color", "Typography", "Emphasis mark color"), ("segment-break", "Typography", "Legacy CJK line-break control"),
    ("speak", "Speech", "Speech output (legacy)"), ("pause", "Speech", "Speech pause (legacy)"), ("rest", "Speech", "Speech rest (legacy)"),
    ("voice-family", "Speech", "Speech voice (legacy)"), ("volume", "Speech", "Speech volume (legacy)"), ("stress", "Speech", "Speech stress (legacy)"),
    ("richness", "Speech", "Speech richness (legacy)"), ("background-position-x", "Background", "Horizontal background position"),
    ("background-position-y", "Background", "Vertical background position"), ("border-top-left-radius", "Box Model", "Top-left corner radius"),
    ("border-top-right-radius", "Box Model", "Top-right corner radius"), ("border-bottom-left-radius", "Box Model", "Bottom-left corner radius"),
    ("border-bottom-right-radius", "Box Model", "Bottom-right corner radius"), ("outline-style", "Box Model", "Outline line style"),
    ("outline-width", "Box Model", "Outline thickness"), ("outline-color", "Box Model", "Outline color (invert)"),
    ("perspective-origin", "3D", "Vanishing point of perspective"), ("backdrop-filter", "Effects", "Filter the area behind the element"),
    ("mask-position", "Effects", "Mask image position"), ("mask-size", "Effects", "Mask image size"), ("mask-repeat", "Effects", "Mask tiling"),
    ("mask-origin", "Effects", "Mask origin box"), ("mask-clip", "Effects", "Mask clip box"), ("mask-mode", "Effects", "alpha / luminance"),
    ("mask-composite", "Effects", "Mask layer composition"), ("text-rendering", "Typography", "Quality vs speed tradeoff"),
    ("font-optical-sizing", "Typography", "Optical size axis"), ("font-weight", "Typography", "100–900 weight"),
    ("color-interpolation-filters", "Effects", "Filter color space (sRGB/linear)"), ("dominant-baseline", "SVG", "Text baseline in SVG"),
    ("fill", "SVG", "SVG fill color"), ("fill-opacity", "SVG", "SVG fill opacity"), ("stroke", "SVG", "SVG stroke"),
    ("stroke-width", "SVG", "SVG stroke width"), ("stroke-linecap", "SVG", "Stroke end caps"), ("stroke-dasharray", "SVG", "Stroke dashes"),
    ("paint-order", "SVG", "fill/stroke/markers order"), ("shape-rendering", "SVG", "SVG antialiasing hint"),
    ("image-rendering", "Effects", "pixelated / crisp-edges scaling"), ("object-fit", "Media", "contain/cover/crop inside replaced elements"),
    ("object-position", "Media", "Position of the replaced content"), ("overflow-anchor", "Scroll", "Scroll anchoring on/off"),
    ("overscroll-behavior-x", "UI", "X-axis overscroll"), ("overscroll-behavior-y", "UI", "Y-axis overscroll"),
    ("text-autospace", "Typography", "Inter-punctuation spacing (legacy)"), ("font-smooth", "Typography", "Antialiasing (legacy)"),
    ("kerning", "Typography", "Legacy kerning"), ("text-underline-position", "Typography", "auto/under/above underline placement"),
    ("font-variant-numeric", "Typography", "tnum/onum/zero figures"), ("font-variant-ligatures", "Typography", "Standard/common/alternate ligatures"),
    ("font-variant-east-asian", "Typography", "CJK glyph variants"), ("font-variant-alternates", "Typography", "Historic forms (CJK)"),
    ("font-variant-position", "Typography", "sub/superscript position"), ("font-variant-caps", "Typography", "Small-caps variants"),
    ("print-color-adjust", "UI", "Keep colors in print"), ("image-orientation", "Media", "EXIF rotation for images"),
    ("object-view-box", "Media", "Clip object content to a viewBox"), ("text-box", "Typography", "Shorthand: text-box-edge + trim"),
    ("text-box-edge", "Typography", "Trim box edge (CJK)"), ("text-box-trim", "Typography", "Trim leading/trailing space (CJK)"),
    ("view-transition-name", "Motion", "Name a view-transition pair"), ("text-decoration-skip", "Typography", "Skip parts under decoration (legacy)"),
    ("text-decoration-skip-ink", "Typography", "Avoid ink on underlines"), ("background-position-x", "Background", "X position"),
]
# dedupe, keep order
_seen = set()
CSS_EXTRA = [x for x in CSS_EXTRA if not (x[0] in _seen or _seen.add(x[0]))]
CSS_EXTRA = [x for x in CSS_EXTRA if x[0] not in {p["p"] for p in CSS_PROPS}]

# ================================================================ PART V: STUDY
PART5 = "Part V — Study: Glossary, Cheat Sheets & Quizzes"

CHEATS = [
    ("HTML — boilerplate & quick start", [
        ("<!doctype html>", "Tells the browser: standards mode, HTML5"),
        ("<html lang=\"en\">", "Root + language (first a11y/SEO win)"),
        ("<meta charset=\"UTF-8\">", "Encoding — must be in the first 1 KB"),
        ("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">", "Responsive — mandatory"),
        ("<title>…</title>", "Tab + search result headline"),
        ("link → style.css", "External stylesheet (cacheable)"),
        ("script defer", "JS after parsing, in order"),
    ]),
    ("Semantic elements — when to use", [
        ("<header> / <footer>", "Intro/outro blocks (page or section)"),
        ("<nav>", "Major link groups"),
        ("<main>", "The dominant content — exactly one, visible"),
        ("<article>", "Self-contained (blog post, card)"),
        ("<section>", "Thematic grouping with a heading"),
        ("<aside>", "Tangentially related (sidebar, callout)"),
        ("figure + figcaption", "Media with a caption"),
        ("<address>", "Contact info for the author"),
    ]),
    ("Text formatting tags", [
        ("<strong> / <em>", "importance / stress (meaning!)"),
        ("<b> / <i>", "stylistic highlight / alternate voice"),
        ("<mark>", "highlight (search results)"),
        ("<code> / <kbd> / <samp> / <var>", "code / keys / output / variable"),
        ("<pre><code>", "multi-line listings"),
        ("<small>", "fine print (copyright, T&Cs)"),
        ("<sub> / <sup>", "subscript / superscript"),
        ("<abbr title=\"…\">", "abbreviation + tooltip"),
    ]),
    ("All <input> types", [
        ("text / search / url / tel / email", "text-ish fields (email/tel/url validate + mobile keyboards)"),
        ("password", "masked input"),
        ("number / range", "numeric field / slider (min, max, step)"),
        ("date / time / datetime-local / month / week", "native pickers"),
        ("color", "color picker"),
        ("checkbox / radio", "multi-select / single-select (group by name)"),
        ("file (accept, multiple)", "file upload (enctype multipart!)"),
        ("hidden / submit / reset / button / image", "meta + action buttons"),
    ]),
    ("Form validation attributes", [
        ("required", "must not be empty"),
        ("min / max", "numeric or date bounds"),
        ("minlength / maxlength", "text length bounds"),
        ("pattern", "regex (no anchors)"),
        ("step", "increment (number/range/date)"),
        ("autocomplete", "autofill hint (name, email, cc-…)"),
        ("inputmode", "mobile keyboard (numeric, email…)"),
        ("novalidate (form)", "switch off native validation"),
    ]),
    ("Table anatomy", [
        ("table > caption", "the title (first child)"),
        ("colgroup > col", "style whole columns"),
        ("thead > tr > th[scope=col]", "header row"),
        ("tbody > tr > td", "data rows"),
        ("tfoot", "totals (renders last even if written first)"),
        ("colspan / rowspan", "merge cells (use sparingly)"),
        ("th scope=\"row\"", "row header"),
        ("border-collapse: collapse", "shared borders"),
    ]),
    ("Media elements cheat sheet", [
        ("img src alt width height", "image (always alt + dimensions)"),
        ("picture > source[media/type]", "adaptive images"),
        ("video controls poster", "video (muted autoplay)"),
        ("audio controls", "audio (no src = invisible)"),
        ("track kind=srclang", "captions/subtitles (.vtt)"),
        ("canvas + JS", "drawing surface"),
        ("iframe src sandbox", "embedded document"),
        ("map > area", "image map (legacy-ish)"),
    ]),
    ("Global attributes quick table", [
        ("id / class", "unique hook / style hooks"),
        ("data-*", "your own data (el.dataset)"),
        ("hidden", "display:none, a11y-safe"),
        ("inert", "grayed out + non-interactive"),
        ("dir / lang", "direction / language"),
        ("draggable / contenteditable", "DnD / inline editing"),
        ("tabindex", "focus order (0 / -1 / n)"),
        ("title", "tooltip (fallback only)"),
    ]),
    ("CSS box model", [
        ("content", "the width/height area"),
        ("padding", "inside the border"),
        ("border", "the edge"),
        ("margin", "outside (collapses for blocks)"),
        ("box-sizing: border-box", "width includes padding+border"),
        ("gap (flex/grid)", "space between items — no collapse"),
        ("aspect-ratio", "lock w:h (16/9, 1/1)"),
    ]),
    ("display — values", [
        ("block", "own line, full width"),
        ("inline", "flows with text"),
        ("inline-block", "flows + accepts w/h"),
        ("flex / grid", "layout containers"),
        ("none", "not rendered"),
        ("contents", "box disappears, children remain"),
        ("table-row/cell", "legacy table layout"),
    ]),
    ("position — values", [
        ("static", "normal flow (default)"),
        ("relative", "offset from own spot (keeps space)"),
        ("absolute", "vs nearest positioned ancestor (out of flow)"),
        ("fixed", "vs viewport (stays on scroll)"),
        ("sticky", "in flow until threshold, then sticks"),
        ("inset: 0", "pin to all 4 sides (overlay)"),
        ("z-index", "stacking (positioned only)"),
    ]),
    ("Flexbox cheat sheet", [
        ("display: flex", "make it a container"),
        ("flex-direction", "main axis (row/column)"),
        ("justify-content", "main-axis distribution"),
        ("align-items / align-self", "cross-axis alignment"),
        ("align-content", "wrapped lines distribution"),
        ("gap", "space between items"),
        ("flex: 1", "grow+shrink+0 basis (fill)"),
        ("order", "visual reorder (a11y caveat)"),
    ]),
    ("Grid cheat sheet", [
        ("display: grid", "make it a container"),
        ("grid-template-columns", "tracks: fr, px, minmax, repeat"),
        ("repeat(auto-fit, minmax(220px,1fr))", "responsive cards — no media queries"),
        ("grid-template-areas", "ASCII layout map"),
        ("gap", "row+column gap"),
        ("place-items: center", "center everything"),
        ("grid-column: 1 / -1", "span all columns"),
        ("grid-auto-flow: dense", "back-fill holes"),
    ]),
    ("Alignment: flex vs grid", [
        ("justify-content (both)", "items along main axis / columns"),
        ("align-content (both)", "lines / rows"),
        ("align-items (both)", "items cross axis / rows"),
        ("justify-items (grid)", "items inline axis"),
        ("align-self / justify-self", "per-item overrides"),
        ("place-items / place-self", "the 2-in-1 shorthands"),
    ]),
    ("Overflow & scroll", [
        ("overflow: hidden", "clip (also a clearfix)"),
        ("overflow: auto", "scroll when needed"),
        ("overflow-x: auto", "wide tables on mobile"),
        ("overflow-wrap: break-word", "long URLs wrap"),
        ("text-overflow: ellipsis", "the 3-line truncation trio"),
        ("scroll-snap-*", "carousels without JS"),
        ("overscroll-behavior: contain", "stop page bounce"),
    ]),
    ("Typography essentials", [
        ("font: size/line-height family", "shorthand (size+lh together)"),
        ("rem", "type sizes (root-relative)"),
        ("line-height 1.5–1.75", "body rhythm (unitless)"),
        ("letter-spacing .08em", "uppercase kickers"),
        ("max-width: 70ch", "comfortable line length"),
        ("text-wrap: balance", "even heading lines"),
        ("vertical-align: middle", "icons next to text"),
    ]),
    ("Color syntax", [
        ("#2563eb", "hex (or #2563eb80 with alpha)"),
        ("rgb(37 99 235)", "channels (spaces OK)"),
        ("hsl(217 91% 60%)", "hue/sat/light"),
        ("oklch(0.6 0.2 250)", "perceptual (modern tokens)"),
        ("color-mix(in srgb, a 10%, b)", "tints/shades in CSS"),
        ("currentcolor", "inherit text color"),
        ("var(--brand)", "token theming"),
    ]),
    ("Background cheat sheet", [
        ("background: shorthand", "color+image+pos+size+repeat"),
        ("background-size: cover", "fill the box (photos)"),
        ("background-position: center", "anchor the image"),
        ("background-clip: text", "gradient text"),
        ("background-attachment: fixed", "parallax (test mobile)"),
        ("repeating-linear-gradient", "stripes"),
        ("radial / conic-gradient", "glows / pies"),
    ]),
    ("Borders & shadows", [
        ("border: 1px solid #ccc", "needs a style!"),
        ("border-radius: 8px", "corners (999px = pill)"),
        ("border-radius: 50%", "circle on a square"),
        ("box-shadow: 0 4px 12px #0002", "soft elevation"),
        ("inset (shadow)", "inner shadow"),
        ("outline: 2px solid", "focus rings (no layout)"),
        ("outline-offset: 2px", "breathing room"),
    ]),
    ("Transform functions", [
        ("translate(x, y)", "move"),
        ("rotate(deg)", "turn (rotateX/Y = 3D)"),
        ("scale(x, y)", "grow (1 = normal)"),
        ("skewX(deg)", "slant"),
        ("perspective(d)", "3D depth (on parent)"),
        ("matrix(…)", "the raw math"),
        ("translate/rotate/scale (independent)", "compose with transform"),
    ]),
    ("Transitions", [
        ("transition: prop .3s ease", "animate changes"),
        ("transform/opacity", "animate these (GPU)"),
        ("ease-out", "entrances (fast→slow)"),
        ("cubic-bezier(…)", "custom curves (overshoot!)"),
        ("transition-delay: calc(i*60ms)", "stagger lists"),
        ("transition: all — use sparingly", "name the property instead"),
    ]),
    ("Animations", [
        ("@keyframes from/to", "define the timeline"),
        ("animation: name 1s linear infinite", "shorthand"),
        ("animation-fill-mode: both", "keep final state"),
        ("animation-delay: -1s", "start mid-way (desync)"),
        ("animation-direction: alternate", "ping-pong"),
        ("animation-play-state: paused", "hover-pause pattern"),
        ("animation-timeline: scroll()", "scroll-driven (no JS)"),
    ]),
    ("Specificity (0,0,0,0)", [
        ("!important", "nuclear option — avoid"),
        (":is / :where lists", "lower / zero specificity"),
        ("#id", "(1,0,0) — often too strong for styling"),
        (".class, [attr], :pseudo", "(0,1,0)"),
        ("tag, ::pseudo-element", "(0,0,1)"),
        ("inheritance", "loses to any declaration"),
        ("source order", "last rule wins on ties"),
        ("@layer", "layers beat order"),
    ]),
    ("Combinators", [
        ("space (descendant)", "any depth inside"),
        ("> (child)", "direct children only"),
        ("+ (adjacent sibling)", "immediately next"),
        ("~ (general sibling)", "all following siblings"),
        ("input:checked + label", "pure-CSS toggle glue"),
        (":has(…)", "the parent selector"),
    ]),
    ("Pseudo-classes (states)", [
        (":hover / :active", "pointer / press"),
        (":focus / :focus-visible", "keyboard focus rings"),
        (":first-child / :last-child", "edges of a list"),
        (":nth-child(even)", "zebra stripes"),
        (":not / :is / :where / :has", "logical selectors"),
        (":valid / :invalid / :placeholder-shown", "form state styling"),
        (":target", "the #fragment element"),
    ]),
    ("Pseudo-elements (boxes)", [
        ("::before / ::after", "generated content (needs content:)"),
        ("::placeholder", "input hint text"),
        ("::selection", "highlight color"),
        ("::marker", "list bullets"),
        ("::backdrop", "dialog dimming layer"),
        ("::first-letter / ::first-line", "drop caps / ledes"),
        (".clearfix::after { content:\"\"; clear:both }", "the classic clearfix"),
    ]),
    ("@media patterns", [
        ("(max-width: 600px)", "mobile adjustments"),
        ("(min-width: 1024px)", "desktop upgrades (mobile-first)"),
        ("(prefers-color-scheme: dark)", "auto dark mode"),
        ("(prefers-reduced-motion)", "kill animations"),
        ("(orientation: portrait)", "screen orientation"),
        ("(min-width: 768px) and (max-width: 1023px)", "tablet band"),
        ("@media print", "PDF styles"),
    ]),
    ("Units", [
        ("px", "absolute"),
        ("rem", "× root font-size (16px)"),
        ("em", "× parent font-size (cascades!)"),
        ("% / %width", "of the containing block"),
        ("vw / vh", "1% of viewport w/h"),
        ("dvh", "dynamic mobile viewport"),
        ("ch / ex", "width of \"0\" / x-height"),
        ("fr", "grid free-space fraction"),
    ]),
    ("Z-index strategy", [
        ("auto (default)", "DOM order"),
        ("10 — sticky header", "above content"),
        ("100 — modal/backdrop", "above header"),
        ("1000 — toasts", "above modals"),
        ("negative", "behind content"),
        ("stacking context trap", "z-index can't escape its context"),
    ]),
    ("Focus & accessibility", [
        (":focus-visible { outline: 3px solid }", "the ring"),
        ("outline-offset: 2px", "don't touch the element"),
        ("<label> for every input", "the form a11y #1"),
        ("th scope=\"col\"/\"row\"", "table a11y"),
        ("alt on every img", "screen readers"),
        ("aria-* only when needed", "native HTML first"),
        ("color contrast ≥ 4.5:1", "AA text"),
    ]),
    ("Print CSS", [
        ("@media print { .no-print { display:none } }", "hide chrome"),
        (".page { break-after: page }", "one book page per sheet"),
        ("thead { display: table-header-group }", "repeat table headers"),
        ("a::after { content: \" (\" attr(href) \")\" }", "print the links"),
        ("print-color-adjust: exact", "keep backgrounds"),
        ("orphans: 3; widows: 3", "no lonely lines"),
    ]),
    ("RTL & logical properties", [
        ("margin-inline-start", "left in LTR, right in RTL"),
        ("padding-block", "top+bottom"),
        ("inset-inline-end", "logical offset"),
        ("text-align: start / end", "logical alignment"),
        ("float: inline-end", "logical float"),
        ("border-start-start-radius", "logical corner"),
        ("dir=\"auto\" / <bdi>", "mixed-direction content"),
    ]),
    ("Responsive images", [
        ("srcset + sizes", "resolution switching"),
        ("<picture> + <source>", "format (avif/webp) switching"),
        ("loading=\"lazy\"", "defer off-screen images"),
        ("width/height attributes", "prevent layout shift"),
        ("aspect-ratio in CSS", "reserve the space"),
        ("decoding=\"async\"", "decode off the main thread"),
    ]),
    ("Table styling patterns", [
        ("border-collapse: collapse", "shared borders"),
        ("th background + bottom: 2px", "header emphasis"),
        ("tbody tr:nth-child(even) bg", "zebra"),
        (".wrap { overflow-x: auto }", "mobile-safe wide tables"),
        ("td vertical-align: top", "ragged cells"),
        (".num { text-align: right; font-variant-numeric: tabular-nums }", "aligned numbers"),
    ]),
    ("Button patterns", [
        (".btn { inline-flex; gap:8px; padding:10px 18px; radius:8px }", "the base"),
        (".btn-primary bg: var(--brand) color: #fff", "main action"),
        (".btn:disabled { opacity:.5; cursor:not-allowed }", "disabled"),
        (".btn:active { translateY(1px) }", "press feedback"),
        (".btn:focus-visible { outline }", "a11y ring"),
        ("min-height: 44px", "touch target"),
    ]),
    ("The reset (minimal, sane)", [
        ("*, *::before, *::after { box-sizing: border-box }", "predictable math"),
        ("body { margin: 0 }", "no default 8px"),
        ("img, video { max-width: 100%; display: block }", "responsive media"),
        ("h1..h6, p { margin: 0 }", "you control rhythm (or keep UA margins)"),
        ("button { font: inherit }", "inherit fonts"),
        ("a { color: inherit }", "optional"),
    ]),
]

def quiz_pool():
    qs = []
    # element quiz
    for i, e in enumerate(ELEMS):
        fakes = [ELEMS[(i + o) % len(ELEMS)] for o in (37, 83, 137)]
        seen, opts = set(), []
        for f in fakes:
            if f["t"] != e["t"] and f["t"] not in seen:
                seen.add(f["t"]); opts.append(f["t"])
        while len(opts) < 3:
            t = ELEMS[(i + len(opts) * 53) % len(ELEMS)]["t"]
            if t != e["t"] and t not in seen:
                seen.add(t); opts.append(t)
        ans = random.Random(i).choice(range(4))
        opts2 = opts[:]
        opts2.insert(ans, e["t"])
        qs.append(("Which element is described by: “" + e["s"] + "”",
                   ["<%s>" % o for o in opts2], ans, "element"))
    # property quiz
    for i, pr in enumerate(CSS_PROPS):
        fakes = [CSS_PROPS[(i + 41) % len(CSS_PROPS)], CSS_PROPS[(i + 97) % len(CSS_PROPS)], CSS_PROPS[(i + 151) % len(CSS_PROPS)]]
        seen, opts = set(), []
        for f in fakes:
            if f["p"] != pr["p"] and f["p"] not in seen:
                seen.add(f["p"]); opts.append(f["p"])
        while len(opts) < 3:
            t = CSS_PROPS[(i + len(opts) * 53) % len(CSS_PROPS)]["p"]
            if t != pr["p"] and t not in seen:
                seen.add(t); opts.append(t)
        ans = random.Random(1000 + i).choice(range(4))
        opts2 = opts[:]; opts2.insert(ans, pr["p"])
        qs.append(("Which CSS property: “" + pr["s"] + "”", opts2, ans, "property"))
    # selector quiz
    for i, s in enumerate(SEL):
        fakes = [SEL[(i + 11) % len(SEL)], SEL[(i + 19) % len(SEL)], SEL[(i + 29) % len(SEL)]]
        seen, opts = set(), []
        for f in fakes:
            if f["n"] != s["n"] and f["n"] not in seen:
                seen.add(f["n"]); opts.append(f["n"])
        while len(opts) < 3:
            t = SEL[(i + len(opts) * 7) % len(SEL)]["n"]
            if t != s["n"] and t not in seen:
                seen.add(t); opts.append(t)
        ans = random.Random(2000 + i).choice(range(4))
        opts2 = opts[:]; opts2.insert(ans, s["n"])
        qs.append(("What does this selector do? “" + s["s"] + "”", opts2, ans, "selector"))
    # value quiz
    for i, pr in enumerate(CSS_PROPS):
        if not pr.get("V"):
            continue
        vals = list(dict.fromkeys(v[0] for v in pr["V"] if " " not in v[0] and "(" not in v[0]))[:2]
        if len(vals) < 2:
            continue
        pool = ["banana", "solid2", "auto2", "never", "always", "banana2", "auto9"]
        fakes = [pool[(i + j) % len(pool)] for j in range(4) if pool[(i + j) % len(pool)] not in vals][:2]
        ans = random.Random(3000 + i).choice(range(4))
        real = vals[random.Random(4000 + i).randint(0, 1)]
        rest = [o for o in vals if o != real] + fakes
        opts2 = [None] * 4
        opts2[ans] = real
        k = 0
        for pos in range(4):
            if pos != ans:
                opts2[pos] = rest[k]
                k += 1
        qs.append(("Which is a valid value of " + pr["p"] + "?", opts2, ans, "value"))
    # attribute quiz
    for i, (a, d, ex) in enumerate(GLOBAL_ATTRS):
        fakes = [GLOBAL_ATTRS[(i + 5) % len(GLOBAL_ATTRS)][0], GLOBAL_ATTRS[(i + 11) % len(GLOBAL_ATTRS)][0], GLOBAL_ATTRS[(i + 17) % len(GLOBAL_ATTRS)][0]]
        seen, opts = set(), []
        for f in fakes:
            if f != a and f not in seen:
                seen.add(f); opts.append(f)
        while len(opts) < 3:
            t = GLOBAL_ATTRS[(i + len(opts) * 9) % len(GLOBAL_ATTRS)][0]
            if t != a and t not in seen:
                seen.add(t); opts.append(t)
        ans = random.Random(5000 + i).choice(range(4))
        opts2 = opts[:]; opts2.insert(ans, a)
        qs.append(("Which global attribute: “" + d + "”", opts2, ans, "attribute"))
    return qs

QUIZ_POOL = quiz_pool()

# ================================================================ PART VI: DRILLS
PART6 = "Part VI — The 8000 Practice Pages"

SIMPLE_VALUES = {}
for pr in CSS_PROPS:
    vals = [v[0].strip() for v in pr.get("V", []) if " " not in v[0] and "(" not in v[0] and not v[0].startswith("e.g")]
    if vals:
        SIMPLE_VALUES[pr["p"]] = vals

FALLBACK_VALUES = {"display": "flex", "position": "relative", "color": "#2563eb",
                   "background": "linear-gradient(90deg,#2563eb,#7c3aed)",
                   "font-size": "1.1rem", "border": "1px solid #d1d5db",
                   "border-radius": "10px", "padding": "12px", "margin": "16px",
                   "width": "200px", "height": "100px", "opacity": "0.8",
                   "transform": "translateY(-4px)", "transition": "all .3s ease",
                   "box-shadow": "0 4px 12px rgba(0,0,0,.15)", "gap": "8px",
                   "z-index": "5", "overflow": "hidden"}

def drill_body(i):
    e = ELEMS[(i * 7) % len(ELEMS)]
    pr = CSS_PROPS[(i * 13 + 5) % len(CSS_PROPS)]
    vals = SIMPLE_VALUES.get(pr["p"])
    v = vals[i % len(vals)] if vals else FALLBACK_VALUES.get(pr["p"], "…")
    q = QUIZ_POOL[(i * 3) % len(QUIZ_POOL)]
    r = random.Random(i)
    b = [f'<h2>Drill {i + 1} — {esc(e["t"])} × {esc(pr["p"])}</h2>']
    b.append(f'<div class="crumb-row">{badge(e["t"], "tag")} {badge(pr["p"], "prop")}</div>')
    b.append(f'<p class="sum">Apply <code class="prop">{esc(pr["p"])}</code> to '
             f'<code class="tag">&lt;{esc(e["t"])}&gt;</code> — {esc(e["s"].lower()).strip("." )}. '
             f'{esc(pr["s"])}</p>')
    b.append('<h3>1 · The element</h3>')
    b.append(demo_box(e["dm"] if e["dm"] else "<i>(no visual demo)</i>", f"<{e['t']}> as rendered"))
    b.append('<h3>2 · Starter code</h3>' + code_block(e["ex"] or f"<{e['t']}>…</{e['t']}>"))
    b.append('<h3>3 · Your task</h3><ul>'
             f'<li>Write one CSS rule that applies <b>{esc(pr["p"])}</b> = <b>{esc(v)}</b> to the element.</li>'
             f'<li>Explain (1 sentence) what changes in the browser.</li></ul>')
    b.append('<h3>4 · Solution</h3>' + code_block(f'{e["t"]} {{\n  {pr["p"]}: {v};\n}}'))
    if pr.get("V"):
        b.append("<h3>5 · Value quick-quiz</h3>")
        opts = q[1]
        letters = "ABCD"
        lis = "".join(f'<li>{"✔ " if j == q[2] else ""}{letters[j]}. <code>{esc(o)}</code></li>' for j, o in enumerate(opts))
        b.append(f'<p class="mut">{esc(q[0])}</p><ul class="quiz">{lis}</ul>')
    return "".join(b)

# ================================================================ PART VII: APPENDIX
PART7 = "Part VII — Appendix"

def app(title, body):
    page(PART7, "Appendix", title, "appendix", body)

app("A1 · The 10-module learning path (Udemy-style)",
    "<p>The most popular paid HTML/CSS courses (and the free ones this book cites) all follow the same arc. Each module maps to a chapter of this book:</p>"
    + table([
        ("Module 1", "How the web works + first page", "Part I · Ch 1 + Appendix A4"),
        ("Module 2", "Text, links, lists, images", "Part I · Ch 3, 4, 9 + Ch 5 (img)"),
        ("Module 3", "Semantic structure (header/nav/main/article/footer)", "Part I · Ch 2"),
        ("Module 4", "Forms (every input type)", "Part I · Ch 6"),
        ("Module 5", "Tables", "Part I · Ch 7"),
        ("Module 6", "CSS basics: selectors, colors, fonts", "Part II · Ch 7 + selectors"),
        ("Module 7", "The box model + layout (flex/grid)", "Part II · Ch 1, 2, 5, 6"),
        ("Module 8", "Responsive design (media queries, units, images)", "Part II · @media + units + gallery"),
        ("Module 9", "Components: buttons, cards, modals, forms UI", "Part III (Gallery)"),
        ("Module 10", "Polish: transitions, animations, a11y, deploy", "Part II · Ch 10–11 + Appendix a11y"),
    ]))
app("A2 · How a page loads (request → pixels)",
    "<ol><li>You type a URL → DNS → the server sends HTML.</li>"
    "<li>The browser parses HTML top-to-bottom, building the <b>DOM</b>.</li>"
    "<li><code>&lt;link&gt;</code> CSS is fetched and parsed into the <b>CSSOM</b> (rendering blocks until it arrives — put CSS in <head>, JS with <code>defer</code> at the end).</li>"
    "<li>DOM + CSSOM → <b>render tree</b> (visible elements + computed styles).</li>"
    "<li><b>Layout</b>: geometry (box model math, flex/grid solves).</li>"
    "<li><b>Paint</b>: pixels onto layers → <b>composite</b> on the GPU.</li></ol>"
    "<p class=\"mut\">Scrolling/zooming and <code>transform</code>/<code>opacity</code> animations skip steps 4–5 (that's why they're cheap).</p>")
app("A3 · DevTools tour (10 minutes)",
    "<ul><li><b>Elements panel</b> — live DOM; edit classes inline; inspect any node (F12 or right-click → Inspect).</li>"
    "<li><b>Computed</b> — the final values + which rules contributed (specificity visible).</li>"
    "<li><b>Styles</b> — the cascade in action; strike-throughs = lost rules.</li>"
    "<li><b>Console</b> — <code>document.querySelector('main')</code>, <code>getComputedStyle(el)</code>.</li>"
    "<li><b>Network</b> — see what a page actually fetched (fonts, images, 404s).</li>"
    "<li><b>Responsive mode</b> — resize the viewport; test 360px/768px/1440px.</li>"
    "<li><b>Layers / Performance</b> — compositing, reflow hotspots.</li>"
    "<li><b>Accessibility</b> — tree of landmarks, contrast warnings (Chrome).</li>"
    "<li><b>Storage</b> — cookies, local storage, service workers.</li></ul>")
app("A4 · HTML5: what's new (vs HTML 4)",
    "<p><b>New elements:</b> <code>article aside audio canvas data datalist details dialog embed figure figcaption footer header main mark meter nav output picture progress section source summary track video time wbr</code> + <code>dialog</code> APIs.</p>"
    "<p><b>New form types:</b> email, url, tel, number, range, search, date/time family, color, month, week.</p>"
    "<p><b>New capabilities:</b> <code>localStorage</code>, geolocation, WebGL, canvas 2D, drag & drop, WebSockets, Media Queries (CSS3), <code>contenteditable</code>, semantic outline (headings), offline apps.</p>"
    "<p><b>Dropped (do not use):</b> frames, applets, marquee, center, font, big, blink, strike, tt, acronym, dir, isindex, nextid, basefont.</p>")
app("A5 · Obsolete elements → modern replacement",
    table([
        ("<font>", "<span> + font-family/color CSS"),
        ("<center>", "text-align: center / margin-inline: auto"),
        ("<marquee>", "CSS animation (or nothing)"),
        ("<big>", "font-size in CSS"),
        ("<blink>", "— (removed; a11y hazard)"),
        ("<strike>", "<s> or line-through"),
        ("<tt>", "<code> or monospace"),
        ("<acronym>", "<abbr>"),
        ("<frame>/<frameset>", "<iframe> / CSS layout"),
        ("<noframes>", "remove (frames are gone)"),
        ("<applet>", "<canvas>/WebGL/JS"),
        ("<basefont>", "CSS on body"),
        ("<isindex>", "<form> + <input> + <button>"),
        ("<nextid>", "plain links"),
        ("<dir>", "<ul>/<ol>"),
    ], ("Obsolete", "Use instead")))
app("A6 · A fully semantic page (pattern)",
    code_block('''<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>My Blog — Post Title</title>
  <meta name="description" content="One-sentence summary.">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <nav><a href="/">Home</a> …</nav>
  </header>
  <main>
    <article>
      <h1>Post title</h1>
      <p>Published <time datetime="2026-09-16">Sep 16</time> by Ana</p>
      <section>
        <h2>Section</h2>
        <p>…</p>
        <figure><img src="a.jpg" alt="…" width="640" height="360" loading="lazy">
          <figcaption>Figure 1.</figcaption></figure>
      </section>
      <aside><h3>Related</h3><ul>…</ul></aside>
    </article>
  </main>
  <footer><address><a href="mailto:hi@x.com">hi@x.com</a></address></footer>
  <script src="app.js" defer></script>
</body>
</html>'''))
app("A7 · Accessibility checklist (HTML)",
    "<ul class=\"check\">".join(f"<li>{esc(x)}</li>" for x in [
        "lang on <html>", "one <h1>, ordered heading levels", "meaningful link text (no 'click here')",
        "alt on every img (empty alt for decorative)", "<label> for every input",
        "th scope on table headers", "landmarks: header/nav/main/footer",
        "buttons are <button> (not divs)", "focus order follows visual order",
        "error messages associated with the field (aria-describedby)",
        "color is not the only indicator", "target ≥ 44px on touch",
    ]) + "</ul>")
app("A8 · Accessibility checklist (CSS)",
    "<ul class=\"check\">".join(f"<li>{esc(x)}</li>" for x in [
        ":focus-visible outline on everything interactive", "never display:none the only feedback (use aria-live)",
        "contrast ≥ 4.5:1 (AA) for text", "@media (prefers-reduced-motion) → kill big animations",
        "don't rely on hover-only menus (keyboard alternative)", "text scales to 200% without breaking (use rem)",
        "don't hide info in title tooltips alone", "logical properties for RTL (margin-inline-*)",
    ]) + "</ul>")
app("A9 · Performance checklist (Core Web Vitals)",
    "<ul class=\"check\">".join(f"<li>{esc(x)}</li>" for x in [
        "LCP: hero image preloaded + sized (aspect-ratio), CSS in head, font-display: swap",
        "CLS: width/height on media, no injected ads above content, reserve ad slots",
        "INP: defer JS, no blocking inline work, batch DOM writes",
        "lazy-load below-the-fold images (loading=\"lazy\")",
        "fonts: woff2, preconnect, self-host, font-display: swap",
        "images: modern formats (avif/webp), srcset, compressed",
        "content-visibility: auto on long feeds", "critical CSS inline (small sites)",
    ]) + "</ul>")
app("A10 · Debugging HTML — 10 common errors",
    table([
        ("Page looks 'weird' / unstyled", "Doctype missing or before <html>; or CSS 404 — check Network"),
        ("Images stretched", "No width/height + width:100% — set aspect-ratio or both dimensions"),
        ("Form doesn't submit", "Missing <button type=submit> (or inside <form>? check nesting)"),
        ("Checkbox looks wrong", "No <label> association (for=id)"),
        ("Table borders double", "Missing border-collapse: collapse"),
        ("Anchor jump hidden behind header", "Target needs scroll-margin-top"),
        ("UTF-8 shows ????", "charset meta missing or not first"),
        ("Video autoplay silent-broken", "Add muted (browser rule)"),
        ("Cyrillic/Arabic garbled", "Wrong charset or file encoding — save as UTF-8"),
        ("<style> not applying", "Selector typo / specificity — Computed panel shows why"),
    ]))
app("A11 · Debugging CSS — why my style doesn't work",
    table([
        ("'It's not applying at all'", "Typo in selector; element not matching; check Elements panel"),
        ("'Another rule wins'", "Specificity! #id beat .class — Computed panel shows the winner"),
        ("'It works but not where'", "A positioned ancestor changed (absolute/fixed) — find the containing block"),
        ("'Height:100% doesn't work'", "Parent has no defined height (set it, or use min-height/dvh)"),
        ("'Flex item won't shrink'", "min-width:auto — set min-width:0 on the item"),
        ("'Margin collapsing surprises'", "Adjacent block margins collapse; use padding or flex (gap)"),
        ("'Padding on <html>/<body> breaks layout'", "Set margin:0 on body (the 8px default)"),
        ("'Gradient text not showing'", "Needs -webkit-background-clip:text AND color:transparent"),
        ("'transition not animating'", "You changed display/visibility (not animatable) or forgot the property"),
        ("'Mobile 100vh jumps'", "Use 100dvh / 100svh"),
        ("'z-index not working'", "Element not positioned — or trapped in a stacking context"),
        ("'gap in flex not working (old browser)'", "Fallback: margin on children + :first-child margin:0"),
        ("'!important war'", "Stop. Restructure with @layer or lower specificity"),
    ]))
app("A12 · Browser support strategy",
    "<p><b>Progressive enhancement</b> is the rule: core content works everywhere; fancy CSS is an upgrade.</p>"
    "<ul><li>Check <b>caniuse.com</b> before using a property (Chrome/Firefox/Safari/Edge + mobile).</li>"
    "<li>Safe today: flex, grid, custom properties, clamp, aspect-ratio, :has (all major browsers 2024+).</li>"
    "<li>Newer (gate with <code>@supports</code> or <code>cssdb</code>): container queries, scroll-driven animations, text-wrap: balance, field-sizing, color-mix (now widely OK), subgrid (now widely OK).</li>"
    "<li>Prefixes: <code>-webkit-</code> still needed for backdrop-filter, mask(-image), background-clip:text.</li>"
    "<li>Autoprefixer in a build handles most prefixes automatically.</li></ul>")
app("A13 · HTML vs CSS vs JavaScript",
    table([
        ("HTML", "Structure & content — the skeleton", "Elements, attributes, semantics"),
        ("CSS", "Presentation & layout — the skin", "Style, box model, flex/grid, motion (pure)"),
        ("JavaScript", "Behavior & data — the brain", "Interactivity, fetching, DOM changes, state"),
        ("Rule of thumb", "If CSS can do it (hover, details, tabs via :checked), don't add JS", "JS for logic, data, and impossible-in-CSS things"),
    ]))
app("A14 · Project file structure (real world)",
    code_block('''my-site/
├─ index.html
├─ css/
│  ├─ base.css      (reset, tokens, typography)
│  ├─ components.css (buttons, cards, forms)
│  └─ pages.css     (page-specific)
├─ js/
│  └─ main.js       (defer)
├─ img/  (avif/webp + srcset)
├─ fonts/ (woff2)
├─ favicon.svg
└─ README.md
Rules: lowercase-hyphen files, relative paths, one CSS per concern,
JS at the end with defer, images in <picture> when sizes differ.'''))
app("A15 · SEO basics (what HTML gives search)",
    "<ul><li>One <code>&lt;title&gt;</code> (≤ 60 chars) + <code>meta description</code> (≤ 160).</li>"
    "<li>One <code>&lt;h1&gt;</code>; headings outline the content.</li>"
    "<li>Descriptive <code>alt</code> text (images are indexed).</li>"
    "<li>Meaningful link text; internal links with logical anchors.</li>"
    "<li><code>hreflang</code> for language versions; canonical for duplicates.</li>"
    "<li>Social: og:title / og:description / og:image (+ twitter:card).</li>"
    "<li>Structured data: JSON-LD (Article, Product, FAQ, BreadcrumbList).</li>"
    "<li>Fast (Core Web Vitals) + mobile viewport = ranking inputs.</li></ul>")
app("A16 · Structured data sample (JSON-LD)",
    code_block('''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The 8000-Page HTML & CSS Bible",
  "author": { "@type": "Person", "name": "Mega Book" },
  "datePublished": "2026-09-16",
  "publisher": { "@type": "Organization", "name": "Mega Book" },
  "mainEntityOfPage": "https://example.com/html-css-bible"
}
</script>'''))
app("A17 · Security basics for front-end",
    "<ul><li><b>XSS:</b> never put raw user input in innerHTML — textContent / escaping.</li>"
    "<li><b>target=_blank:</b> always add <code>rel=\"noopener\"</code>.</li>"
    "<li><b>iframe:</b> embed unknown origins with <code>sandbox</code> + <code>referrerpolicy</code>.</li>"
    "<li><b>CSP:</b> <code>meta http-equiv=\"Content-Security-Policy\" content=\"default-src 'self'\"</code> (server-set in production).</li>"
    "<li><b>HTTPS</b> everywhere; HSTS from the server.</li>"
    "<li><b>autocomplete</b> hints: don't fight the password manager, guide it.</li>"
    "<li><b>Forms:</b> POST sensitive data; validate server-side always.</li></ul>")
app("A18 · The CSS syntax vocabulary",
    table([
        ("rule", "selector { declarations }"),
        ("declaration", "property: value;"),
        ("block", "the { … } group"),
        ("selector", "who: .card, #x, div, :hover, ::after"),
        ("at-rule", "@media, @keyframes, @font-face, @layer, @import…"),
        ("shorthand", "one property for several (margin, font, background)"),
        ("custom property", "--name: value (a CSS variable)"),
        ("specificity", "the tie-breaker (id > class > tag)"),
        ("cascade", "origin → layers → specificity → source order"),
        ("inheritance", "children get parent values (color, font…)"),
    ]))
app("A19 · Keyboard shortcuts for THIS book",
    "<ul><li>← / → — previous / next page</li>"
    "<li>Type a number in the <b>jump box</b> (footer) + Enter — go to any of the 8000 pages</li>"
    "<li><b>TOC</b> button — back to the content map</li>"
    "<li>Browser print (Ctrl/Cmd+P) — print the open volume to PDF (A4, one book-page per sheet)</li></ul>")
app("A20 · Colophon",
    f"<p><b>The 8000-Page HTML &amp; CSS Bible</b> — generated 2026-09-16. "
    f"Content compiled from the references on the References page, cross-checked against MDN/W3C specs. "
    f"HTML elements: {N_ELEM} (incl. {sum(1 for e in ELEMS if e.get('st')=='obsolete')} obsolete, documented 'do not use'). "
    f"CSS properties: {N_PROP} in-depth pages + {len(CSS_EXTRA)} one-line index entries ≈ the full cssreference.io catalog. "
    f"Selectors: {N_SEL} · At-rules: {len(ATR)} · Value keywords: {len(VAL)}. "
    f"16 volumes × 500 pages = 8000 pages. "
    f"Built as a self-contained HTML book (no network needed, no external assets — every demo is rendered live in the page). "
    f"Print it, study it, abuse it — and when you reach page 8000, you deserve a coffee.</p>")

# ================================================================ assemble order
def build_pages():
    # (already added: front placeholders, part7 appendix)
    # PART I
    for chap, cats in HTML_CHAPTERS:
        items = []
        for cat in cats:
            for e in E_BY_CAT.get(cat, []):
                title = f"<{e['t']}> — {e['n']}"
                page(PART1, chap, title, "element", element_body(e))
                items.append((title,))  # page# resolved after numbering
        intro = chapter_intro(chap, "Every element of this group, with attributes, examples, and live results.", items)
        # insert intro at the position of the first element of this chapter:
        first = next(i for i, p in enumerate(PAGES) if p["chap"] == chap and p["tag"] == "element")
        PAGES.insert(first, dict(part=PART1, chap=chap, title=chap, tag="chapter", body=intro))
    # global attributes chapter
    chap = "Chapter 10 · Global Attributes (any element)"
    PAGES.append(dict(part=PART1, chap=chap, title=chap, tag="chapter", body=chapter_intro(
        chap, "Attributes allowed on EVERY element. 36 of them.", [])))
    for a, d, ex in GLOBAL_ATTRS:
        PAGES.append(dict(part=PART1, chap=chap, title=f"{a} — global attribute", tag="attribute",
                          body=f"<h2><code class='tag'>{esc(a)}</code> <span class='mut'>— global attribute</span></h2>"
                               f"<div class='crumb-row'>{badge('works on every element','cat')}</div>"
                               f"<p class='sum'>{esc(d)}</p>"
                               f"<h3>Example</h3>{code_block('<div ' + ex + '></div>')}"
                               f"<h3>Live result</h3>" + demo_box(f"<div style='font-family:monospace;font-size:12px;border:1px dashed #94a3b8;padding:6px' {esc(ex)}>this element carries {esc(a)}</div>")))
    # attribute deep-dives
    chap = "Chapter 11 · Attribute Deep-Dives (the big controls)"
    PAGES.append(dict(part=PART1, chap=chap, title=chap, tag="chapter", body=chapter_intro(
        chap, "The elements with the most attributes, with their FULL attribute tables.", [])))
    for e in sorted(ELEMS, key=lambda x: -len(x["A"])):
        if len(e["A"]) >= 5:
            PAGES.append(dict(part=PART1, chap=chap, title=f"All attributes of <{e['t']}>", tag="deeplink",
                              body=f"<h2>Every attribute of <code class='tag'>&lt;{esc(e['t'])}&gt;</code> ({len(e['A'])} total)</h2>"
                                   f"<p class='sum'>{esc(e['s'])}</p>"
                                   + table([(a, t, d) for a, t, d in e["A"]], ("Attribute", "Type", "Description"))
                                   + f"<h3>Minimal + rich example</h3>{code_block(e['ex'])}"))
    # PART II
    for n, (chap, blurb) in enumerate(CSS_CHAPTER_DEFS):
        pass
    # assign props to chapters by category order
    chap_map = [
        (CSS_CHAPTER_DEFS[0][0], ["Layout", "Box Model", "Positioning"]),
        (CSS_CHAPTER_DEFS[1][0], []),  # spacing — handled by scanning property names
        (CSS_CHAPTER_DEFS[2][0], []),
        (CSS_CHAPTER_DEFS[3][0], []),
        (CSS_CHAPTER_DEFS[4][0], ["Flexbox", "Flexbox & Grid"]),
        (CSS_CHAPTER_DEFS[5][0], ["Grid", "Grid & Flex"]),
        (CSS_CHAPTER_DEFS[6][0], ["Typography"]),
        (CSS_CHAPTER_DEFS[7][0], ["Color", "Background", "Media"]),
        (CSS_CHAPTER_DEFS[8][0], ["Effects", "SVG", "Reset"]),
        (CSS_CHAPTER_DEFS[9][0], ["Motion", "Scroll-driven"]),
        (CSS_CHAPTER_DEFS[10][0], ["Motion & 3D", "3D Transforms"]),
        (CSS_CHAPTER_DEFS[11][0], ["Lists", "Generated Content"]),
        (CSS_CHAPTER_DEFS[12][0], ["UI", "Performance", "Speech"]),
    ]
    # spacing / border chapters by name prefix
    def prop_chap(p):
        name, cat = p["p"], p["c"]
        if name in ("border-collapse", "border-spacing"):
            return CSS_CHAPTER_DEFS[2][0]
        if name in ("display",) or cat in ("Layout", "Positioning", "Box Model"):
            if name.startswith(("margin", "padding")):
                return CSS_CHAPTER_DEFS[1][0]
            if name.startswith(("border", "outline", "box-shadow")):
                return CSS_CHAPTER_DEFS[2][0]
            if name in ("float", "clear", "position", "top", "right", "bottom", "left", "inset", "z-index",
                        "overflow", "overflow-x", "overflow-y", "visibility", "zoom", "contain",
                        "content-visibility", "perspective", "transform-style", "backface-visibility"):
                return CSS_CHAPTER_DEFS[3][0]
            return CSS_CHAPTER_DEFS[0][0]
        for chap, cats in chap_map:
            if cat in cats:
                return chap
        if cat == "Tables":
            return CSS_CHAPTER_DEFS[11][0]
        return CSS_CHAPTER_DEFS[12][0]

    groups2 = {}
    for p in CSS_PROPS:
        groups2.setdefault(prop_chap(p), []).append(p)
    for chap, blurb in CSS_CHAPTER_DEFS:
        plist = groups2.get(chap, [])
        PAGES.append(dict(part=PART2, chap=chap, title=chap, tag="chapter",
                          body=chapter_intro(chap, f"{blurb}. {len(plist)} properties.",
                                             [(p["p"], None) for p in plist])))
        for p in plist:
            PAGES.append(dict(part=PART2, chap=chap, title=p["p"], tag="property", body=prop_body(p)))
    # selectors
    chap = "Chapter 14 · Selectors"
    PAGES.append(dict(part=PART2, chap=chap, title=chap, tag="chapter",
                      body=chapter_intro(chap, "Every selector, with what it matches, examples, and live demos.", [])))
    for s in SEL:
        PAGES.append(dict(part=PART2, chap=chap, title=f"Selector {s['n']}", tag="selector", body=selector_body(s)))
    # at-rules
    chap = "Chapter 15 · At-Rules"
    PAGES.append(dict(part=PART2, chap=chap, title=chap, tag="chapter",
                      body=chapter_intro(chap, "The @-family: media, supports, container, layer, keyframes, font-face…", [])))
    for a in ATR:
        PAGES.append(dict(part=PART2, chap=chap, title=a["n"], tag="atrule", body=atr_body(a)))
    # values
    chap = "Chapter 16 · Value Keywords & Functions"
    PAGES.append(dict(part=PART2, chap=chap, title=chap, tag="chapter",
                      body=chapter_intro(chap, "The values that do the heavy lifting: calc, var, gradients, units, curves…", [])))
    for v in VAL:
        PAGES.append(dict(part=PART2, chap=chap, title=v["n"], tag="value", body=val_body(v)))
    # PART III
    for i, proj in enumerate(PROJECTS):
        for theme_name, theme_filter in THEMES:
            PAGES.append(dict(part=PART3, chap=f"Project {i + 1:02d} · {proj['t']}",
                              title=f"{proj['t']} — {theme_name}", tag="project",
                              body=project_body(proj, theme_name, theme_filter)))
    # PART IV
    PAGES.append(dict(part=PART4, chap="Master Tables", title="Part IV opens", tag="chapter",
                      body=chapter_intro("Master Reference Tables",
                                         "Fast lookup: the element × attribute matrix, the complete CSS property index, selector & value tables.", [])))
    # element x attribute matrix (8 per page)
    rows_all = []
    for e in ELEMS:
        attrs = ", ".join(a[0] for a in e["A"]) or "—"
        st = e.get("st", "standard")
        rows_all.append((f"<code class='tag'>&lt;{esc(e['t'])}&gt;</code>", e["n"], e["cat"],
                         f"<code style='font-size:11px'>{esc(attrs)}</code>", st))
    for i in range(0, len(rows_all), 8):
        PAGES.append(dict(part=PART4, chap="Element × Attribute Matrix",
                          title=f"Element matrix {i // 8 + 1}", tag="matrix",
                          body=f"<h2>Element × Attribute Matrix — part {i // 8 + 1}</h2>"
                               + table(rows_all[i:i + 8], ("Element", "Name", "Category", "Attributes", "Status"), raw=True)))
    # full css index (20 per page): in-depth props + extra one-liners
    css_index = [(p["p"], p["c"], p["s"]) for p in CSS_PROPS] + [(n, c, s) for n, c, s in CSS_EXTRA]
    for i in range(0, len(css_index), 20):
        PAGES.append(dict(part=PART4, chap="Complete CSS Property Index",
                          title=f"CSS index {i // 20 + 1}", tag="matrix",
                          body=f"<h2>Complete CSS Property Index — part {i // 20 + 1} of {math.ceil(len(css_index) / 20)}</h2>"
                               + table([(f"<code class='prop'>{esc(n)}</code>", c, s) for n, c, s in css_index[i:i + 20]],
                                       ("Property", "Category", "One-line description"), raw=True)))
    # selectors table (24/page)
    for i in range(0, len(SEL), 24):
        PAGES.append(dict(part=PART4, chap="Selector Index", title=f"Selectors {i // 24 + 1}", tag="matrix",
                          body=f"<h2>Selector Index — part {i // 24 + 1}</h2>"
                               + table([(f"<code class='prop'>{esc(s['n'])}</code>", s["k"], s["s"]) for s in SEL[i:i + 24]],
                                       ("Selector", "Kind", "What it matches"), raw=True)))
    # global attrs table (18/page)
    for i in range(0, len(GLOBAL_ATTRS), 18):
        PAGES.append(dict(part=PART4, chap="Global Attribute Index", title=f"Global attrs {i // 18 + 1}", tag="matrix",
                          body=f"<h2>Global Attribute Index — part {i // 18 + 1}</h2>"
                               + table([(f"<code class='tag'>{esc(a)}</code>", d) for a, d, ex in GLOBAL_ATTRS[i:i + 18]],
                                       ("Attribute", "Description"), raw=True)))
    # PART V
    for i in range(0, len(GLOSSARY), 6):
        chunk = GLOSSARY[i:i + 6]
        PAGES.append(dict(part=PART5, chap="Glossary", title=f"Glossary {i // 6 + 1}", tag="glossary",
                          body=f"<h2>Glossary — part {i // 6 + 1} of {math.ceil(len(GLOSSARY) / 6)}</h2>"
                               + table([(f"<b>{esc(k)}</b>", v) for k, v in chunk], ("Term", "Definition"))))
    for title, rows in CHEATS:
        PAGES.append(dict(part=PART5, chap="Cheat Sheets", title=title, tag="cheat",
                          body=f"<h2>Cheat Sheet — {esc(title)}</h2>" + table(rows, ("Rule / Value", "What it does"))))
    for z in range(120):
        start = (z * 7) % len(QUIZ_POOL)
        qs = [QUIZ_POOL[(start + k) % len(QUIZ_POOL)] for k in range(5)]
        lis = []
        for k, (q, opts, ans, kind) in enumerate(qs, 1):
            letters = "ABCD"
            ol = "".join(f"<li>{'✔ ' if j == ans else ''}{letters[j]}. <code>{esc(o)}</code></li>"
                         for j, o in enumerate(opts))
            lis.append(f"<p><b>{k}.</b> {esc(q)} <span class='mut'>({kind})</span></p><ol class='quiz'>{ol}</ol>")
        PAGES.append(dict(part=PART5, chap="Quizzes", title=f"Quiz {z + 1}", tag="quiz",
                          body=f"<h2>Quiz {z + 1} / 120</h2><p class='mut'>5 questions · answers marked ✔</p>" + "".join(lis)))
    return PAGES

# ================================================================ render
STYLE = """
:root{--ink:#1e293b;--mut:#64748b;--line:#e2e8f0;--bg:#f1f5f9;--accent:#4f46e5;--accent2:#0ea5e9;--code:#0f172a}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
.page{max-width:880px;margin:0 auto;background:#fff;min-height:100vh;padding:44px 56px 20px;position:relative;
  box-shadow:0 0 24px #0f172a14;border-left:1px solid var(--line);border-right:1px solid var(--line)}
.pg-head{display:flex;justify-content:space-between;font-size:12px;color:var(--mut);border-bottom:1px solid var(--line);
  padding-bottom:8px;margin-bottom:22px}
.pg-head .crumb{text-transform:uppercase;letter-spacing:.08em;font-weight:600}
h1,h2,h3{line-height:1.25;color:#0f172a}
h2{font-size:26px;margin:0 0 10px}
h3{font-size:16px;margin:20px 0 8px;color:#334155}
p{margin:10px 0}
.sum{font-size:17px;font-weight:600;color:#0f172a;margin:4px 0 8px}
.desc{color:#334155}
.mut{color:var(--mut);font-size:14px}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.92em;background:#eef2ff;color:#3730a3;
  padding:1px 6px;border-radius:6px}
code.tag{background:#ecfdf5;color:#047857}
code.prop{background:#fff7ed;color:#c2410c}
pre.code{background:var(--code);color:#e2e8f0;border-radius:10px;padding:14px 16px;overflow-x:auto;font-size:13px;
  line-height:1.6;margin:8px 0}
pre.code code{background:none;color:inherit;padding:0}
table.ref{width:100%;border-collapse:collapse;font-size:13.5px;margin:10px 0}
table.ref th{background:#f8fafc;text-align:left;padding:8px 10px;border-bottom:2px solid var(--line);font-size:12px;
  text-transform:uppercase;letter-spacing:.05em;color:#475569}
table.ref td{padding:8px 10px;border-bottom:1px solid #f1f5f9;vertical-align:top}
table.ref tr:nth-child(even) td{background:#fafbfc}
table.ref tr.grp td{background:#eef2ff;border-top:2px solid #c7d2fe;font-weight:700;font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:#3730a3;padding:10px}
.badge{display:inline-block;font-size:11px;font-weight:600;padding:2px 10px;border-radius:99px;background:#e0e7ff;color:#3730a3}
.badge.cat{background:#e0f2fe;color:#0369a1}
.badge.st-obsolete{background:#fee2e2;color:#991b1b}
.badge.tag{background:#ecfdf5;color:#047857;font-family:monospace}
.badge.prop{background:#fff7ed;color:#c2410c;font-family:monospace}
.ini{font-size:12px;color:var(--mut);font-family:monospace}
.demo{border:1px solid var(--line);border-radius:12px;overflow:hidden;margin:10px 0;background:#fff}
.demo-bar{background:#f8fafc;border-bottom:1px solid var(--line);padding:7px 12px;display:flex;gap:5px;align-items:center}
.demo-bar span{width:10px;height:10px;border-radius:50%;background:#e2e8f0}
.demo-bar span:first-child{background:#fca5a5}.demo-bar span:nth-child(2){background:#fde68a}.demo-bar span:nth-child(3){background:#86efac}
.demo-bar em{margin-left:auto;font-size:11px;color:var(--mut);font-style:normal}
.demo-body{padding:18px;overflow-x:auto;background:
  linear-gradient(#fff 0 0) padding-box}
.rel{font-size:14px;color:var(--mut)}
.tocbox{background:#f8fafc;border:1px solid var(--line);border-radius:12px;padding:14px 18px;margin:12px 0;columns:2;column-gap:28px}
.tocbox h3{margin-top:0}
.tocbox ol{margin:0;padding-left:20px;font-size:14px}
.tocbox li{margin:3px 0;break-inside:avoid}
.tocbox a{color:var(--accent);text-decoration:none}
.tocbox a:hover{text-decoration:underline}
.callout{background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px 18px;font-size:15px}
.cover{min-height:70vh;display:flex;flex-direction:column;justify-content:center;text-align:center;padding:40px 10px}
.cover-kicker{font-size:12px;letter-spacing:.2em;color:var(--mut);font-weight:700}
.cover-title{font-size:64px;line-height:1.05;margin:18px 0;font-weight:900;letter-spacing:-.02em}
.cover-title span{background:linear-gradient(90deg,var(--accent),var(--accent2));-webkit-background-clip:text;background-clip:text;color:transparent}
.cover-sub{font-size:19px;color:#334155;max-width:560px;margin:0 auto}
.cover-stats{display:flex;gap:26px;justify-content:center;margin:30px 0;flex-wrap:wrap}
.cover-stats b{display:block;font-size:30px;color:var(--accent)}
.cover-stats span{font-size:12px;color:var(--mut)}
.cover-note{font-size:13px;color:var(--mut);max-width:620px;margin:0 auto}
ul.check li::marker{content:"✓  ";color:#16a34a}
ol.quiz li{margin:3px 0}
.pg-foot{position:sticky;bottom:0;display:flex;gap:10px;align-items:center;background:rgba(255,255,255,.92);
  backdrop-filter:blur(6px);border-top:1px solid var(--line);margin:26px -56px -20px;padding:10px 56px;font-size:13px}
.pg-foot a{display:inline-block;padding:6px 14px;border-radius:8px;text-decoration:none;color:var(--accent);
  background:#eef2ff;font-weight:600}
.pg-foot a:hover{background:#e0e7ff}
.pg-foot .num{color:var(--mut)}
.pg-foot .jump{margin-left:auto;display:flex;gap:6px;align-items:center;color:var(--mut)}
.pg-foot input{width:70px;padding:5px 8px;border:1px solid var(--line);border-radius:8px;font-size:13px}
@media print{
  @page{size:A4;margin:11mm}
  body{background:#fff}
  .page{box-shadow:none;border:none;min-height:auto;page-break-after:always;padding:0;max-width:none}
  .pg-foot{display:none}
  .demo{break-inside:avoid}
  table.ref{break-inside:auto}
  tr{break-inside:avoid}
}
"""

SCRIPT = """
(function(){
  var pageEl = document.querySelector('.page[data-page]');
  if(!pageEl) return;
  // hash scroll
  function goHash(){
    if(location.hash){
      var t = document.querySelector(location.hash);
      if(t) t.scrollIntoView();
    }
  }
  window.addEventListener('load', goHash);
  window.addEventListener('hashchange', goHash);
  // keyboard
  document.addEventListener('keydown', function(e){
    if(e.target.matches('input,textarea')) return;
    if(e.key === 'ArrowRight'){ var n = document.querySelector('a[data-nav="next"]'); if(n) n.click(); }
    if(e.key === 'ArrowLeft'){ var p = document.querySelector('a[data-nav="prev"]'); if(p) p.click(); }
  });
  // jump (every page has one)
  var boxes = document.querySelectorAll('.jump-input');
  for(var bi = 0; bi < boxes.length; bi++){
    (function(box){
      box.addEventListener('keydown', function(e){
        if(e.key !== 'Enter') return;
        var n = parseInt(box.value, 10);
        if(!n || n < 1 || n > 8000){ box.value=''; box.placeholder='1–8000'; return; }
        var vol = Math.ceil(n / 500);
        location.href = 'vol-' + String(vol).padStart(2, '0') + '.html' + '#p' + n;
      });
    })(boxes[bi]);
  }
})();
"""

def finalize_gotos(pages):
    """Replace data-goto links with real page anchors (same-volume or cross-volume)."""
    t2n = {}
    for no, p in enumerate(pages, 1):
        t2n.setdefault(p["title"], no)
    for idx, p in enumerate(pages):
        cur_no = idx + 1
        cur_vol = cur_no // PER_VOLUME  # 0-based volume index of THIS page

        def rep(m, cur_vol=cur_vol):
            title = H.unescape(m.group(1))
            no = t2n.get(title)
            if not no:
                return '<a class="goto">'
            vol = (no - 1) // PER_VOLUME
            if vol == cur_vol:
                return f'<a href="#p{no}">'
            return f'<a href="../volumes/vol-{vol + 1:02d}.html#p{no}">'
        p["body"] = re.sub(r'<a class="goto" data-goto="([^"]*)"[^>]*>', rep, p["body"])

def render_page(p, no, total):
    part = p["part"]
    prev_no, next_no = no - 1, no + 1
    def navlink(n, label, key):
        if n < 1 or n > total:
            return f'<span class="num">{label}</span>'
        if (n - 1) // PER_VOLUME == (no - 1) // PER_VOLUME:
            return f'<a data-nav="{key}" href="#p{n}">{label}</a>'
        vol = (n - 1) // PER_VOLUME + 1
        return f'<a data-nav="{key}" href="../volumes/vol-{vol:02d}.html#p{n}">{label}</a>'
    foot = f'''<div class="pg-foot">
      {navlink(prev_no, "← Prev", "prev")}
      <span class="num">Page {no} / {total} · {esc(p["chap"][:44])}</span>
      {navlink(next_no, "Next →", "next")}
      <span class="jump">Go to <input class="jump-input" type="number" min="1" max="8000" placeholder="page"> <a href="../index.html">🗺 Map</a></span>
    </div>'''
    head = f'''<div class="pg-head"><span class="crumb">{esc(part)} · {esc(p["chap"])}</span><span>Page {no} of {total}</span></div>'''
    return (f'<section class="page" id="p{no}" data-page="{no}" data-tag="{p["tag"]}" data-title="{esc(p["title"])}">\n'
            f'{head}\n{p["body"]}\n{foot}\n</section>\n')

def render_volume(vol_no, pages_with_nos):
    parts = "".join(render_page(p, no, TOTAL_PAGES) for no, p in pages_with_nos)
    vol_pages = [no for no, _ in pages_with_nos]
    title = f"Volume {vol_no:02d} · Pages {vol_pages[0]}–{vol_pages[-1]}"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The 8000-Page HTML &amp; CSS Bible — {title}</title>
<style>{STYLE}</style>
</head>
<body>
{parts}
<script>{SCRIPT}</script>
</body>
</html>
'''

def render_index(pages):
    # content map (front page #3) + element lists (pages #4,#5) filled here
    # parts overview with page ranges
    parts = {}
    for no, p in enumerate(pages, 1):
        parts.setdefault(p["part"], [no, no, 0])
        parts[p["part"]][1] = no
        parts[p["part"]][2] += 1
    part_links = []
    for name, (a, b, n) in parts.items():
        vol = (a - 1) // PER_VOLUME + 1
        part_links.append(
            f'<li><a href="volumes/vol-{vol:02d}.html#p{a}"><b>{esc(name)}</b></a> '
            f'<span class="mut">pages {a}–{b} · {n} pages</span></li>')
    map_body = f'''<h2>Content Map</h2>
<p>8000 pages in 7 parts + front matter. Jump to any part, then use the in-book navigation.</p>
<ul>{''.join(part_links)}</ul>
<div class="callout"><b>Tip:</b> open any volume and type a page number in the jump box (bottom-right) —
it carries you across volumes automatically. Keyboard ← / → flips pages.</div>
<h3>Volume index</h3>
<table class="ref"><thead><tr><th>Volume</th><th>Pages</th><th>Opens with</th></tr></thead><tbody>'''
    for v in range(1, VOLUMES + 1):
        first_no = (v - 1) * PER_VOLUME + 1
        first_p = pages[first_no - 1]
        map_body += (f'<tr><td><a href="volumes/vol-{v:02d}.html">vol-{v:02d}.html</a></td>'
                     f'<td>{first_no}–{first_no + PER_VOLUME - 1}</td><td>{esc(first_p["part"])} · {esc(first_p["chap"][:40])}</td></tr>')
    map_body += "</tbody></table>"
    # replace the placeholder map page body
    for p in pages:
        if p["tag"] == "map":
            p["body"] = map_body
            break
    # element status list — grouped by content type (presentation mapping)
    CONTENT_GROUPS = [
        ("Document & head (metadata)", ["html", "head", "title", "base", "link", "meta", "style", "script", "noscript", "template"]),
        ("Page layout & structure", ["body", "div", "section", "article", "aside", "nav", "header", "footer", "main", "address", "figure", "figcaption"]),
        ("Paragraphs & text blocks", ["p", "pre", "blockquote", "hr", "br", "wbr"]),
        ("Headings", ["h1", "h2", "h3", "h4", "h5", "h6"]),
        ("Inline text & formatting", ["span", "b", "strong", "i", "em", "u", "s", "small", "mark", "cite", "q", "abbr", "data", "dfn", "time", "kbd", "samp", "code", "var", "sub", "sup", "ruby", "rt", "rp", "bdi", "bdo", "del", "ins"]),
        ("Disclosure & dialogs", ["details", "summary", "dialog"]),
        ("Lists", ["ul", "ol", "li", "dl", "dt", "dd", "menu"]),
        ("Links", ["a"]),
        ("Tables", ["table", "caption", "colgroup", "col", "thead", "tbody", "tfoot", "tr", "th", "td"]),
        ("Media & embedded content", ["img", "picture", "source", "video", "audio", "track", "canvas", "svg", "math", "iframe", "embed", "object", "param", "map", "area"]),
        ("Forms & inputs", ["form", "input", "button", "select", "option", "optgroup", "datalist", "textarea", "label", "fieldset", "legend", "output"]),
        ("Web components", ["slot"]),
        ("NOT USED — obsolete (never write these)", ["font", "center", "marquee", "big", "blink", "strike", "tt", "acronym", "frame", "frameset", "noframes", "applet", "basefont", "isindex", "nextid", "dir"]),
    ]
    E_BY_TAG = {e["t"]: e for e in ELEMS}
    listed = [t for _, tags in CONTENT_GROUPS for t in tags]
    assert sorted(listed) == sorted(E_BY_TAG), "content groups must cover every element exactly once"
    assert len(listed) == len(set(listed)), "no element in two groups"

    def el_row(e):
        st = e.get("st", "standard")
        label = "✔ used (standard)" if st == "standard" else "✘ NOT used — obsolete"
        cls = "" if st == "standard" else "st-obsolete"
        return (f"<tr><td><code class='tag'>&lt;{esc(e['t'])}&gt;</code></td><td>{esc(e['n'])}</td>"
                f"<td><span class=\"badge {cls}\">{label}</span></td></tr>")

    group_html = []
    for gname, tags in CONTENT_GROUPS:
        body_rows = "".join(el_row(E_BY_TAG[t]) for t in tags)
        hdr = f"<tr class='grp'><td colspan='3'>{esc(gname)} <span class='mut'>— {len(tags)} elements</span></td></tr>"
        group_html.append(hdr + body_rows)
    # split into 2 pages at a group boundary, near the middle
    total_rows = len(listed)
    acc, cut = 0, len(group_html)
    for gi, (_, tags) in enumerate(CONTENT_GROUPS):
        acc += len(tags)
        if acc >= total_rows / 2:
            cut = gi + 1
            break
    def group_table(chunk):
        return ('<table class="ref"><thead><tr><th>Tag</th><th>Name</th><th>Status</th></tr></thead>'
                f"<tbody>{chunk}</tbody></table>")
    intro = ("<p>Every element, grouped by what it is — paragraphs (<code class='tag'>&lt;p&gt;</code>, "
             "<code class='tag'>&lt;pre&gt;</code>…), lists, tables, forms, media. "
             "<b>✔ used</b> in modern HTML · <b>✘ NOT used</b> — obsolete, do not write it. "
             "Each element's full page (attributes, example, live result) is in Part I.</p>")
    list1 = f"<h2>All {len(listed)} HTML Elements — full list, grouped</h2>" + intro + group_table("".join(group_html[:cut]))
    list2 = "<h2>All HTML Elements — full list, grouped (continued)</h2>" + group_table("".join(group_html[cut:]))
    done = 0
    for p in pages:
        if p["tag"] == "list":
            p["body"] = list1 if done == 0 else list2
            done += 1
    return map_body

def main():
    pages = build_pages()
    # Order the book: front matter + Parts I–V first, then the Part VI practice
    # bank filling up to exactly 8000, and the Part VII appendix at the very end.
    front = [p for p in pages if p["part"] == FRONT]
    appendix = [p for p in pages if p["part"] == PART7]
    core = [p for p in pages if p["part"] not in (FRONT, PART7)]
    n_drills = TOTAL_PAGES - len(front) - len(core) - len(appendix) - 1
    print(f"curated pages: {len(front) + len(core)}, appendix: {len(appendix)}, drills needed: {n_drills}")
    assert n_drills > 0, "too many curated pages for 8000"
    # intro page for part VI, then the drills
    pages = front + core
    pages.append(dict(part=PART6, chap="Practice 1", title="Welcome to the Practice Bank", tag="chapter",
                      body=f"<h2>The 8000 Practice Pages</h2>"
                           "<p>This part is a <b>generated drill bank</b>: every page pairs a real HTML element "
                           "with a real CSS property — rendered element, starter code, your task, the solution, "
                           "and a mini value-quiz. Page numbers are deterministic (same number → same drill), "
                           "so you can track progress: e.g. 'finish one drill a day for 19 years' — or a page an hour for a month.</p>"
                           f"<p class='mut'>{n_drills} drills in this part. They are practice, not new reference material — the reference is Parts I–IV.</p>"))
    for i in range(n_drills):
        pages.append(dict(part=PART6, chap=f"Practice {i // 200 + 1}",
                          title=f"Drill {i + 1}", tag="drill", body=drill_body(i)))
    pages += appendix
    # re-check total
    assert len(pages) == TOTAL_PAGES, f"page count {len(pages)} != {TOTAL_PAGES}"
    finalize_gotos(pages)
    render_index(pages)
    os.makedirs(os.path.join(OUT, "volumes"), exist_ok=True)
    # index.html
    idx = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The 8000-Page HTML &amp; CSS Bible — Content Map</title>
<style>{STYLE}
.pg-foot{{position:static;margin:26px 0 0;padding:10px 0;border-top:1px solid var(--line)}}
</style>
</head>
<body>
<section class="page">
  <div class="pg-head"><span class="crumb">Content Map · Start here</span><span>8000 pages · 16 volumes</span></div>
  {render_index_front(pages)}
  <div class="pg-foot"><a href="volumes/vol-01.html">Open Volume 01 → (Page 1: Cover)</a>
  <span class="jump" style="margin-left:auto">Jump to page <input class="idx-jump" type="number" min="1" max="8000" placeholder="1–8000"></span></div>
</section>
<script>
(function(){{var b=document.querySelector('.idx-jump');if(b)b.addEventListener('keydown',function(e){{if(e.key!=='Enter')return;var n=parseInt(b.value,10);if(!n||n<1||n>8000)return;var v=Math.ceil(n/500);location.href='volumes/vol-'+String(v).padStart(2,'0')+'.html#p'+n;}});}})();
</script>
</body>
</html>
'''
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(idx)
    # volumes
    for v in range(1, VOLUMES + 1):
        chunk = list(enumerate(pages[(v - 1) * PER_VOLUME:v * PER_VOLUME], start=(v - 1) * PER_VOLUME + 1))
        html_doc = render_volume(v, chunk)
        with open(os.path.join(OUT, "volumes", f"vol-{v:02d}.html"), "w", encoding="utf-8") as f:
            f.write(html_doc)
        print(f"  vol-{v:02d}.html  {len(html_doc) / 1024:8.0f} KB")
    print("done.")

def render_index_front(pages):
    """The front content (cover-style) for index.html."""
    list_bodies = [p["body"] for p in pages if p["part"] == FRONT and p["tag"] == "list"]
    parts = {}
    for no, p in enumerate(pages, 1):
        parts.setdefault(p["part"], [no, no, 0])
        parts[p["part"]][1] = no
        parts[p["part"]][2] += 1
    part_links = "".join(
        f'<li><a href="volumes/vol-{(a - 1) // PER_VOLUME + 1:02d}.html#p{a}"><b>{esc(name)}</b></a> '
        f'<span class="mut">pages {a}–{b} · {n} pages</span></li>'
        for name, (a, b, n) in parts.items())
    vol_rows = []
    for v in range(1, VOLUMES + 1):
        first_no = (v - 1) * PER_VOLUME + 1
        fp = pages[first_no - 1]
        vol_rows.append(f'<tr><td><a href="volumes/vol-{v:02d}.html">vol-{v:02d}.html</a></td>'
                        f'<td>{first_no}–{first_no + PER_VOLUME - 1}</td><td>{esc(fp["part"])}</td><td>{esc(fp["chap"][:42])}</td></tr>')
    return f'''
<h2>The 8000-Page HTML &amp; CSS Bible</h2>
<p class="sum">Start here — the content map. 16 volumes × 500 pages. Every chapter, every element, every property,
with links to the exact page.</p>
<h3>Parts &amp; page ranges</h3><ul>{part_links}</ul>
<h3>Volumes</h3>
<table class="ref"><thead><tr><th>File</th><th>Pages</th><th>Part</th><th>Opens with</th></tr></thead>
<tbody>{''.join(vol_rows)}</tbody></table>
{''.join(list_bodies)}
<h3>How it works</h3>
<ul><li>Open any volume → ← / → flips pages → jump box goes to any of the 8000 pages.</li>
<li>Part I = every HTML element · Part II = every CSS property · Part III = components · Part IV = master tables.</li>
<li>Part V = study tools · Part VI = 7000+ generated practice drills · Part VII = appendix.</li></ul>
'''

if __name__ == "__main__":
    main()
