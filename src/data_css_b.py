# -*- coding: utf-8 -*-
# CSS properties — Part B: Typography, Color, Background, Effects, UI
from data_css_a import P, p  # noqa: F401  (extend the same list)

# ---------------- TYPOGRAPHY: FONT ----------------
p("font", "Typography",
  "Shorthand: font-style font-variant font-weight font-size/line-height font-family.",
  "The compact way to set all text in one line: font: 16px/1.5 Arial, sans-serif; (size + line-height together, family last). font: inherit / initial / unset also work.",
  [("style variant weight size/line-height family", "e.g. italic 700 14px/1.4 Georgia, serif.")],
  "body { font: 16px/1.6 system-ui, sans-serif; }",
  '<div style="font:italic 700 14px/1.4 Georgia,serif">font: italic 700 14px/1.4 Georgia — one line, whole look</div>',
  "normal normal 400 medium 1em auto", ["font-size", "font-family", "line-height"])

p("font-family", "Typography",
  "The typeface(s) to use, as a priority list.",
  "A comma-separated list from preferred to fallback: font-family: \"Segoe UI\", Tahoma, sans-serif;. Always end with a generic family (serif, sans-serif, monospace, cursive, fantasy, system-ui) so something always renders. Load custom fonts with @font-face first.",
  [("family list", "Named fonts (quote if they contain spaces), then a generic.")],
  "body { font-family: system-ui, -apple-system, \"Segoe UI\", Roboto, sans-serif; }",
  '<div style="font-size:13px;display:grid;gap:3px"><span style="font-family:Georgia,serif">Georgia (serif)</span><span style="font-family:Arial,sans-serif">Arial (sans-serif)</span><span style="font-family:\'Courier New\',monospace">Courier (monospace)</span></div>',
  "initial", ["font", "@font-face"])

p("font-size", "Typography", "The size of the text.",
  "px is absolute; em is relative to the parent; rem is relative to the ROOT element (the web-safe choice: 1rem = 16px default). Modern scale: body 1rem, h1 2rem, small 0.875rem. Also: % , ch (width of “0”), and clamp() for fluid type.",
  [("px", "Absolute pixels."),
   ("rem", "× the root font-size (default 16px) — recommended."),
   ("em", "× the parent font-size (nested multiplies!)."),
   ("%", "Of the parent size."),
   ("clamp(min, val, max)", "Fluid, e.g. clamp(1rem, 2vw + 1rem, 2rem).")],
  "h1 { font-size: 2rem; }\nbody { font-size: 1rem; }",
  '<div style="display:grid;gap:2px"><span style="font-size:24px">24px</span><span style="font-size:18px">18px</span><span style="font-size:14px">14px</span><span style="font-size:12px">12px</span></div>',
  "medium (16px)", ["font", "line-height"])

p("font-weight", "Typography", "The thickness of the text (100–900 or keywords).",
  "Numeric 100 (thin) → 900 (black); 400 = normal, 700 = bold. Keywords: normal, bold, bolder, lighter (relative to parent). Variable fonts accept any value in their range.",
  [("100–900", "Numeric weights."),
   ("normal / bold", "400 / 700."),
   ("bolder / lighter", "One step up/down from the parent.")],
  "h2 { font-weight: 700; }\nmeta { font-weight: 300; }",
  '<div style="font-size:14px;display:grid;gap:2px"><span style="font-weight:300">300 light</span><span style="font-weight:400">400 normal</span><span style="font-weight:600">600 semibold</span><span style="font-weight:800">800 extrabold</span></div>',
  "400", ["font"])

p("font-style", "Typography", "Italic, oblique, or upright.",
  "normal (default), italic (true italics if available), oblique (faux-slant when no italic face). Small-caps come from font-variant-caps.",
  [("normal", "Upright (default)."),
   ("italic", "Italic style."),
   ("oblique", "Slanted (auto angle)."),
   ("oblique 15deg", "Custom slant angle.")],
  "blockquote { font-style: italic; }",
  '<div style="font-size:14px"><span>normal</span> · <span style="font-style:italic">italic</span> · <span style="font-style:oblique 12deg">oblique 12°</span></div>',
  "normal", ["font-variant"])

p("font-variant", "Typography", "Compact switch for small caps and other variants.",
  "font-variant: small-caps; renders lowercase as small capitals. (The full legacy shorthand also covered weight/style/size — prefer the individual properties.)",
  [("normal", "Default."),
   ("small-caps", "Small capitals."),
   ("lining-nums / oldstyle-nums / tabular-nums", "Numeral styles.")],
  ".title { font-variant: small-caps; }",
  '<div style="font-size:15px"><span style="font-variant:small-caps">small caps variant</span></div>',
  "normal", ["font-variant-caps"])

p("font-variant-caps", "Typography", "Control the style of capital letters.",
  "normal, small-caps, all-small-caps, petite-caps, unicase, titling-caps — typographic refinements for headings and labels.",
  [("normal / small-caps / all-small-caps / petite-caps / unicase / titling-caps / none", "Caps styles.")],
  "h1 .kicker { font-variant-caps: all-small-caps; }",
  '<div style="font-size:15px"><span style="font-variant-caps:all-small-caps">All small caps, even the big letters</span></div>',
  "normal", ["font-variant"])

p("font-stretch", "Typography", "Width of the font (condensed / expanded).",
  "Applies to variable fonts and families with width variants: 75% condensed, 100% normal, 125% expanded.",
  [("percentage / keyword", "50%–200% or ultra-condensed…expanded.")],
  "@supports (font-stretch: 75%) { h1 { font-stretch: 75%; } }",
  '<div style="font-size:15px;font-family:Arial,sans-serif">font-stretch: 75% (condensed) — needs a condensed face</div>',
  "100%", ["font-weight"])

p("font-feature-settings", "Typography", "Turn OpenType features on/off (ligatures, tabular nums…).",
  "Low-level access to font features: font-feature-settings: \"liga\" 1, \"tnum\" 1; — ligatures on, tabular figures on (great for number columns). Newer individual properties (font-variant-numeric, font-kerning) are easier.",
  [("\"tag\" 0|1 …", "Feature tags: liga, dlig, tnum, onum, ss01…")],
  ".price { font-feature-settings: \"tnum\"; }",
  '<div style="font-size:14px;font-family:Georgia,serif">font-feature-settings: \"liga\" 1, \"tnum\" 1 → figures with tab <i>width</i></div>',
  "normal", ["font-variant-numeric"])

p("font-kerning", "Typography", "Enable/disable kerning between letter pairs.",
  "auto (default) lets the font kern (Av, To, etc. fit tightly); normal/none disable it.",
  [("auto", "Kerning per the font (default)."),
   ("normal / none", "Force on/off.")],
  "body { font-kerning: auto; }",
  '<div style="font-size:18px;font-family:Georgia,serif">Kerning: <span style="font-kerning:auto">VaToWa</span> vs <span style="font-kerning:none;letter-spacing:0">VaToWa</span></div>',
  "normal", ["font-feature-settings"])

p("font-optical-sizing", "Typography", "Use the font's optical sizes (automatically pick the right cut).",
  "auto (default) lets the browser choose the optical variant of the font (display vs text cut) based on size; off locks one cut.",
  [("auto", "Optical sizing on (default)."),
   ("off", "Single cut only.")],
  "h1 { font-optical-sizing: auto; }",
  '<div style="font-size:14px">font-optical-sizing: auto — the font picks its display/text cut per size.</div>',
  "auto", ["font-variation-settings"])

p("font-variation-settings", "Typography", "Direct access to variable-font axes (wght, wdth, ital, GRAD…).",
  "font-variation-settings: \"wght\" 620, \"wdth\" 90; — fine-grained control of variable fonts. (font-weight/size cover the common axes; this is the escape hatch.)",
  [("\"axis\" value …", "Axis tags: wght, wdth, opsz, GRAD…")],
  ".brand { font-variation-settings: \"wght\" 620, \"wght\" 620, \"GRAD\" 100; }",
  '<div style="font-size:15px">font-variation-settings: \"wght\" 620 — direct axis control on variable fonts.</div>',
  "normal", ["font-feature-settings"])

p("line-height", "Typography",
  "The height of each line box (vertical rhythm).",
  "Unitless numbers multiply the font-size (line-height: 1.6 = 160%) — the recommended form. Lengths fix the absolute line height. 1.5–1.75 for body text, 1.1–1.3 for headings.",
  [("number", "Multiplier of font-size (recommended)."),
   ("length / %", "Absolute line height."),
   ("normal", "Font-dependent (≈1.2).")],
  "p { line-height: 1.6; }\nh1 { line-height: 1.15; }",
  '<div style="font-size:14px"><p style="line-height:1.15;margin:0">line-height 1.15 — tight heading rhythm</p><p style="line-height:1.9;margin:8px 0 0;background:repeating-linear-gradient(transparent 0 10px, #e0f2fe 10px 11px)">line-height 1.9 — airy body rhythm</p></div>',
  "normal", ["font-size", "letter-spacing"])

# ---------------- TYPOGRAPHY: SPACING & ALIGNMENT ----------------
p("letter-spacing", "Typography", "Space between letters (tracking).",
  "Positive widens (uppercase kickers: letter-spacing: .08em), negative tightens (large display type). em units scale with the font size.",
  [("length", "e.g. 0.05em, -0.02em, 2px.")],
  ".kicker { letter-spacing: 0.1em; text-transform: uppercase; }",
  '<div style="font-size:14px"><span>normal</span><br><span style="letter-spacing:.15em">LETTER SPACING .15EM</span><br><span style="letter-spacing:-.03em;font-weight:800;font-size:20px">tight -0.03em display</span></div>',
  "normal", ["word-spacing"])

p("word-spacing", "Typography", "Extra space between words.",
  "Adds to the normal space between words (rarely needed; use letter-spacing for tracking).",
  [("length", "e.g. 2px, 0.2em.")],
  "p { word-spacing: 0.1em; }",
  '<div style="font-size:14px"><span>normal words</span><br><span style="word-spacing:.3em">word spacing 0.3em</span></div>',
  "normal", ["letter-spacing"])

p("text-align", "Typography", "Horizontal alignment of inline content in a block.",
  "left/right (or start/end — the logical, RTL-safe versions), center, justify. Inheritable — set it on the parent to align everything.",
  [("left / right", "Physical sides."),
   ("start / end", "Logical sides (flip with dir)."),
   ("center", "Centered."),
   ("justify", "Stretched lines (careful: can create rivers).")],
  "blockquote { text-align: center; }\n[dir=\"rtl\"] .menu { text-align: end; }",
  '<div style="font-size:12px;max-width:220px"><p style="text-align:left;border:1px solid #e5e7eb;padding:4px">text-align: left</p><p style="text-align:center;border:1px solid #e5e7eb;padding:4px">center</p><p style="text-align:justify;border:1px solid #e5e7eb;padding:4px">justify stretches every line edge to edge including the words inside this box.</p></div>',
  "start", ["text-indent", "text-align-last"])

p("text-align-last", "Typography", "Alignment of the last line (matters with justify).",
  "With text-align: justify the last line stays start-aligned — text-align-last: center/justify changes that. Mostly useful for centered headings on a justified block.",
  [("auto / left / right / center / justify / start / end", "Last-line alignment.")],
  "h1 { text-align: justify; text-align-last: center; }",
  '<div style="font-size:12px;max-width:200px"><p style="text-align:justify;text-align-last:center;border:1px solid #e5e7eb;padding:4px">justified body with the last line centered instead of jammed to the left edge.</p></div>',
  "auto", ["text-align"])

p("text-indent", "Typography", "Indent the first line of a block.",
  "text-indent: 2em; indents the first line (negative values pull it left). Classic book-style paragraphs.",
  [("length", "e.g. 2em, -1.5em.")],
  "p { text-indent: 2em; }",
  '<p style="font-size:13px;text-indent:2em;max-width:230px">The first line of every paragraph is indented by two ems, the traditional book layout style for continuous text.</p>',
  "0", ["text-align"])

p("text-transform", "Typography", "Change the case of the text (uppercase, lowercase, capitalize).",
  "Purely visual — the DOM text is unchanged (good for a11y). Uppercase micro-labels are a design staple; keep letter-spacing on them.",
  [("none", "As written (default)."),
   ("uppercase / lowercase", "All caps / all small."),
   ("capitalize", "First letter of each word.")],
  ".btn { text-transform: uppercase; letter-spacing: .06em; }",
  '<div style="font-size:13px"><span>mega book</span> → <span style="text-transform:uppercase">mega book</span> · <span style="text-transform:capitalize">mega book</span> · <span style="text-transform:lowercase">MEGA BOOK</span></div>',
  "none", ["letter-spacing"])

p("text-decoration", "Typography",
  "Shorthand: line + style + color for underlines/overlines/strikethroughs.",
  "text-decoration: underline dotted red; — also the classic link style: a { text-decoration: none; } then :hover { text-decoration: underline; }.",
  [("line style color", "line: none|underline|overline|line-through; style: solid|double|dotted|dashed|wavy; color: any color.")],
  "a { text-decoration: none; }\na:hover { text-decoration: underline; }",
  '<div style="font-size:14px"><span style="text-decoration:underline">underline</span> · <span style="text-decoration:overline">overline</span> · <span style="text-decoration:line-through">line-through</span> · <span style="text-decoration:underline wavy red">wavy underline</span></div>',
  "none", ["text-decoration-color", "text-underline-offset"])

p("text-decoration-color", "Typography", "Color of the text decoration line.",
  "Separate the underline color from the text: a:hover { text-decoration-color: #2563eb; }.",
  [("color", "Any color.")],
  "a { text-decoration-color: #93c5fd; }",
  '<div style="font-size:14px"><span style="text-decoration:underline;text-decoration-color:#f59e0b;text-underline-offset:4px">blue text, orange underline</span></div>',
  "currentcolor", ["text-decoration"])

p("text-decoration-thickness", "Typography", "Thickness of the decoration line.",
  "text-decoration-thickness: 2px; (or from/over the em value).",
  [("length", "e.g. 2px, 0.1em.")],
  "mark { text-decoration-thickness: .2em; }",
  '<div style="font-size:14px"><span style="text-decoration:underline;text-decoration-thickness:3px">3px underline</span></div>',
  "auto", ["text-decoration"])

p("text-underline-offset", "Typography", "Distance between the underline and the text.",
  "Keeps descenders (g, y) from touching the line: a { text-underline-offset: 3px; } — a subtle polish.",
  [("length", "e.g. 2px, 0.15em.")],
  "a { text-underline-offset: .15em; }",
  '<div style="font-size:15px"><span style="text-decoration:underline">default offset</span> · <span style="text-decoration:underline;text-underline-offset:6px">offset 6px</span></div>',
  "auto", ["text-decoration"])

p("text-shadow", "Typography", "One or more shadows behind the text.",
  "Same syntax as box-shadow: x y blur color [spread]. Subtle: 0 1px 2px rgba(0,0,0,.3) for text on photos. Stack multiple for 3D extrusion.",
  [("x y blur color", "e.g. 2px 2px 4px rgba(0,0,0,.4).")],
  "h1 { text-shadow: 0 2px 12px rgba(0,0,0,.45); }",
  '<div style="font-size:18px;font-weight:800"><span style="text-shadow:0 2px 6px rgba(0,0,0,.5)">soft shadow</span> · <span style="text-shadow:2px 2px 0 #fde047,4px 4px 0 #f59e0b">stacked 3D</span></div>',
  "none", ["box-shadow", "filter"])

p("text-overflow", "Typography", "What to show when text overflows a clipped box (ellipsis!).",
  "ellipsis shows … at the truncation point — the classic single-line truncation trio: white-space: nowrap; overflow: hidden; text-overflow: ellipsis;",
  [("clip", "Cut off (default)."),
   ("ellipsis", "Show … at the end.")],
  ".cell {\n  white-space: nowrap;\n  overflow: hidden;\n  text-overflow: ellipsis;\n}",
  '<div style="font-size:13px"><div style="width:170px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;border:1px solid #e5e7eb;padding:4px">A very long title that gets cut with an ellipsis here…</div></div>',
  "clip", ["overflow", "white-space", "display:-webkit-box"])

p("text-wrap", "Typography", "Modern line-breaking control (balance, pretty).",
  "balance (headings: even line lengths — gorgeous for titles), pretty (avoids orphans at the end of paragraphs), auto (default).",
  [("auto", "Default browser wrapping."),
   ("balance", "Even out the lines of a short block (headings)."),
   ("pretty", "Avoid a one-word last line in paragraphs.")],
  "h1 { text-wrap: balance; }\np { text-wrap: pretty; }",
  '<div style="font-size:13px;max-width:190px"><h3 style="text-wrap:balance;margin:0 0 6px">A title that wraps with balanced lines</h3><p style="text-wrap:pretty;margin:0">A paragraph where the last line is kept from being a single lonely word thanks to pretty wrapping.</p></div>',
  "auto", ["white-space", "overflow-wrap"])

p("vertical-align", "Typography", "Aligns inline content to the baseline (icons with text!).",
  "middle is the icon fix: .icon { vertical-align: middle; }. Values: baseline (default), sub/super, top/bottom, middle, and lengths (+.1em).",
  [("baseline", "Default — align to text baseline."),
   ("middle", "Center on the x-height (icon fix)."),
   ("top / bottom", "Top/bottom of the line box."),
   ("sub / super", "Subscript/superscript position."),
   ("length", "e.g. -.12em nudge.")],
  ".icon { vertical-align: middle; }",
  '<div style="font-size:14px"><span>Text with an <span style="vertical-align:middle;background:#e0e7ff;border:1px solid #a5b4fc;padding:1px 6px;font-size:11px">icon box</span> aligned middle, a <span style="vertical-align:super">super</span>, and a <span style="vertical-align:sub">sub</span>.</span></div>',
  "baseline", ["display", "line-height"])

p("white-space", "Typography", "How whitespace is handled: wrap, collapse, pre…",
  "normal: collapse spaces + wrap (default). nowrap: never wrap (table cells, badges). pre: keep everything (like <pre>). pre-wrap: keep spaces but wrap. pre-line: collapse spaces but keep line breaks. The single-line truncation uses nowrap.",
  [("normal", "Collapse + wrap (default)."),
   ("nowrap", "No wrapping (badges, full URLs)."),
   ("pre", "Keep all whitespace, no wrapping."),
   ("pre-wrap", "Keep whitespace, do wrap."),
   ("pre-line", "Collapse spaces, keep line breaks.")],
  ".badge { white-space: nowrap; }\npre { white-space: pre; }",
  '<div style="font-size:12px;max-width:230px"><span style="white-space:nowrap;background:#f3f4f6;padding:2px 6px;border:1px solid #e5e7eb">this badge never wraps no matter what</span><p style="white-space:pre-wrap;background:#f9fafb;border:1px solid #e5e7eb;padding:4px">    multiple   spaces   kept\nand line breaks kept</p></div>',
  "normal", ["overflow-wrap", "text-overflow"])

p("word-break", "Typography", "Where long words may break.",
  "normal: browser default. break-all: break anywhere (CJK text). keep-all: never break CJK. For Latin overflow, overflow-wrap: break-word is usually the right tool.",
  [("normal", "Default."),
   ("break-all", "Break inside words anywhere."),
   ("keep-all", "Keep CJK words intact.")],
  ".cjk { word-break: keep-all; }",
  '<div style="font-size:12px;width:120px;border:1px dashed #94a3b8;padding:6px;word-break:break-all">break-all splits supercalifragilisticexpialidocious anywhere it needs to</div>',
  "normal", ["overflow-wrap", "white-space"])

p("hyphens", "Typography", "Automatic hyphenation of long words.",
  "auto hyphenates at word boundaries (needs the element's lang for the right dictionary) — improves justified text. manual = break where a - is typed; none = off (default).",
  [("manual", "Only typed hyphens (default)."),
   ("none", "No hyphenation."),
   ("auto", "Browser hyphenates (needs lang).")],
  "p { hyphens: auto; }",
  '<p lang="en" style="font-size:13px;max-width:150px;text-align:justify;hyphens:auto;border:1px solid #e5e7eb;padding:6px">Hyphenation splits uncomfortably long words like antidisestablishmentarianism automatically.</p>',
  "manual", ["text-align", "lang"])

p("text-justify", "Typography", "Justification method (CJK mostly).",
  "inter-word (default): stretch spaces. inter-character: stretch character gaps (CJK). kibenzel: classic algorithm (legacy).",
  [("inter-word", "Stretch word spaces (default)."),
   ("inter-character", "Stretch character gaps."),
   ("kibenzel", "Legacy algorithm.")],
  ".cjk { text-justify: inter-character; }",
  '<div style="font-size:12px;max-width:190px;text-align:justify">text-justify: inter-word stretches the spaces between words in justified blocks like this one here.</div>',
  "auto", ["text-align"])

p("orphans", "Typography", "Minimum lines of a paragraph that must stay at the bottom of a page.",
  "Print/paged media: orphans: 3; keeps at least 3 lines together with the next page's content.",
  [("integer", "e.g. 2, 3.")],
  "@media print { p { orphans: 3; widows: 3; } }",
  '<div style="font-size:11px;color:#6b7280">orphans: 3 — at the page break, a paragraph always leaves ≥3 lines behind.</div>',
  "2", ["widows"])

p("widows", "Typography", "Minimum lines of a paragraph that must stay at the top of the next page.",
  "Print/paged media: widows: 3; avoids a 1-line orphan at the top of a page.",
  [("integer", "e.g. 2, 3.")],
  "@media print { p { widows: 3; } }",
  '<div style="font-size:11px;color:#6b7280">widows: 3 — a paragraph always carries ≥3 lines onto the next page.</div>',
  "2", ["orphans"])

p("tab-size", "Typography", "Width of a tab character in <pre>/monospace.",
  "tab-size: 4; makes \\t align to 4-character columns (editor parity).",
  [("integer", "e.g. 2, 4, 8.")],
  "pre { tab-size: 4; }",
  '<pre style="font-size:12px;tab-size:4;background:#0d1117;color:#e5e7eb;padding:8px;border-radius:6px;margin:0">a\tb\tc\naa\tb\tc</pre>',
  "8", ["font-family"])

# ---------------- DIRECTION & WRITING MODE ----------------
p("direction", "Typography", "Base text direction of the element (ltr / rtl).",
  "ltr (default) or rtl — sets the starting side for text and physical margins. Inheritable; the html lang usually implies it. For mixed content use dir/bdi instead of flipping direction.",
  [("ltr", "Left-to-right (default)."),
   ("rtl", "Right-to-left (Arabic, Hebrew).")],
  ".ar { direction: rtl; }",
  '<div style="direction:rtl;text-align:start;font-size:13px;border:1px solid #e5e7eb;padding:6px">العربية — starts from the right with direction:rtl</div>',
  "ltr", ["writing-mode"])

p("writing-mode", "Typography", "The flow direction of the text (horizontal, vertical, and which way).",
  "horizontal-tb (default): horizontal, top to bottom. vertical-rl: vertical, columns right→left (traditional CJK/Japanese). vertical-lr: vertical, left→right (Korean).",
  [("horizontal-tb", "Default horizontal."),
   ("vertical-rl", "Vertical, right-to-left columns."),
   ("vertical-lr", "Vertical, left-to-right columns.")],
  ".kanji { writing-mode: vertical-rl; }",
  '<div style="display:flex;gap:10px;align-items:flex-start;font-size:13px"><span>horizontal-tb (default)</span><span style="writing-mode:vertical-rl;max-height:90px;border:1px solid #e5e7eb;padding:2px 6px">vertical-rl CJK flow</span></div>',
  "horizontal-tb", ["direction"])

p("text-orientation", "Typography", "How text rotates inside a vertical writing mode.",
  "mixed (default): CJK stays upright, Latin rotates. upright: everything upright (great for Japanese UIs with Latin). sideways: rotate Latin 90°.",
  [("mixed", "CJK upright, Latin rotated (default)."),
   ("upright", "All characters upright."),
   ("sideways", "Rotate non-CJK 90°.")],
  ".jp { writing-mode: vertical-rl; text-orientation: upright; }",
  '<div style="font-size:13px;border:1px solid #e5e7eb;padding:4px;writing-mode:vertical-rl;text-orientation:upright;max-height:90px">text-orientation: upright — Latin stays readable</div>',
  "mixed", ["writing-mode"])

p("unicode-bidi", "Typography", "Control bidirectional text embedding (isolate/plane).",
  "isolate embeds a bidi context; plaintext treats content as a paragraph. For user-generated mixed-direction content, prefer the <bdi> element.",
  [("normal", "Default bidi algorithm."),
   ("embed / isolate", "Embed an isolated direction."),
   ("bidi-override", "Legacy force override."),
   ("plaintext", "Treat as a paragraph of plaintext.")],
  ".username { unicode-bidi: isolate; }",
  '<div style="font-size:13px">Normal: <span style="unicode-bidi:isolate;background:#fef9c3;padding:1px 4px">isolate mixed content</span> keeps layout stable.</div>',
  "normal", ["direction"])

# ---------------- COLOR & BACKGROUND ----------------
p("color", "Color",
  "The text color of an element (and its descendants).",
  "Any CSS color: #fff, rgb(255 0 0), hsl(0 100% 50%), oklch(), named (red), currentcolor, transparent. Inheritable — set it on the root for a theme. currentcolor lets other properties (borders, icons) follow the text color.",
  [("any color", "Hex, rgb(), hsl(), oklch(), keyword, var().")],
  ":root { color: #1f2937; }\na { color: #2563eb; }",
  '<div style="font-size:14px"><span style="color:#111827">slate-900</span> · <span style="color:#2563eb">blue-600</span> · <span style="color:#059669">emerald-600</span> · <span style="color:#dc2626">red-600</span></div>',
  "canvastext", ["background-color"])

p("background", "Background",
  "Shorthand: color + image + position + size + repeat + attachment + origin + clip.",
  "background: #f5f5f5 url(logo.png) center / cover no-repeat fixed;. Order is flexible except the first length pair = position, second = size (separated by /). The 9 longhands can each be overridden individually.",
  [("color image pos/size repeat attach origin/clip", "Any subset, any order (except the pos/size pair).")],
  ".hero { background: linear-gradient(135deg,#4285f4,#34a853) center / cover no-repeat; }",
  '<div style="background:linear-gradient(135deg,#6366f1,#ec4899) center/cover no-repeat;color:#fff;font-size:12px;padding:14px;border-radius:8px">background: linear-gradient(…) center / cover no-repeat</div>',
  "initial", ["background-color", "background-image"])

p("background-color", "Background", "The solid background color.",
  "Works with any alpha: rgba(0,0,0,.5) overlays, #00000080 hex+alpha, color-mix(). Set it before the image loads to avoid a white flash.",
  [("color", "Any color incl. alpha.")],
  ".card { background-color: #ffffff; }",
  '<div style="display:flex;gap:6px;font-size:11px"><span style="background-color:#eff6ff;color:#1e40af;padding:6px 10px">eff6ff</span><span style="background-color:#fef2f2;color:#991b1b;padding:6px 10px">fef2f2</span><span style="background-color:rgba(16,185,129,.15);color:#065f46;padding:6px 10px">rgba .15</span></div>',
  "transparent", ["background"])

p("background-image", "Background", "One or more background images (URLs, gradients, both).",
  "Comma-separated layers, first = topmost: background-image: url(pattern.png), linear-gradient(#0006, #0000);. Gradients are images too. (Gradients have their own pages in this book.)",
  [("url(...) / gradient / …", "Comma-separated layer list.")],
  ".page { background-image: url(dots.png), linear-gradient(#1118, #0000); }",
  '<div style="background-image:radial-gradient(#ffffff33 1px, transparent 1px),linear-gradient(135deg,#1e293b,#0f172a);background-size:12px 12px,cover;color:#cbd5e1;font-size:11px;padding:14px;border-radius:8px">two layers: dot pattern over a gradient</div>',
  "none", ["background", "background-size"])

p("background-position", "Background", "Where the background image sits.",
  "Keywords (top left, center, right bottom…), lengths (10px 20px), percentages (50% 50%), and edge offsets (top 10px left 20px). center / cover is the photo hero combo.",
  [("x y", "Keywords, lengths, or %: e.g. center, top right, 10px 20px, 50% 100%.")],
  ".hero { background-position: center; }",
  '<div style="display:flex;gap:6px;font-size:10px"><div style="width:52px;height:52px;background:linear-gradient(135deg,#f59e0b,#ef4444) center/cover;border-radius:6px;display:flex;align-items:center;justify-content:center;color:#fff">center</div><div style="width:52px;height:52px;background:linear-gradient(135deg,#10b981,#0ea5e9) top left/cover;border-radius:6px;display:flex;align-items:flex-start;justify-content:flex-start;color:#fff;padding:4px">top left</div><div style="width:52px;height:52px;background:linear-gradient(135deg,#8b5cf6,#ec4899) bottom right/cover;border-radius:6px;display:flex;align-items:flex-end;justify-content:flex-end;color:#fff;padding:4px">bottom right</div></div>',
  "0% 0%", ["background", "background-size"])

p("background-size", "Background", "How big the background image renders.",
  "auto: natural size. cover: fill the box (crop to keep ratio — the photo default). contain: fit the whole image (letterbox). Lengths: explicit w/h. %: relative to the box.",
  [("auto / cover / contain / length(s)", "e.g. cover, contain, 100% auto, 200px 100px.")],
  ".hero { background-size: cover; }",
  '<div style="display:flex;gap:6px;font-size:10px"><div style="width:64px;height:44px;background:linear-gradient(135deg,#0ea5e9,#6366f1) center/cover;border-radius:6px;display:flex;align-items:flex-end;justify-content:flex-end;color:#fff;padding:3px">cover</div><div style="width:64px;height:44px;background:linear-gradient(135deg,#0ea5e9,#6366f1) center/contain;border-radius:6px;display:flex;align-items:flex-end;justify-content:flex-end;color:#fff;padding:3px">contain</div></div>',
  "auto auto", ["background-position", "background-repeat"])

p("background-repeat", "Background", "Whether the image tiles (repeats).",
  "repeat (default, both axes), no-repeat, repeat-x, repeat-y, round (scale tiles to fit whole number), space (keep tile size, add gaps).",
  [("repeat / repeat-x / repeat-y / no-repeat / round / space", "Tiling behavior.")],
  ".page { background-repeat: no-repeat; }",
  '<div style="display:flex;gap:6px;font-size:10px"><div style="width:64px;height:44px;background:radial-gradient(circle at 8px 8px,#fde047 6px,transparent 7px);background-size:20px 20px;border:1px solid #e5e7eb;border-radius:6px;display:flex;align-items:flex-end;color:#92400e;padding:3px">repeat</div><div style="width:64px;height:44px;background:radial-gradient(circle at 8px 8px,#93c5fd 6px,transparent 7px);background-size:20px 20px;background-repeat:no-repeat;border:1px solid #e5e7eb;border-radius:6px;display:flex;align-items:flex-end;color:#1e40af;padding:3px">no-repeat</div><div style="width:64px;height:44px;background:radial-gradient(circle at 8px 8px,#86efac 6px,transparent 7px);background-size:20px 20px;background-repeat:round;border:1px solid #e5e7eb;border-radius:6px;display:flex;align-items:flex-end;color:#166534;padding:3px">round</div></div>',
  "repeat", ["background-image"])

p("background-attachment", "Background", "Scroll behavior of the background (fixed = parallax-ish).",
  "scroll (default): moves with the page. fixed: stays put while content scrolls (parallax effect; can jank on mobile — test it). local: scrolls with the element's content.",
  [("scroll", "Default — scrolls with the document."),
   ("fixed", "Fixed to the viewport (parallax)."),
   ("local", "Scrolls with the element content.")],
  ".hero { background-attachment: fixed; }",
  '<div style="font-size:11px;background:#f1f5f9;border:1px solid #e2e8f0;padding:8px;border-radius:6px">background-attachment: fixed → the image stays put while the text scrolls over it.</div>',
  "scroll", ["background"])

p("background-origin", "Background", "Where the background starts measuring from (border-box / padding-box / content-box).",
  "With border + padding, origin decides whether the image starts at the border edge, the padding edge, or the content edge.",
  [("border-box / padding-box / content-box", "The origin rectangle.")],
  ".boxed { background-origin: content-box; }",
  '<div style="font-size:10px"><div style="border:6px solid #f59e0b;padding:8px;background:linear-gradient(90deg,#fde68a,#f59e0b) content-box/no-repeat;width:140px">origin: content-box (starts inside the padding)</div><div style="border:6px solid #f59e0b;padding:8px;background:linear-gradient(90deg,#fde68a,#f59e0b) border-box/no-repeat;width:140px;margin-top:6px">origin: border-box (starts at the border)</div></div>',
  "padding-box", ["background-clip"])

p("background-clip", "Background", "How far the background is painted (border-box / padding-box / content-box / text).",
  "text is the magic value: the background (usually a gradient) is clipped to the letterforms → gradient text: -webkit-background-clip: text; color: transparent;",
  [("border-box / padding-box / content-box / text", "The clipping rectangle (text = letterforms).")],
  ".gradient-text {\n  background: linear-gradient(90deg,#2563eb,#9333ea);\n  -webkit-background-clip: text;\n  background-clip: text;\n  color: transparent;\n}",
  '<div style="font-size:20px;font-weight:800;background:linear-gradient(90deg,#2563eb,#9333ea,#ec4899);-webkit-background-clip:text;background-clip:text;color:transparent">gradient text via clip</div>',
  "border-box", ["background-origin"])

p("opacity", "Color",
  "The overall transparency of the element (0–1).",
  "Affects the whole element including children (unlike rgba which is per-pixel). 0.5 = half visible. Common: disabled buttons opacity:.5, hover states opacity:1, ghost overlays opacity:.85.",
  [("number 0–1", "e.g. 0.5, 1.")],
  ".muted { opacity: 0.5; }",
  '<div style="display:flex;gap:8px;font-size:12px;align-items:center"><span style="background:#3b82f6;color:#fff;padding:6px 10px;border-radius:6px">opacity 1</span><span style="background:#3b82f6;color:#fff;padding:6px 10px;border-radius:6px;opacity:.7">.7</span><span style="background:#3b82f6;color:#fff;padding:6px 10px;border-radius:6px;opacity:.4">.4</span><span style="background:#3b82f6;color:#fff;padding:6px 10px;border-radius:6px;opacity:.15">.15</span></div>',
  "1", ["visibility", "background-color"])

p("caret-color", "UI", "The color of the text-input caret (cursor).",
  "caret-color: #2563eb; matches the caret to your brand. (The blinking I-beam in inputs.)",
  [("color / auto", "Any color or auto (default = text color).")],
  "input { caret-color: #2563eb; }",
  '<input placeholder="type here — caret is blue" style="border:1px solid #d1d5db;border-radius:6px;padding:6px 10px;font-size:12px;caret-color:#2563eb;width:200px">',
  "auto", ["color"])

p("accent-color", "UI", "The accent color of form controls (checkboxes, radios, ranges, progress).",
  "One line themes every form control: accent-color: #2563eb; — the modern alternative to styling each input by hand.",
  [("color / auto", "Any color.")],
  ":root { accent-color: #2563eb; }",
  '<div style="font-size:12px;display:flex;gap:14px;align-items:center;accent-color:#059669"><label><input type="checkbox" checked> checkbox</label><label><input type="radio" checked> radio</label><input type="range" value="60" style="width:110px"></div>',
  "auto", ["color-scheme"])

p("color-scheme", "UI", "Declare light/dark support (form controls, scrollbars, canvas default bg).",
  "color-scheme: dark light; tells the browser the page supports both — native form controls and the canvas pick the right palette. Pairs with @media (prefers-color-scheme: dark).",
  [("normal / only / light / dark / <custom>", "e.g. dark light, only dark.")],
  ":root { color-scheme: light dark; }",
  '<div style="font-size:12px;display:flex;gap:10px;align-items:center;color-scheme:light"><select style="border:1px solid #d1d5db;border-radius:6px;padding:4px 8px"><option>light scheme select</option></select><input type="date" style="border:1px solid #d1d5db;border-radius:6px;padding:4px 8px"></div>',
  "normal", ["prefers-color-scheme"])

p("forced-color-adjust", "UI", "Whether the OS 'forced colors' mode (Windows High Contrast) overrides colors.",
  "auto (default): the OS may replace your colors in forced-color mode. none: keep them (for charts/logos where color is meaning).",
  [("auto / none", "Auto respects the OS setting.")],
  ".logo { forced-color-adjust: none; }",
  '<div style="font-size:11px;background:#f1f5f9;padding:8px;border-radius:6px">forced-color-adjust: none → the element keeps its colors even in Windows High Contrast mode.</div>',
  "auto", ["color-scheme"])

p("print-color-adjust", "UI", "Keep background colors when printing (-webkit-print-color-adjust).",
  "Printers strip backgrounds by default; print-color-adjust: exact; (with -webkit-) keeps your colored UI in the PDF.",
  [("economy / economy-ink / accurate / exact", "exact keeps colors.")],
  "@media print { * { print-color-adjust: exact; -webkit-print-color-adjust: exact; } }",
  '<div style="font-size:11px;background:#dbeafe;color:#1e3a8a;padding:8px;border-radius:6px">print-color-adjust: exact → this background survives printing.</div>',
  "auto", ["color-scheme"])

# ---------------- EFFECTS: FILTER, MASK, CLIP, BLEND ----------------
p("filter", "Effects",
  "Real-time image effects on the element (blur, brightness, grayscale…).",
  "Functions chain: filter: blur(2px) brightness(1.1) saturate(1.4) drop-shadow(0 4px 8px #0006). Affects rendering only, not layout. Also a performance hint — browsers GPU-composite filtered elements.",
  [("function list", "blur(px) brightness(n) contrast(n) grayscale(n) hue-rotate(deg) invert(n) opacity(n) saturate(n) sepia(n) drop-shadow(x y blur color) url(#svg)."),
   ("none", "Default.")],
  ".photo { filter: saturate(1.2) contrast(1.05); }\n.blurred { filter: blur(8px); }",
  '<div style="display:flex;gap:8px;font-size:10px"><span style="width:64px;height:44px;border-radius:6px;background:linear-gradient(135deg,#f59e0b,#ef4444,#8b5cf6)"></span><span style="width:64px;height:44px;border-radius:6px;background:linear-gradient(135deg,#f59e0b,#ef4444,#8b5cf6);filter:grayscale(1)"></span><span style="width:64px;height:44px;border-radius:6px;background:linear-gradient(135deg,#f59e0b,#ef4444,#8b5cf6);filter:blur(3px)"></span><span style="width:64px;height:44px;border-radius:6px;background:linear-gradient(135deg,#f59e0b,#ef4444,#8b5cf6);filter:invert(1)"></span></div>',
  "none", ["backdrop-filter", "transform"])

p("backdrop-filter", "Effects",
  "Filters what is BEHIND the element (glassmorphism!).",
  "The frosted-glass effect: a semi-transparent background + backdrop-filter: blur(12px) saturate(1.4). Needs a semi-transparent background to see through to. Prefix: -webkit- for Safari.",
  [("function list", "Same functions as filter, applied to the backdrop."),
   ("none", "Default.")],
  ".glass {\n  background: rgba(255,255,255,.35);\n  backdrop-filter: blur(12px) saturate(1.4);\n  border: 1px solid rgba(255,255,255,.4);\n}",
  '<div style="position:relative;font-size:11px"><div style="position:absolute;inset:0;background:repeating-linear-gradient(45deg,#f59e0b 0 14px,#3b82f6 14px 28px,#10b981 28px 42px)"></div><div style="position:relative;margin:16px auto;width:150px;background:rgba(255,255,255,.4);backdrop-filter:blur(6px) saturate(1.5);-webkit-backdrop-filter:blur(6px) saturate(1.5);border:1px solid rgba(255,255,255,.6);border-radius:10px;padding:10px;text-align:center;font-weight:700">glass panel</div></div>',
  "none", ["filter", "mix-blend-mode"])

p("mix-blend-mode", "Effects", "How the element's pixels blend with what's behind it.",
  "multiply (darken, multiply layers), screen (lighten), overlay, difference, exclusion, hue, color… — Photoshop-like blending, in CSS. Great for duotone images and overlay effects.",
  [("normal / multiply / screen / overlay / darken / lighten / color-dodge / color-burn / hard-light / soft-light / difference / exclusion / hue / saturation / color / luminosity", "Blend modes.")],
  ".logo-duotone { mix-blend-mode: multiply; }",
  '<div style="display:flex;gap:10px;font-size:10px"><div style="width:70px;height:50px;background:linear-gradient(135deg,#60a5fa,#f472b6);border-radius:6px;position:relative"><span style="position:absolute;inset:10px;background:#1d4ed8;border-radius:4px;mix-blend-mode:multiply"></span></div><div style="width:70px;height:50px;background:linear-gradient(135deg,#60a5fa,#f472b6);border-radius:6px;position:relative"><span style="position:absolute;inset:10px;background:#1d4ed8;border-radius:4px;mix-blend-mode:screen"></span></div><div style="width:70px;height:50px;background:linear-gradient(135deg,#60a5fa,#f472b6);border-radius:6px;position:relative"><span style="position:absolute;inset:10px;background:#1d4ed8;border-radius:4px;mix-blend-mode:difference"></span></div></div>',
  "normal", ["filter", "isolation"])

p("isolation", "Effects", "Isolate the element from blend modes above/below it.",
  "isolation: isolate; makes the element a stacking+grouping context so mix-blend-mode children can't blend with the page background — group your effect layers.",
  [("auto", "Blend with the context (default)."),
   ("isolate", "Isolate blending.")],
  ".scene { isolation: isolate; }",
  '<div style="font-size:11px;background:#f1f5f9;padding:8px;border-radius:6px">isolation:isolate → child blend modes only mix inside this element.</div>',
  "auto", ["mix-blend-mode"])

p("mask-image", "Effects", "Clip the element with an image/gradient mask (alpha channel).",
  "mask-image: linear-gradient(to right, #000 60%, transparent); fades the element out to the right. Combine with mask-size/position/repeat. Prefix: -webkit-mask-image in Safari/Firefox.",
  [("image / gradient", "Luminance/alpha mask source.")],
  ".fade {\n  -webkit-mask-image: linear-gradient(to right, #000 55%, transparent);\n  mask-image: linear-gradient(to right, #000 55%, transparent);\n}",
  '<div style="font-size:12px;max-width:230px;background:linear-gradient(90deg,#3b82f6,#8b5cf6);color:#fff;padding:10px;-webkit-mask-image:linear-gradient(to right,#000 45%,transparent);mask-image:linear-gradient(to right,#000 45%,transparent)">mask-image fades this gradient text block out to the right side of the box</div>',
  "none", ["mask-position", "clip-path"])

p("mask", "Effects", "Shorthand: mask-image + mode + position + size + repeat + origin + clip.",
  "mask: linear-gradient(…) center / cover no-repeat; — the one-liner version of the mask longhands.",
  [("image mode pos/size repeat", "Full mask shorthand.")],
  "mask: radial-gradient(circle at 30% 30%, #000 40%, transparent 70%);",
  '<div style="font-size:12px;width:120px;height:60px;background:repeating-linear-gradient(45deg,#0ea5e9 0 10px,#6366f1 10px 20px);mask:radial-gradient(circle at 30% 40%,#000 30%,transparent 70%);-webkit-mask:radial-gradient(circle at 30% 40%,#000 30%,transparent 70%)"></div>',
  "none", ["mask-image"])

p("clip-path", "Effects",
  "Clip the element to a shape or path (non-rectangular boxes!).",
  "Shapes: circle(50% at 50% 50%), ellipse(), polygon(0 0, 100% 0, 100% 100%), inset(10px round 8px). Paths: path(\"M…\") for arbitrary SVG paths. The rounded-avatar and hero-shape workhorse. Animatable (transition clip-path).",
  [("basic shape", "circle(r at x y), ellipse(rx ry at x y), polygon(x y, …), inset(t r b l round r)."),
   ("path(…)", "SVG path data."),
   ("url(#id)", "An <clipPath> element.")],
  ".avatar { clip-path: circle(50%); }\n.shape { clip-path: polygon(0 0, 100% 0, 100% 85%, 50% 100%, 0 85%); }",
  '<div style="display:flex;gap:10px;font-size:10px;align-items:center"><span style="width:56px;height:56px;background:linear-gradient(135deg,#f472b6,#8b5cf6);clip-path:circle(50%)"></span><span style="width:56px;height:56px;background:linear-gradient(135deg,#0ea5e9,#10b981);clip-path:polygon(50% 0,100% 38%,81% 100%,19% 100%,0 38%)"></span><span style="width:56px;height:56px;background:linear-gradient(135deg,#f59e0b,#ef4444);clip-path:inset(8px round 14px)"></span><span style="width:70px;height:56px;background:linear-gradient(135deg,#6366f1,#ec4899);clip-path:polygon(0 0,100% 0,100% 100%,0 100%,12% 50%)"></span></div>',
  "none", ["mask-image", "border-radius"])

p("shape-outside", "Layout", "Float content around a non-rectangular shape.",
  "With float, text wraps the shape: shape-outside: circle(50%); or url(image.png) (alpha wrap) or polygon(). Magazine layout power.",
  [("shape / url(image)", "circle/ellipse/polygon/inset or an image alpha channel.")],
  ".logo-float { float: left; shape-outside: circle(50%); }",
  '<div style="font-size:11px;line-height:1.5;width:230px"><span style="float:left;width:80px;height:80px;background:radial-gradient(circle at 35% 35%,#fde047,#f59e0b);shape-outside:circle(50%);margin:0 10px 6px 0"></span>Text wraps around the circular shape, following its curve — the float + shape-outside combo for editorial layouts.</div>',
  "none", ["float"])

p("shape-margin", "Layout", "Extra clearance around a shape-outside shape.",
  "shape-margin: 8px; adds a breathing gap between the wrapped text and the shape.",
  [("length", "e.g. 8px.")],
  ".logo-float { shape-margin: 8px; }",
  '<div style="font-size:10px;background:#f8fafc;border:1px solid #e2e8f0;padding:8px">shape-margin: 8px → 8px of air between text and shape.</div>',
  "0", ["shape-outside"])

# ---------------- LIST STYLES ----------------
p("list-style", "Typography", "Shorthand: list-style-type + position + image.",
  "list-style: none; kills bullets (the menu reset). list-style: square inside; custom look. None + your own ::marker gives full control.",
  [("type position image", "e.g. circle outside, none, url(bullet.svg) outside.")],
  "ul { list-style: none; padding: 0; }",
  '<div style="font-size:12px"><ul style="list-style:square;padding-left:20px;margin:0"><li>square item</li></ul><ul style="list-style:none;padding:0;margin:4px 0 0"><li style="padding-left:18px;position:relative"><span style="position:absolute;left:0">•</span>custom bullet (list-style:none)</li></ul></div>',
  "initial", ["list-style-type", "list-style-position"])

p("list-style-type", "Typography", "The bullet/number marker style.",
  "disc (default round), circle, square; for ordered: decimal, decimal-leading-zero, lower-roman, upper-alpha, armenian, georgian… and none to remove.",
  [("disc / circle / square / decimal / lower-roman / upper-alpha / … / none", "Marker style keywords.")],
  "ul { list-style-type: square; }\nol { list-style-type: lower-roman; }",
  '<div style="font-size:12px;display:flex;gap:20px"><ul style="list-style-type:disc;padding-left:18px;margin:0"><li>disc</li><li>disc</li></ul><ul style="list-style-type:circle;padding-left:18px;margin:0"><li>circle</li><li>circle</li></ul><ul style="list-style-type:square;padding-left:18px;margin:0"><li>square</li><li>square</li></ul><ol style="list-style-type:lower-roman;padding-left:18px;margin:0"><li>lower-roman</li></ol></div>',
  "disc", ["list-style", "list-style-position"])

p("list-style-position", "Typography", "Where the marker sits: inside or outside the box.",
  "outside (default): marker hangs in the padding (background doesn't reach it). inside: marker is part of the content box (background covers it, text wraps below).",
  [("outside", "Default — marker in the margin/padding area."),
   ("inside", "Marker inside the content box.")],
  "li { list-style-position: inside; background: #f3f4f6; }",
  '<div style="font-size:12px"><ul style="padding-left:18px"><li style="background:#e0e7ff;padding:2px 4px">outside: background stops before the bullet</li></ul><ul style="padding-left:18px;margin-top:6px"><li style="list-style-position:inside;background:#dcfce7;padding:2px 4px">inside: background covers the whole row</li></ul></div>',
  "outside", ["list-style"])

p("list-style-image", "Typography", "Use an image (URL/SVG/data URI) as the list marker.",
  "list-style-image: url(icon.svg); — custom bullets without pseudo-elements.",
  [("url()", "Image URL or data URI.")],
  "ul.tasks li { list-style-image: url(check.svg); }",
  '<div style="font-size:12px"><ul style="padding-left:4px;margin:0"><li style="padding-left:20px;position:relative">custom bullet via list-style-image (an SVG here)</li></ul></div>',
  "none", ["list-style"])

p("counter-reset", "Generated Content", "Reset a CSS counter to a value.",
  "counter-reset: chapter 3; starts your custom numbering (often used with ::before and content: counter(chapter) \".\").",
  [("name value", "e.g. chapter 0, step 1.")],
  "article { counter-reset: chapter; }\narticle h2::before { counter-increment: chapter; content: counter(chapter) \". \"; }",
  '<div style="font-size:12px;color:#4b5563">counter-reset + counter-increment + content: counter() = custom numbering without <ol>.</div>',
  "none", ["counter-increment", "content"])

p("counter-increment", "Generated Content", "Increment a CSS counter.",
  "counter-increment: chapter; (or +2). Each matched element bumps the counter for content: counter(chapter).",
  [("name step", "e.g. chapter, step 2.")],
  "li::before { counter-increment: item; content: counter(item) \". \"; }",
  '<div style="font-size:12px;color:#4b5563">counter-increment: item → each li adds 1 to “item”.</div>',
  "none", ["counter-reset", "content"])

p("content", "Generated Content", "Insert generated text/images into ::before/::after (or replace content in replaced elements).",
  "The pseudo-element engine: content: counter(step) \". \";, content: \"→\";, content: url(arrow.svg);, content: attr(data-title);. content: none is the default. In @property-land, content can even be quoted strings and CSS variables.",
  [("none", "Nothing (default)."),
   ("string", "content: \"Page \"."),
   ("counter()/counters()/attr()", "Dynamic values: counter(n), attr(data-x)."),
   ("url()", "Generated image."),
   ("open-quote / close-quote", "Smart quotes from quotes property.")],
  "li::marker { content: \"\\2713 \"; }\n.step::before { content: counter(step) \". \"; counter-increment: step; }",
  '<div style="font-size:12px"><span data-tip="hover me" style="border-bottom:1px dotted #6b7280;position:relative">attr(data-tip) via content</span><ol style="padding-left:18px;margin:4px 0 0;list-style:none"><li style="padding-left:24px;position:relative">item with counter content</li></ol></div>',
  "normal", ["counter-increment", "quotes"])

p("quotes", "Generated Content", "Define the quotation marks used by open-quote/close-quote.",
  "quotes: \"\\201C\" \"\\201D\" \"\\2018\" \"\\2019\"; → curly double, then single for nested quotes.",
  [("open close pairs", "Escaped characters or strings.")],
  "blockquote { quotes: \"“\" \"”\"; }\nblockquote p::before { content: open-quote; }",
  '<div style="font-size:12px;font-style:italic">“smart quotes via the quotes property (open-quote / close-quote)”</div>',
  "none", ["content"])

p("initial-letter", "Generated Content", "Enlarge the first letter (drop cap).",
  "initial-letter: 4; (WebKit: -webkit-initial-letter) + initial-letter-align: alphabetic; creates a drop cap spanning 4 lines.",
  [("number", "Number of lines to span.")],
  "p:first-of-type::first-letter { initial-letter: 3; }",
  '<p style="font-size:13px;max-width:200px;margin:0"><span style="float:left;font-size:3.2em;line-height:.85;font-weight:800;color:#2563eb;margin-right:6px;font-family:Georgia,serif">D</span>rop caps span several lines with initial-letter (and ::first-letter in practice).</p>',
  "none", ["content"])

# ---------------- CURSOR & UI BEHAVIOR ----------------
p("cursor", "UI", "The mouse cursor over the element.",
  "pointer (links/buttons), default, text (inputs), move, grab/grabbing (draggable), wait, progress, crosshair, not-allowed, help, and url() for custom SVG cursors.",
  [("keyword", "auto|default|pointer|text|wait|progress|help|move|not-allowed|crosshair|grab|grabbing|cell|col-resize|row-resize|n-resize…|zoom-in|zoom-out|alias|copy|none|all-scroll"),
   ("url(…) fallback", "Custom cursor image.")],
  "a, button { cursor: pointer; }\n.drag { cursor: grab; } .drag:active { cursor: grabbing; }",
  '<div style="font-size:11px;display:flex;gap:8px;flex-wrap:wrap"><span style="padding:6px 10px;border:1px solid #d1d5db;border-radius:6px;cursor:pointer">pointer</span><span style="padding:6px 10px;border:1px solid #d1d5db;border-radius:6px;cursor:text">text</span><span style="padding:6px 10px;border:1px solid #d1d5db;border-radius:6px;cursor:grab">grab</span><span style="padding:6px 10px;border:1px solid #d1d5db;border-radius:6px;cursor:move">move</span><span style="padding:6px 10px;border:1px solid #d1d5db;border-radius:6px;cursor:not-allowed">not-allowed</span></div>',
  "auto", ["user-select", "pointer-events"])

p("user-select", "UI", "Whether the text can be selected by the user.",
  "none: unselectable (drag handles, card labels — mind a11y). auto/text: selectable. all: clicking selects the whole element (great for copyable IDs).",
  [("auto", "Browser default."),
   ("none", "Selection disabled."),
   ("text", "Selectable."),
   ("all", "One click selects everything inside.")],
  ".drag-handle { user-select: none; }\n.id { user-select: all; }",
  '<div style="font-size:12px"><span style="user-select:none;background:#f3f4f6;padding:6px 10px;border-radius:6px">user-select: none — try to select me (can\'t)</span> <code style="user-select:all;background:#eef2ff;padding:2px 6px">select-all-id</code></div>',
  "auto", ["cursor"])

p("resize", "UI", "Allow the user to resize the element (with overflow ≠ visible).",
  "resize: both; shows a corner grip (needs overflow: auto/hidden/scroll). vertical/horizontal limit the axis.",
  [("none", "Default."),
   ("both / horizontal / vertical", "Allowed resize directions.")],
  ".console { resize: vertical; overflow: auto; }",
  '<div style="resize:both;overflow:auto;border:1px dashed #6366f1;background:#eef2ff;padding:8px;font-size:11px;min-width:120px;max-width:220px">resize: both — drag the bottom-right grip</div>',
  "none", ["overflow"])

p("pointer-events", "UI", "Whether the element can be the target of mouse/pointer events.",
  "none: clicks pass through (invisible to the pointer — great for decorative overlays, SVG hit areas). auto: default.",
  [("auto", "Default — normal hit testing."),
   ("none", "Element never receives pointer events; children don't either."),
   ("visiblePainted / visibleFill / …", "SVG-specific variants.")],
  ".overlay::after { pointer-events: none; }",
  '<div style="font-size:11px;position:relative"><a href="#" style="color:#2563eb">link</a><div style="position:absolute;inset:0;background:rgba(239,68,68,.15);pointer-events:none;border-radius:6px"></div>the red overlay ignores the pointer (pointer-events: none).</div>',
  "auto", ["cursor"])

p("touch-action", "UI", "What gestures the browser handles (scroll/zoom) vs the app.",
  "manipulation: kill the 300ms double-tap delay + page zoom on tap (buttons). none: you own all gestures (canvas games, sliders). pan-x/pan-y: allow only that scroll direction.",
  [("auto", "Default browser behavior."),
   ("none", "Browser handles no touch gestures."),
   ("pan-x / pan-y", "Only that scroll direction."),
   ("pinch-zoom / manipulation", "Allow zoom / only manipulate.")],
  "button { touch-action: manipulation; }",
  '<div style="font-size:11px;background:#f1f5f9;padding:8px;border-radius:6px">touch-action: manipulation → no double-tap-zoom delay on this element (snappier taps on mobile).</div>',
  "auto", ["cursor"])

p("scroll-behavior", "UI", "Smooth or instant scrolling for the element (and anchor jumps).",
  "html { scroll-behavior: smooth; } → in-page #anchor jumps animate. Pairs with scroll-margin-top so sticky headers don't cover targets.",
  [("auto", "Instant (default)."),
   ("smooth", "Animated scroll.")],
  "html { scroll-behavior: smooth; }\n@media (prefers-reduced-motion) { html { scroll-behavior: auto; } }",
  '<div style="font-size:11px;background:#f0fdf4;border:1px solid #86efac;padding:8px;border-radius:6px">scroll-behavior: smooth — clicking #section glides instead of jumping.</div>',
  "auto", ["scroll-margin-top"])

p("scroll-margin-top", "UI", "Offset for scroll snapping & anchor scrolling (sticky-header fix).",
  "When you scroll to #section, stop this many px early — so a sticky header (e.g. 64px) doesn't cover the target.",
  [("length", "e.g. 80px.")],
  "section { scroll-margin-top: 80px; }",
  '<div style="font-size:11px;background:#fefce8;border:1px solid #fde047;padding:8px;border-radius:6px">scroll-margin-top: 80px → anchor jumps stop 80px before the element (below the sticky header).</div>',
  "0", ["scroll-behavior"])

p("scroll-padding-top", "UI", "Padding inside a scroll/snap container (align snapped items under headers).",
  "On the scroll container: snap points are offset from the padding box edge — keeps snapped slides clear of a fixed toolbar.",
  [("length", "e.g. 72px.")],
  ".snap { scroll-padding-top: 72px; }",
  '<div style="font-size:11px;background:#eff6ff;border:1px solid #93c5fd;padding:8px;border-radius:6px">scroll-padding-top: 72px → snapped items stop 72px inside the container edge.</div>',
  "0", ["scroll-snap-align"])

p("scroll-snap-type", "UI", "Enable scroll snapping on a container (x, y, both).",
  "mandatory: always land on a snap point. proximity: snap only when close. scroll-snap-type: y mandatory; + child scroll-snap-align: start = a slide/carousel with zero JS.",
  [("none", "Off (default)."),
   ("x | y | both", "Snap axis."),
   ("mandatory / proximity", "Strictness.")],
  ".carousel { overflow-x: auto; scroll-snap-type: x mandatory; }\n.slide { scroll-snap-align: start; }",
  '<div style="font-size:10px"><div style="display:flex;gap:6px;overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:4px"><div style="scroll-snap-align:start;min-width:90px;height:40px;background:#a5f3fc;border:1px solid #67e8f9"></div><div style="scroll-snap-align:start;min-width:90px;height:40px;background:#67e8f9"></div><div style="scroll-snap-align:start;min-width:90px;height:40px;background:#22d3ee"></div></div>scroll-snap-type: x mandatory — scroll snaps to slides</div>',
  "none", ["scroll-snap-align", "scroll-snap-stop"])

p("scroll-snap-align", "UI", "Where the child snaps inside the container (start/center/end).",
  "start: child's start edge aligns to the container's snap edge (the carousel default). center: the child centers.",
  [("none / start / end / center", "Snap position; or two values: inline, block.")],
  ".slide { scroll-snap-align: start; }",
  '<div style="font-size:10px;background:#f0fdf4;border:1px solid #86efac;padding:6px;border-radius:4px;display:inline-block">scroll-snap-align: start → this child\'s start edge snaps to the container edge.</div>',
  "none", ["scroll-snap-type"])

p("scroll-snap-stop", "UI", "Whether the scroller must stop at every snap point (normal) or can skip (always).",
  "always: fling can't skip a snap point (good for onboarding carousels). normal (default): can skip.",
  [("normal", "Can skip points."),
   ("always", "Must stop at each point.")],
  ".slide { scroll-snap-stop: always; }",
  '<div style="font-size:10px;background:#fdf4ff;border:1px solid #e9d5ff;padding:6px;border-radius:4px;display:inline-block">scroll-snap-stop: always → every fling lands on each slide.</div>',
  "normal", ["scroll-snap-align"])

p("overscroll-behavior", "UI", "What happens when you scroll past the edges (bounce/chain control).",
  "none: stop at the edge (no rubber-band, no scroll chaining — apps, carousels). contain: no chaining to the parent. auto: default. Fixes the annoying full-page scroll when dragging a horizontal list.",
  [("auto", "Default chaining/bounce."),
   ("contain", "No chaining to parent."),
   ("none", "No bounce, no chaining."),
   ("x / y / both + value", "Per-axis: e.g. overscroll-behavior-x: contain.")],
  ".carousel { overscroll-behavior-x: contain; }",
  '<div style="font-size:11px;background:#fef2f2;border:1px solid #fecaca;padding:8px;border-radius:6px">overscroll-behavior: contain → reaching the edge of this scroller does not scroll the page behind it.</div>',
  "auto", ["overflow"])

p("scrollbar-width", "UI", "Firefox: scrollbar size (thin / auto / none).",
  "scrollbar-width: thin; + scrollbar-color: #cbd5e1 transparent; style scrollbars the standard way (Chrome now supports it too; WebKit still needs the pseudo-elements).",
  [("auto", "Default thickness."),
   ("thin", "Thin scrollbar."),
   ("none", "Hidden (element still scrolls).")],
  ".log { scrollbar-width: thin; scrollbar-color: #94a3b8 #f1f5f9; }",
  '<div style="font-size:11px;overflow:auto;max-height:40px;width:150px;background:#f8fafc;border:1px solid #e2e8f0;padding:6px;scrollbar-width:thin;scrollbar-color:#94a3b8 transparent;line-height:1.7">thin<br>scrollbar<br>width<br>demo<br>text<br>here</div>',
  "auto", ["scrollbar-color"])

p("scrollbar-color", "UI", "Firefox: scrollbar thumb + track colors.",
  "scrollbar-color: #64748b #f1f5f9; (thumb, track). The standard companion to scrollbar-width.",
  [("thumb track", "Two colors, or auto.")],
  "::-webkit-scrollbar { width: 10px; }  /* WebKit still needs pseudos */",
  '<div style="font-size:11px;color:#64748b">scrollbar-color: thumb track — two colors, done (standard, no pseudo-elements).</div>',
  "auto", ["scrollbar-width"])

p("accent-color" if False else "field-sizing", "UI",
  "Let an input/textarea size itself to its content (content-based width).",
  "field-sizing: content; sizes a text input to its text (like an auto-growing input). fix / none for fixed behavior. Newer property — check support before shipping.",
  [("content", "Size to the content."),
   ("fix", "Fixed size (default)."),
   ("none", "No automatic sizing.")],
  "input[name=\"name\"] { field-sizing: content; }",
  '<div style="font-size:11px;background:#f8fafc;border:1px solid #e2e8f0;padding:8px;border-radius:6px">field-sizing: content → the input grows with its text (progressive enhancement).</div>',
  "fix", ["resize"])

p("appearance", "UI",
  "Reset or request the native form-control look.",
  "none: strip the browser chrome (build your own checkbox/select/button styles). auto: keep native (the default). The first step of custom-styling form controls.",
  [("auto", "Native rendering (default)."),
   ("none", "No native styling — style it yourself."),
   ("button / textfield / …", "Request a specific widget look.")],
  ".toggle { appearance: none; }",
  '<div style="font-size:12px;display:flex;gap:8px;align-items:center"><input type="checkbox" checked style="appearance:none;width:20px;height:20px;border:2px solid #2563eb;border-radius:6px;background:#2563eb;display:grid;place-items:center;color:#fff;font-size:12px">appearance:none + custom styles = your own checkbox</div>',
  "auto", ["cursor"])

p("user-drag", "UI", "Whether the element can be dragged (legacy, mostly images).",
  "none disables native image dragging (dragstart doesn't fire). The global draggable attribute is the HTML-side equivalent.",
  [("auto", "Browser default."),
   ("none", "No native dragging."),
   ("element / all", "Drag the element / anything inside.")],
  "img.logo { user-drag: none; }",
  '<div style="font-size:11px;background:#f8fafc;border:1px solid #e2e8f0;padding:8px;border-radius:6px">user-drag: none → the image is not natively draggable.</div>',
  "auto", ["cursor"])

p("will-change", "Performance",
  "Hint: the element will change this property soon (promote it to a layer).",
  "will-change: transform; tells the browser to prepare a compositing layer → smoother animations. Overuse wastes memory — set it right before the change (via JS) and remove it after, or scope it to the animated element.",
  [("property list", "transform, opacity, scroll-position, contents, or a comma list."),
   ("auto", "Default — browser decides.")],
  ".enter { will-change: transform, opacity; transition: .3s; }",
  '<div style="font-size:11px;background:#ecfdf5;border:1px solid #6ee7b7;padding:8px;border-radius:6px">will-change: transform → browser pre-promotes this layer for a smoother animation (use sparingly!).</div>',
  "auto", ["transition", "transform"])
