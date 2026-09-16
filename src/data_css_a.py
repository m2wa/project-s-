# -*- coding: utf-8 -*-
# CSS properties — Part A: Layout, Box Model, Flexbox, Grid, Positioning
# Compiled from cssreference.io, W3Schools CSS, Elzero Web School, MDN cross-check.

P = []

def p(name, cat, s, d, vals, ex, dm, ini="", rel=()):
    P.append(dict(p=name, c=cat, s=s, d=d, V=list(vals), ex=ex, dm=dm, ini=ini, rel=list(rel)))

# ---------------- LAYOUT: DISPLAY & BOX ----------------
p("display", "Layout",
  "Sets how an element participates in layout: block, inline, flex, grid, none…",
  "The most powerful property in CSS. It decides whether an element takes a full line (block), flows with text (inline), or becomes a formatting container (flex/grid). display:none removes the element from layout entirely (display:contents removes only the box, keeping children).",
  [("block", "Full-width block; line breaks before and after (div, p, section)."),
   ("inline", "Flows with text; width/height ignored (span, a)."),
   ("inline-block", "Flows with text but accepts width/height/padding (buttons)."),
   ("flex", "Becomes a flex container; children are flex items."),
   ("grid", "Becomes a grid container; children are grid items."),
   ("none", "Not rendered at all (skipped by layout and assistive tech mostly)."),
   ("contents", "The element's box disappears; children render as if direct children."),
   ("table / table-row / table-cell", "Legacy table layout (pre-flex/grid era).")],
  "nav { display: flex; gap: 8px; }\n.card { display: inline-block; }",
  '<div style="font-size:11px"><div style="background:#fee2e2;padding:4px 8px;margin-bottom:4px">display:block — full line</div><div><span style="background:#fef9c3;padding:2px 6px">inline</span> flows with text <span style="background:#dbeafe;padding:2px 6px">inline</span></div><div style="display:flex;gap:6px;margin-top:4px"><span style="background:#dcfce7;padding:4px 8px">flex item 1</span><span style="background:#dcfce7;padding:4px 8px">flex item 2</span></div></div>',
  "inline", ["display", "flex-direction"])

p("box-sizing", "Box Model",
  "Whether width/height include padding and border.",
  "content-box (default): width is the content only; padding and border are added outside. border-box: width is the total including padding and border — almost always what you want. The common reset sets * { box-sizing: border-box; }.",
  [("content-box", "width = content only (default)."),
   ("border-box", "width = content + padding + border.")],
  "* { box-sizing: border-box; }\n.box { width: 200px; padding: 20px; border: 2px solid; }",
  '<div style="display:flex;gap:10px;font-size:10px"><div style="border:2px solid #ef4444;background:#fef2f2;width:150px;padding:10px">border-box: total = 150px <i>(incl. padding+border)</i></div><div style="border:2px solid #3b82f6;background:#eff6ff;width:130px;padding:10px">content-box: 130px <b>+</b> padding+border</div></div>',
  "content-box", ["width", "padding"])

p("width", "Box Model",
  "Sets the width of an element (content or border-box, per box-sizing).",
  "Accepted values: lengths (px, em, rem, %…), fit-content, min-content, max-content, and in flex/grid also flex-basis keywords. Percentages are relative to the containing block. width:auto (default for blocks) = as wide as the containing block.",
  [("auto", "Natural size (block: fill the parent)."),
   ("px / em / rem / %", "Absolute, relative, or percentage lengths."),
   ("fit-content", "Shrink to content, capped by available space."),
   ("min-content / max-content", "Smallest possible / widest single-line size."),
   ("100vw", "100% of the viewport width (mind the scrollbar).")],
  ".card { width: 320px; }\n.video { width: 100%; }",
  '<div style="font-size:10px;display:grid;gap:4px"><div style="background:#e0e7ff;border:1px solid #a5b4fc;padding:3px 6px;width:60%">width:60%</div><div style="background:#e0e7ff;border:1px solid #a5b4fc;padding:3px 6px;width:120px">width:120px</div><div style="background:#e0e7ff;border:1px solid #a5b4fc;padding:3px 6px">width:auto → fills</div></div>',
  "auto", ["height", "max-width", "box-sizing"])

p("height", "Box Model",
  "Sets the height of an element.",
  "Like width: lengths, %, auto. height:100% needs the parent to have a defined height. For full-viewport height use 100vh (or 100dvh to follow the mobile address bar).",
  [("auto", "Content height (default)."),
   ("px / % / vh", "Fixed, parent-relative, or viewport-relative."),
   ("100dvh", "Dynamic viewport height — accounts for mobile browser UI.")],
  "header { height: 64px; }\nmain { min-height: 100vh; }",
  '<div style="font-size:10px"><div style="background:#fce7f3;border:1px solid #f9a8d4;height:28px;line-height:28px;text-align:center">height:28px</div></div>',
  "auto", ["width", "max-height"])

p("max-width", "Box Model",
  "The upper limit of the width.",
  "The element can be any width up to max-width — wider content is clipped or wrapped instead. The classic readable-width trick: .container { max-width: 800px; margin-inline: auto; }.",
  [("px / em / %", "The ceiling, in any length unit."),
   ("none", "No limit (default).")],
  ".article { max-width: 70ch; }  /* ch = width of “0” */",
  '<div style="font-size:10px"><div style="max-width:170px;background:#ecfdf5;border:1px solid #6ee7b7;padding:4px 6px">max-width:170px — the text wraps instead of overflowing.</div></div>',
  "none", ["min-width", "width"])

p("min-width", "Box Model",
  "The lower limit of the width.",
  "Prevents an element from shrinking below the value — e.g. keeping a sidebar usable: .sidebar { min-width: 220px; }.",
  [("px / %", "The floor for the width."),
   ("0", "Default — allows shrinking.")],
  "input { min-width: 120px; }",
  '<div style="font-size:10px"><div style="min-width:150px;background:#fff7ed;border:1px solid #fdba74;padding:4px 6px">min-width:150px</div></div>',
  "0", ["max-width"])

p("max-height", "Box Model",
  "The upper limit of the height.",
  "Often paired with overflow:auto to make scrollable boxes: .log { max-height: 200px; overflow: auto; }.",
  [("px / vh", "The ceiling for height."),
   ("none", "Default.")],
  ".menu { max-height: 300px; overflow-y: auto; }",
  '<div style="font-size:10px;max-height:44px;overflow:auto;border:1px solid #a7f3d0;background:#ecfdf5;padding:4px">max-height:44px + overflow:auto → this small box scrolls internally.</div>',
  "none", ["min-height", "overflow"])

p("min-height", "Box Model",
  "The lower limit of the height.",
  "Keep areas from collapsing: .hero { min-height: 70vh; display: grid; place-items: center; }.",
  [("px / vh", "The floor for height."),
   ("0", "Default.")],
  "main { min-height: calc(100vh - 64px); }",
  '<div style="font-size:10px;min-height:60px;background:#f0f9ff;border:1px solid #7dd3fc;padding:4px;display:flex;align-items:center">min-height:60px — grows if content is taller</div>',
  "0", ["max-height"])

p("aspect-ratio", "Box Model",
  "Locks the width:height ratio (16/9, 1/1, 4/3…).",
  "Reserve space for images and media before they load (kills layout shift): .thumb { aspect-ratio: 16 / 9; }. With only one dimension set, the other is derived from the ratio.",
  [("width / height", "e.g. 16 / 9, 1, 4 / 3. Spaces around / are optional."),
   ("auto", "No ratio (default).")],
  ".thumb { aspect-ratio: 16 / 9; width: 100%; }",
  '<div style="display:flex;gap:8px;font-size:10px;align-items:flex-end"><div style="aspect-ratio:16/9;width:150px;background:linear-gradient(135deg,#0ea5e9,#6366f1);border-radius:6px"></div><div style="aspect-ratio:1/1;width:70px;background:linear-gradient(135deg,#f59e0b,#ef4444);border-radius:6px"></div><div style="aspect-ratio:4/3;width:110px;background:linear-gradient(135deg,#10b981,#059669);border-radius:6px"></div></div>',
  "auto", ["width", "height"])

# ---------------- MARGIN / PADDING ----------------
p("margin", "Box Model",
  "Space outside the border (all four sides in one declaration).",
  "margin: 10px → all sides; 10px 20px → top/bottom, left/right; four values → top right bottom left (clockwise from top). Positive margins push neighbors away; margins of adjacent blocks collapse (the bigger one wins) — flex/grid items don't collapse.",
  [("one length", "All four sides."),
   ("two lengths", "vertical, horizontal."),
   ("three lengths", "top, horizontal, bottom."),
   ("four lengths", "top, right, bottom, left."),
   ("auto", "Center the block (margin-inline: auto) or absorb leftover space in flex.")],
  ".card { margin: 16px 24px; }\n.center { margin-inline: auto; }",
  '<div style="font-size:10px;display:flex;gap:8px"><div style="background:#faf5ff;border:1px solid #d8b4fe;margin:8px 12px;padding:6px">margin:8px 12px</div></div>',
  "0", ["padding", "gap"])

p("margin-top", "Box Model", "Distance above the element (outside its border).", "One of the four individual margins. Block margins collapse: two stacked margins keep the larger, not the sum. margin-top doesn't work on flex items (use gap or padding).", [("length", "Any length or %.")], "h1 { margin-top: 0; }", '<div style="font-size:10px"><div style="background:#f3f4f6;padding:4px;margin-top:10px;border:1px solid #e5e7eb">10px above this box</div></div>', "0", ["margin"])

p("margin-right", "Box Model", "Distance to the right of the element.", "One of the four individual margins. In RTL pages it still means the physical right — for logical (flip with direction) use margin-inline-end.", [("length", "Any length or %.")], "li { margin-right: 8px; }", '<div style="font-size:10px;display:flex;gap:0"><span style="background:#fee2e2;border:1px solid #fca5a5;padding:4px 6px">A</span><span style="background:#fee2e2;border:1px solid #fca5a5;padding:4px 6px;margin-right:8px">B has 8px right</span></div>', "0", ["margin"])

p("margin-bottom", "Box Model", "Distance below the element.", "One of the four individual margins. Collides with the next sibling's margin-top — they collapse.", [("length", "Any length or %.")], "p { margin-bottom: 1em; }", '<div style="font-size:10px"><div style="background:#fef9c3;border:1px solid #fde047;padding:4px">margin-bottom:10px</div><div style="background:#f3f4f6;border:1px solid #e5e7eb;padding:4px">next box</div></div>', "0", ["margin"])

p("margin-left", "Box Model", "Distance to the left of the element.", "One of the four individual margins. For RTL-friendly code prefer margin-inline-start.", [("length", "Any length or %.")], "blockquote { margin-left: 24px; }", '<div style="font-size:10px"><div style="background:#dbeafe;border:1px solid #93c5fd;padding:4px;margin-left:20px">margin-left:20px</div></div>', "0", ["margin"])

p("margin-inline", "Box Model", "Logical left+right margin (flips with direction/RTL).", "margin-inline = margin-inline-start + margin-inline-end. In LTR: start=left; in RTL: start=right. Write once, works for both directions.", [("length", "One or two values: start, end.")], ".title { margin-inline: auto; }", '<div style="font-size:10px"><div style="margin-inline:auto;max-width:120px;background:#e0f2fe;border:1px solid #7dd3fc;padding:4px;text-align:center">centered with margin-inline:auto</div></div>', "0", ["margin"])

p("margin-block", "Box Model", "Logical top+bottom margin (flips with writing mode).", "margin-block = margin-block-start + margin-block-start… i.e. top/bottom for horizontal writing.", [("length", "One or two values.")], "section { margin-block: 32px; }", '<div style="font-size:10px;margin-block:10px"><div style="background:#ecfdf5;border:1px solid #6ee7b7;padding:4px">margin-block:10px top and bottom</div></div>', "0", ["margin"])

p("padding", "Box Model", "Space inside the border (all four sides).",
  "Same syntax as margin: 1–4 values. Padding never collapses and always adds to the box size (with border-box it's included in width). The go-to for spacing text from edges: .card { padding: 20px; }.",
  [("one length", "All sides."),
   ("two lengths", "vertical, horizontal."),
   ("three lengths", "top, horizontal, bottom."),
   ("four lengths", "top, right, bottom, left.")],
  "button { padding: 10px 18px; }",
  '<div style="font-size:10px"><div style="background:#fef2f2;border:2px solid #ef4444;padding:14px 10px 6px">padding:14px 10px 6px — space inside the border</div></div>',
  "0", ["margin", "gap"])

p("padding-top", "Box Model", "Inner space at the top (inside the border).", "One of the four individual paddings. Does not collapse — it always takes its declared space.", [("length", "Any length (no % of height for padding-top… it's % of width!).")], "header { padding-top: 16px; }", '<div style="font-size:10px"><div style="background:#fff7ed;border:2px solid #f97316;padding-top:16px">16px between border and content</div></div>', "0", ["padding"])

p("padding-right", "Box Model", "Inner space at the right.", "Individual padding. Use padding-inline-end for RTL-safe code.", [("length", "Any length.")], "pre { padding-right: 12px; }", '<div style="font-size:10px"><div style="background:#f0fdf4;border:2px solid #22c55e;padding-right:22px;text-align:right">right padding 22px</div></div>', "0", ["padding"])

p("padding-bottom", "Box Model", "Inner space at the bottom.", "Individual padding.", [("length", "Any length.")], "footer { padding-bottom: 24px; }", '<div style="font-size:10px"><div style="background:#fdf4ff;border:2px solid #d946ef;padding-bottom:16px">bottom padding 16px</div></div>', "0", ["padding"])

p("padding-left", "Box Model", "Inner space at the left.", "Individual padding. Use padding-inline-start for RTL-safe code.", [("length", "Any length.")], "li { padding-left: 8px; }", '<div style="font-size:10px"><div style="background:#eff6ff;border:2px solid #3b82f6;padding-left:22px">left padding 22px</div></div>', "0", ["padding"])

p("padding-inline", "Box Model", "Logical left+right padding (flips with direction).", "start + end padding in one declaration — the RTL-correct way to write horizontal padding.", [("length", "One or two values.")], ".btn { padding-inline: 16px; }", '<div style="font-size:10px"><div style="padding-inline:24px;background:#fefce8;border:2px solid #eab308;text-align:center;width:170px">padding-inline:24px</div></div>', "0", ["padding"])

p("padding-block", "Box Model", "Logical top+bottom padding.", "start + end padding for vertical space (logical for writing-mode).", [("length", "One or two values.")], ".card { padding-block: 12px; }", '<div style="font-size:10px"><div style="padding-block:14px;background:#f5f3ff;border:2px solid #8b5cf6">padding-block:14px</div></div>', "0", ["padding"])

# ---------------- BORDER ----------------
p("border", "Box Model", "Shorthand: width + style + color for the whole border.",
  "border: 1px solid #ccc; — the three parts in any order. You must include border-style (solid, dashed…) or the border won't show at all.",
  [("width style color", "e.g. 2px dashed #f59e0b. width: thin/medium/thick or a length; style: none|hidden|dotted|dashed|solid|double|groove|ridge|inset|outset; color: any color.")],
  ".box { border: 2px solid #4285f4; }",
  '<div style="font-size:10px;display:flex;gap:8px;flex-wrap:wrap"><span style="border:2px solid #4285f4;padding:6px">2px solid</span><span style="border:2px dashed #f59e0b;padding:6px">2px dashed</span><span style="border:2px dotted #ef4444;padding:6px">2px dotted</span><span style="border:3px double #10b981;padding:6px">3px double</span></div>',
  "medium none currentcolor", ["border-radius", "box-shadow"])

p("border-width", "Box Model", "Border thickness on all sides (1–4 values like margin).", "Without border-style the width does nothing.", [("length / thin|medium|thick", "Any length.")], "table { border-width: 1px 0; }", '<div style="font-size:10px"><span style="border:1px solid #9ca3af;border-width:4px 1px;padding:4px 8px">border-width:4px 1px</span></div>', "medium", ["border"])

p("border-style", "Box Model", "The line style of the border (all sides, 1–4 values).",
  "The part that actually makes the border visible.",
  [("none", "No border (default)."),
   ("hidden", "Like none, but wins in table border conflicts."),
   ("dotted", "Series of dots."),
   ("dashed", "Series of dashes."),
   ("solid", "Solid line."),
   ("double", "Two thin lines."),
   ("groove / ridge / inset / outset", "3D-look styles (mostly legacy).")],
  "img { border-style: dashed; }",
  '<div style="font-size:10px;display:flex;gap:6px;flex-wrap:wrap"><span style="border:2px dotted #6b7280;padding:4px">dotted</span><span style="border:2px dashed #6b7280;padding:4px">dashed</span><span style="border:2px solid #6b7280;padding:4px">solid</span><span style="border:2px double #6b7280;padding:4px">double</span><span style="border:4px groove #a78bfa;padding:4px">groove</span></div>',
  "none", ["border-width", "border-color"])

p("border-color", "Box Model", "Border color on all sides (1–4 values).", "Defaults to the element's color.", [("any color", "e.g. #ff0000, red, currentcolor.")], ".alert { border-color: #f59e0b; }", '<div style="font-size:10px;display:flex;gap:6px"><span style="border:2px solid #ef4444;padding:4px">red</span><span style="border:2px solid #22c55e;padding:4px">green</span><span style="border:2px solid #3b82f6;padding:4px">blue</span></div>', "currentcolor", ["border"])

p("border-top", "Box Model", "Shorthand for the top border (width + style + color).", "The other sides: border-right, border-bottom, border-left. Very common: .divider { border-top: 1px solid #e5e7eb; }.", [("width style color", "e.g. 1px solid #e5e7eb.")], "hr { border-top: 2px solid #333; }", '<div style="font-size:10px"><div style="border-top:2px solid #334155;padding-top:6px">border-top:2px solid</div></div>', "0", ["border", "border-radius"])

p("border-bottom", "Box Model", "Shorthand for the bottom border.", "Classic link hover: a:hover { border-bottom-color: currentColor; }.", [("width style color", "e.g. 1px solid.")], "a { border-bottom: 1px solid transparent; }", '<div style="font-size:10px"><span style="border-bottom:2px solid #2563eb;padding-bottom:2px">border-bottom:2px solid</span></div>', "0", ["border"])

p("border-radius", "Box Model",
  "Rounds the corners (all four in one declaration).",
  "border-radius: 8px → all corners. Four values: top-left, top-right, bottom-right, bottom-left. Two values + a / slash = horizontal / vertical radii (elliptical). border-radius: 50% on a square = a circle. Larger than half the box = fully pill-shaped (use 999px for pills).",
  [("one length", "All corners."),
   ("two lengths (h / v)", "Horizontal / vertical radius — ellipse corners."),
   ("three/four lengths", "Per corner: TL, TR, BR, BL."),
   ("50%", "Half — makes squares circular."),
   ("999px", "The pill trick (capsule shape).")],
  ".avatar { border-radius: 50%; }\n.pill { border-radius: 999px; }",
  '<div style="font-size:10px;display:flex;gap:8px;align-items:center"><span style="width:44px;height:44px;background:linear-gradient(135deg,#f472b6,#8b5cf6);border-radius:50%"></span><span style="background:#0ea5e9;color:#fff;padding:6px 14px;border-radius:999px">pill 999px</span><span style="background:#f59e0b;color:#fff;padding:6px 14px;border-radius:12px">12px</span></div>',
  "0", ["border", "background-clip"])

p("border-collapse", "Tables", "Merges adjacent table borders into one.",
  "collapse: borders of touching cells become a single shared border (clean look). separate: each cell keeps its own border (then use border-spacing for gaps).",
  [("collapse", "Shared borders (classic table)."),
   ("separate", "Independent borders + border-spacing (default).")],
  "table { border-collapse: collapse; }",
  '<div style="font-size:10px;display:grid;grid-template-columns:1fr 1fr;width:170px"><span style="border:1px solid #94a3b8;padding:4px;background:#f8fafc">1</span><span style="border:1px solid #94a3b8;padding:4px;background:#f8fafc">2</span><span style="border:1px solid #94a3b8;padding:4px;background:#f8fafc">3</span><span style="border:1px solid #94a3b8;padding:4px;background:#f8fafc">4</span></div>',
  "separate", ["border-spacing"])

p("border-spacing", "Tables", "Gap between table cells (separate mode).", "Only works when border-collapse: separate. One value = all gaps; two = columns, rows.", [("length", "One or two values.")], "table { border-spacing: 8px 4px; }", '<div style="font-size:10px;display:grid;grid-template-columns:1fr 1fr;gap:6px 10px;width:170px"><span style="background:#e0e7ff;padding:4px">1</span><span style="background:#e0e7ff;padding:4px">2</span><span style="background:#e0e7ff;padding:4px">3</span><span style="background:#e0e7ff;padding:4px">4</span></div>', "0", ["border-collapse"])

p("outline", "Box Model", "A line drawn outside the border (focus rings!).",
  "Unlike border, outline doesn't take layout space and follows border-radius in modern browsers. The accessibility default focus style: :focus-visible { outline: 2px solid #2563eb; outline-offset: 2px; }.",
  [("width style color", "e.g. 2px solid #2563eb.")],
  "a:focus-visible { outline: 3px solid #2563eb; outline-offset: 2px; }",
  '<div style="font-size:10px"><span style="outline:3px solid #2563eb;outline-offset:3px;padding:4px 8px;background:#eff6ff">outline (outside the box)</span></div>',
  "none", ["outline-offset", "border"])

p("outline-offset", "Box Model", "Distance between the outline and the element edge.",
  "Positive values push the outline out. Essential for accessible focus rings that don't touch the element.",
  [("length", "e.g. 2px, -1px.")],
  ":focus-visible { outline-offset: 3px; }",
  '<div style="font-size:10px"><span style="outline:2px dashed #f59e0b;outline-offset:6px;padding:4px 8px">offset:6px</span></div>',
  "0", ["outline"])

p("box-shadow", "Box Model",
  "One or more shadows around the box.",
  "Syntax: x y blur spread color [inset]. x/y = offset (negative = left/up), blur = softness, spread = grows the shadow, inset = shadow inside the box. Stack multiple shadows with commas.",
  [("x y blur spread color", "e.g. 0 4px 12px rgba(0,0,0,.15)."),
   ("inset", "Shadow inside the element."),
   ("multiple", "comma-separated list.")],
  ".card { box-shadow: 0 4px 12px rgba(0,0,0,.12); }\n.inset { box-shadow: inset 0 2px 6px rgba(0,0,0,.2); }",
  '<div style="font-size:10px;display:flex;gap:14px;align-items:center;flex-wrap:wrap"><span style="padding:10px;background:#fff;border:1px solid #e5e7eb;box-shadow:0 4px 12px rgba(0,0,0,.18)">soft shadow</span><span style="padding:10px;background:#fff;border:1px solid #e5e7eb;box-shadow:8px 8px 0 #c7d2fe">hard 8/8</span><span style="padding:10px;background:#fef9c3;box-shadow:inset 0 3px 8px rgba(0,0,0,.25)">inset</span></div>',
  "none", ["border-radius"])

# ---------------- FLOAT / POSITION / OVERFLOW ----------------
p("float", "Layout", "Floats the element left/right; text wraps around it.",
  "Historical layout tool (magazine layouts). Still the cleanest way to pull an image into flowing text. Floating removes the element from normal flow — parents need a clearfix/overflow or a modern flex alternative.",
  [("none", "No float (default)."),
   ("left / right", "Float to that side."),
   ("inline-start / inline-end", "Logical versions (flip with RTL).")],
  ".pull-quote { float: right; margin: 0 0 12px 20px; }",
  '<div style="font-size:11px;line-height:1.55;width:230px"><span style="float:right;width:70px;height:50px;background:linear-gradient(135deg,#f472b6,#fb7185);border-radius:6px;margin:0 0 6px 12px;display:inline-block"></span>Text wraps around the floated image on both sides. This is the classic figure layout that floats are still perfect for.</div>',
  "none", ["clear", "position"])

p("clear", "Layout", "Prevents floats on one or both sides (moves the box below them).",
  "clear: left stops the box from sitting beside a left float. clearfix pattern: .wrap::after { content:""; display:block; clear:both; } — or use overflow:hidden/auto on the parent.",
  [("none", "Default."),
   ("left / right", "Clear that side."),
   ("both", "Clear both sides."),
   ("inline-start / inline-end", "Logical versions.")],
  ".clear { clear: both; }",
  '<div style="font-size:10px;width:200px"><div style="float:left;width:80px;height:24px;background:#bfdbfe;border:1px solid #93c5fd;margin-right:8px">float:left</div><div style="clear:left;background:#fee2e2;border:1px solid #fca5a5;padding:4px">clear:left — drops below the float</div></div>',
  "none", ["float"])

p("position", "Layout",
  "The positioning scheme of the element (static, relative, absolute, fixed, sticky).",
  "The master switch for layout placement. static = normal flow (default). relative = offset from its own place (keeps its space). absolute = removed from flow, placed against the nearest non-static ancestor. fixed = against the viewport (stays put on scroll). sticky = hybrid: in flow until a threshold, then sticks.",
  [("static", "Normal flow (default). top/left ignored."),
   ("relative", "Offset from its own position; becomes a containing block for absolute descendants."),
   ("absolute", "Placed by top/right/bottom/left against the nearest positioned ancestor; out of flow."),
   ("fixed", "Against the viewport; ignores scroll."),
   ("sticky", "Stays in flow but sticks within its parent once a threshold is passed.")],
  ".header { position: sticky; top: 0; }\n.modal { position: fixed; inset: 0; }",
  '<div style="font-size:10px;position:relative;width:220px;height:90px;background:#f8fafc;border:1px dashed #94a3b8"><span style="position:absolute;right:8px;top:8px;background:#2563eb;color:#fff;padding:3px 8px;border-radius:4px">absolute in the corner</span><div style="position:sticky;top:0;background:#fef9c3;padding:4px;margin-top:26px">sticky (sticks at top:0 while the parent scrolls)</div></div>',
  "static", ["top", "z-index"])

p("top", "Positioning", "Vertical offset for positioned elements.",
  "Works with position: relative (offset from own place), absolute (distance from top of the containing block), fixed (from viewport top), sticky (threshold from the scroll port top). Ignored on static elements.",
  [("length / %", "e.g. 0, 16px, 50%. % of the containing block's height.")],
  ".toast { position: fixed; top: 16px; right: 16px; }",
  '<div style="font-size:10px;position:relative;height:70px;background:#f8fafc;border:1px dashed #94a3b8"><span style="position:absolute;top:6px;left:6px;background:#10b981;color:#fff;padding:3px 8px;border-radius:4px">top:6px</span></div>',
  "auto", ["bottom", "left", "right"])

p("bottom", "Positioning", "Vertical offset from the bottom.",
  "Same rules as top but measured from the bottom edge: fixed bottom bar → .bar { position: fixed; bottom: 0; }.",
  [("length / %", "e.g. 0, 12px.")],
  ".footer-fixed { position: fixed; bottom: 0; left: 0; right: 0; }",
  '<div style="font-size:10px;position:relative;height:70px;background:#f8fafc;border:1px dashed #94a3b8"><span style="position:absolute;bottom:6px;right:6px;background:#f59e0b;color:#fff;padding:3px 8px;border-radius:4px">bottom:6px</span></div>',
  "auto", ["top"])

p("left", "Positioning", "Horizontal offset from the left.",
  "Same rules as top for the horizontal axis. In RTL documents, prefer inset-inline-start for flip-safe code.",
  [("length / %", "e.g. 0, 50%.")],
  ".sidebar { position: absolute; left: 0; }",
  '<div style="font-size:10px;position:relative;height:60px;background:#f8fafc;border:1px dashed #94a3b8"><span style="position:absolute;left:8px;top:16px;background:#6366f1;color:#fff;padding:3px 8px;border-radius:4px">left:8px</span></div>',
  "auto", ["right"])

p("right", "Positioning", "Horizontal offset from the right.",
  "Same rules as left. Watch: setting both left and right (with no width) stretches the element.",
  [("length / %", "e.g. 0, 16px.")],
  ".badge { position: absolute; right: 8px; top: 8px; }",
  '<div style="font-size:10px;position:relative;height:60px;background:#f8fafc;border:1px dashed #94a3b8"><span style="position:absolute;right:8px;top:16px;background:#ef4444;color:#fff;padding:3px 8px;border-radius:4px">right:8px</span></div>',
  "auto", ["left"])

p("inset", "Positioning", "Shorthand for top/right/bottom/left (one declaration).",
  "inset: 0 → pin the element to all four sides of its containing block (full overlay). 16px → 16px padding from all sides. Two values = vertical, horizontal; four = TRBL.",
  [("0", "Pin to all sides (full overlay)."),
   ("one length", "All four offsets."),
   ("two lengths", "vertical, horizontal."),
   ("four lengths", "top right bottom left.")],
  ".overlay { position: fixed; inset: 0; background: rgba(0,0,0,.5); }",
  '<div style="font-size:10px;position:relative;height:70px;background:#f8fafc;border:1px dashed #94a3b8"><span style="position:absolute;inset:8px;background:rgba(37,99,235,.12);border:1px solid #93c5fd;border-radius:6px;display:flex;align-items:center;justify-content:center">inset:8px</span></div>',
  "auto", ["top", "left"])

p("z-index", "Positioning", "Stacking order of positioned elements (higher = on top).",
  "Only works on positioned elements (and flex/grid items). Auto = normal DOM order. Negative values go behind. Each position: value creates a stacking context — z-index can't escape its context. The classic fix for overlapping UI: assign explicit levels (header 10, modal 100, toast 1000).",
  [("auto", "Default — painted in DOM order."),
   ("integer", "Any number, positive or negative.")],
  ".modal { z-index: 100; }\n.header { z-index: 10; }",
  '<div style="position:relative;height:64px;font-size:10px"><span style="position:absolute;left:20px;top:18px;width:90px;height:28px;background:#c7d2fe;z-index:1">z:1 (bottom)</span><span style="position:absolute;left:50px;top:18px;width:90px;height:28px;background:#fca5a5;z-index:2">z:2</span><span style="position:absolute;left:90px;top:18px;width:90px;height:28px;background:#fde047;z-index:3">z:3 (top)</span></div>',
  "auto", ["position"])

p("overflow", "Layout", "What happens when content is bigger than the box (clip, scroll…).",
  "visible (default) lets content spill out; hidden clips it (also creates a block formatting context — old clearfix); auto adds scrollbars only when needed; scroll always shows them. overflow-x/overflow-y for one axis. Note: setting one axis to hidden makes the other become auto (never visible).",
  [("visible", "Content spills out (default for most elements)."),
   ("hidden", "Clipped, no scrollbars."),
   ("scroll", "Scrollbars always shown."),
   ("auto", "Scrollbars when needed."),
   ("clip", "Clipped without creating a scroll container (newer).")],
  ".pre { overflow-x: auto; }\n.hero { overflow: hidden; }",
  '<div style="font-size:10px"><div style="width:150px;overflow:hidden;border:1px solid #fca5a5;background:#fef2f2;padding:4px">overflow:hidden — <span>everything after this point is clipped and gone.</span></div><div style="width:150px;overflow:auto;border:1px solid #93c5fd;background:#eff6ff;padding:4px;max-height:40px">overflow:auto — <span>this box scrolls when the text is longer than the box allows it to show.</span></div></div>',
  "visible", ["overflow-x", "overflow-y"])

p("overflow-x", "Layout", "Horizontal overflow behavior (clip/scroll/auto/hidden).", "Control scrollbars on the x-axis only: .table-wrap { overflow-x: auto; } makes wide tables scroll on mobile.", [("keyword", "same as overflow.")], "table { display: block; overflow-x: auto; }", '<div style="width:150px;overflow-x:auto;border:1px solid #d1d5db;font-size:10px"><div style="width:300px;background:#f8fafc;padding:4px">this 300px row scrolls horizontally inside the 150px box</div></div>', "visible", ["overflow"])

p("overflow-y", "Layout", "Vertical overflow behavior.", "Same as overflow-x for the vertical axis: .log { overflow-y: auto; max-height: 300px; }.", [("keyword", "same as overflow.")], ".chat { overflow-y: auto; }", '<div style="width:150px;overflow-y:auto;max-height:44px;border:1px solid #d1d5db;font-size:10px;background:#f8fafc;padding:4px">one line<br>two lines<br>three lines<br>four lines<br>five lines</div>', "visible", ["overflow"])

p("overflow-wrap", "Typography", "Break long words so they don't overflow (break-word).",
  "break-word allows breaking long words (URLs!) to fit the box; normal (default) doesn't. The modern name for the old word-wrap.",
  [("normal", "No breaking (default)."),
   ("break-word", "Break when necessary.")],
  "p { overflow-wrap: break-word; }",
  '<div style="width:130px;font-size:11px;overflow-wrap:break-word;border:1px dashed #94a3b8;padding:6px">https://www.example.com/a-very/long-url-that-must-wrap-instead-of-overflowing</div>',
  "normal", ["word-break", "overflow"])

p("visibility", "Layout", "Show or hide an element while keeping its space.",
  "hidden = invisible but still occupies layout (unlike display:none which removes the space). Toggled with JS or media queries; inherited by descendants (a visible child can re-show itself).",
  [("visible", "Default."),
   ("hidden", "Invisible, space preserved."),
   ("collapse", "Like hidden for tables (removes the row/col space).")],
  "@media print { .no-print { visibility: hidden; } }",
  '<div style="font-size:10px;display:flex;gap:6px"><span style="border:1px solid #d1d5db;padding:4px">visible</span><span style="border:1px dashed #d1d5db;padding:4px;color:transparent;background:#f3f4f6">visibility:hidden (space kept)</span></div>',
  "visible", ["display"])

p("content-visibility", "Performance", "Skip rendering of off-screen subtrees (auto + contain-intrinsic-size).",
  "auto tells the browser: don't fully render this subtree until it's near the viewport. Huge scroll performance win for long pages. Pair with contain-intrinsic-size so layout stays stable.",
  [("visible", "Default."),
   ("auto", "Skip rendering until near the viewport.")],
  ".feed-item { content-visibility: auto; contain-intrinsic-size: auto 120px; }",
  '<div style="font-size:10px;background:#ecfdf5;border:1px solid #6ee7b7;padding:6px">content-visibility:auto → browser skips painting this subtree while it is off-screen (faster long pages).</div>',
  "visible", ["contain"])

p("zoom", "Layout", "Scales the rendered size of an element (non-standard but universal).",
  "zoom: 1.5 enlarges the element (and its layout space). Not in the CSS spec but supported everywhere; the standard alternative is transform: scale() (which doesn't affect layout) — or design responsively instead of zooming.",
  [("number / %", "e.g. 1.5, 75%.")],
  ".legacy { zoom: 1.2; }",
  '<div style="font-size:10px;display:flex;gap:8px;align-items:center"><span style="border:1px solid #d1d5db;padding:4px">normal</span><span style="zoom:1.3;border:1px solid #d1d5db;padding:4px">zoom:1.3</span></div>',
  "1", ["transform"])

p("contain", "Performance", "Limits an element's side effects (layout, paint, size, style) to its subtree.",
  "Performance hint for the browser: contain: layout paint size strict — the element's internals can't affect the outside, so the browser can skip reflows outside it. Great for lists, cards, and iframes.",
  [("none", "Default."),
   ("layout", "Internal layout can't affect outside."),
   ("paint", "Nothing inside paints outside the box."),
   ("size", "Size doesn't depend on contents."),
   ("strict / content", "Combos.")],
  ".card { contain: layout paint; }",
  '<div style="font-size:10px;background:#f5f3ff;border:1px solid #c4b5fd;padding:6px">contain: paint → the browser knows nothing inside can draw outside this box (faster repaints).</div>',
  "none", ["content-visibility"])

p("perspective", "3D Transforms", "How strong the 3D effect looks (distance of the viewer's eye).",
  "Set on the parent to give children 3D depth: smaller value = more dramatic. perspective: 600px; then children use transform: rotateY(…). perspective-origin moves the vanishing point.",
  [("length", "e.g. 400px – 2000px."),
   ("none", "No perspective (default).")],
  ".scene { perspective: 800px; }\n.card { transform: rotateY(20deg); }",
  '<div style="font-size:10px;display:flex;gap:20px;align-items:center"><div style="perspective:300px;width:70px;height:46px"><div style="width:100%;height:100%;background:#6366f1;transform:rotateY(35deg);display:flex;align-items:center;justify-content:center;color:#fff">300px</div></div><div style="perspective:1200px;width:70px;height:46px"><div style="width:100%;height:100%;background:#94a3b8;transform:rotateY(35deg);display:flex;align-items:center;justify-content:center;color:#fff">1200px</div></div></div>',
  "none", ["transform", "transform-style"])

p("transform-style", "3D Transforms", "Keep children in the same 3D space (preserve-3d).",
  "preserve-3d lets nested transforms share one 3D plane (needed for CSS 3D cards/cubes). flat (default) flattens children into 2D.",
  [("flat", "Default — children flattened."),
   ("preserve-3d", "Children live in the same 3D space.")],
  ".card { transform-style: preserve-3d; }",
  '<div style="font-size:10px;background:#f8fafc;border:1px solid #d1d5db;padding:8px">preserve-3d → inner elements share one 3D coordinate space (needed for cube/card flips).</div>',
  "flat", ["perspective"])

p("backface-visibility", "3D Transforms", "Hide the element when it's rotated to show its back.",
  "hidden makes the element disappear past 90° of rotation — the other half of the classic 3D flip card trick.",
  [("visible", "Default — you can see the mirrored back."),
   ("hidden", "Invisible when its back faces the viewer.")],
  ".card-front { backface-visibility: hidden; }",
  '<div style="font-size:10px"><div style="width:90px;height:56px;background:#4ade80;transform:rotateY(180deg);display:flex;align-items:center;justify-content:center;color:#14532d">mirrored text = backface visible</div></div>',
  "visible", ["transform-style"])

# ---------------- FLEXBOX ----------------
p("flex-direction", "Flexbox", "The main axis direction of a flex container.",
  "row (default): left→right, wrap to new rows. row-reverse: right→left. column: top→bottom, wrap to new columns. column-reverse: bottom→top. The main axis determines where justify-content works and where items grow.",
  [("row", "Left → right (default)."),
   ("row-reverse", "Right → left."),
   ("column", "Top → bottom."),
   ("column-reverse", "Bottom → top.")],
  ".nav { display: flex; flex-direction: row; }\n.stack { display: flex; flex-direction: column; gap: 8px; }",
  '<div style="font-size:10px"><div style="display:flex;gap:4px"><span style="background:#93c5fd;padding:4px 10px">1</span><span style="background:#93c5fd;padding:4px 10px">2</span><span style="background:#93c5fd;padding:4px 10px">3</span></div><div style="display:flex;flex-direction:column;gap:4px;margin-top:6px"><span style="background:#fca5a5;padding:4px 10px">1</span><span style="background:#fca5a5;padding:4px 10px">2</span></div></div>',
  "row", ["justify-content", "flex-wrap"])

p("flex-wrap", "Flexbox", "Whether flex items wrap to multiple lines.",
  "nowrap (default) squishes items into one line; wrap allows new lines; wrap-reverse flips the cross axis of wrapped lines. The classic responsive nav: flex-wrap: wrap; gap: 8px;.",
  [("nowrap", "One line (default)."),
   ("wrap", "Wrap to next line."),
   ("wrap-reverse", "Wrap, new lines start from the cross-end.")],
  ".toolbar { display: flex; flex-wrap: wrap; gap: 8px; }",
  '<div style="font-size:10px"><div style="display:flex;gap:4px"><span style="background:#c4b5fd;padding:4px 8px">a</span><span style="background:#c4b5fd;padding:4px 8px">b</span><span style="background:#c4b5fd;padding:4px 8px">c</span><span style="background:#c4b5fd;padding:4px 8px">d</span></div><div style="display:flex;flex-wrap:wrap;gap:4px;max-width:120px;margin-top:6px;border:1px dashed #a78bfa"><span style="background:#c4b5fd;padding:4px 8px">a</span><span style="background:#c4b5fd;padding:4px 8px">b</span><span style="background:#c4b5fd;padding:4px 8px">c</span><span style="background:#c4b5fd;padding:4px 8px">d</span></div></div>',
  "nowrap", ["flex-direction", "gap"])

p("flex-flow", "Flexbox", "Shorthand: flex-direction + flex-wrap.",
  "flex-flow: column wrap; — order doesn't matter.",
  [("direction wrap", "e.g. row wrap, column nowrap.")],
  ".gallery { flex-flow: row wrap; }",
  '<div style="font-size:10px;background:#f0f9ff;border:1px solid #7dd3fc;padding:6px">flex-flow = flex-direction + flex-wrap in one line.</div>',
  "row nowrap", ["flex-direction", "flex-wrap"])

p("justify-content", "Flexbox", "Distributes flex items along the main axis.",
  "How items sit on the main axis: flex-start (packed at start, default), center, flex-end, space-between (even space between, none at edges), space-around (equal space around each), space-evenly (all gaps equal).",
  [("flex-start", "Packed at the start (default)."),
   ("center", "Centered as a group."),
   ("flex-end", "Packed at the end."),
   ("space-between", "First at start, last at end, even space between."),
   ("space-around", "Equal space around each item (half at the edges)."),
   ("space-evenly", "All gaps equal, including the edges.")],
  ".nav { justify-content: space-between; }\n.actions { justify-content: center; }",
  '<div style="font-size:9px"><div style="display:flex;justify-content:space-between;border:1px dashed #94a3b8;padding:4px;margin-bottom:4px"><span style="background:#fcd34d;padding:2px 6px">A</span><span style="background:#fcd34d;padding:2px 6px">B</span><span style="background:#fcd34d;padding:2px 6px">C</span></div><div style="display:flex;justify-content:space-evenly;border:1px dashed #94a3b8;padding:4px"><span style="background:#fcd34d;padding:2px 6px">A</span><span style="background:#fcd34d;padding:2px 6px">B</span><span style="background:#fcd34d;padding:2px 6px">C</span></div></div>',
  "normal", ["align-items", "flex-direction"])

p("align-items", "Flexbox", "Aligns flex items along the cross axis (for all items).",
  "stretch (default): items fill the cross size. center: vertically centered (the classic .icon-row { display:flex; align-items:center } ). flex-start / flex-end: to the cross-start/end. baseline: align by text baseline.",
  [("stretch", "Items fill the cross axis (default)."),
   ("flex-start / flex-end", "To the cross start/end."),
   ("center", "Centered on the cross axis."),
   ("baseline", "Text baselines align.")],
  ".icon-label { display: flex; align-items: center; gap: 8px; }",
  '<div style="font-size:9px"><div style="display:flex;align-items:center;gap:4px;height:40px;border:1px dashed #94a3b8;padding:4px"><span style="background:#86efac;padding:2px 6px">tall</span><span style="background:#86efac;padding:6px 6px">short</span></div><div style="display:flex;align-items:flex-end;gap:4px;height:40px;border:1px dashed #94a3b8;padding:4px;margin-top:4px"><span style="background:#f9a8d4;padding:2px 6px">tall</span><span style="background:#f9a8d4;padding:6px 6px">short</span></div></div>',
  "normal", ["align-self", "align-content"])

p("align-content", "Flexbox", "Distributes the flex LINES when items wrap (needs flex-wrap).",
  "With one line it does nothing (unless items are stretched). space-between spreads wrapped lines; center centers the block of lines; stretch stretches lines to fill.",
  [("normal / stretch", "Lines stretch (default)."),
   ("flex-start / flex-end / center", "Pack / center lines."),
   ("space-between / space-around / space-evenly", "Distribute line gaps.")],
  ".gallery { display: flex; flex-wrap: wrap; align-content: space-between; min-height: 200px; }",
  '<div style="font-size:9px"><div style="display:flex;flex-wrap:wrap;gap:4px;align-content:space-between;height:80px;width:150px;border:1px dashed #94a3b8;padding:4px"><span style="background:#a5b4fc;padding:2px 6px">1</span><span style="background:#a5b4fc;padding:2px 6px">2</span><span style="background:#a5b4fc;padding:2px 6px">3</span><span style="background:#a5b4fc;padding:2px 6px">4</span><span style="background:#a5b4fc;padding:2px 6px">5</span><span style="background:#a5b4fc;padding:2px 6px">6</span></div></div>',
  "normal", ["justify-content", "flex-wrap"])

p("align-self", "Flexbox", "Overrides align-items for one item.",
  "auto = follow align-items; otherwise the same keywords (center, flex-start…). Use it to pin one item to the bottom of a row.",
  [("auto", "Inherit the container's align-items."),
   ("flex-start / flex-end / center / baseline / stretch", "Per-item cross placement.")],
  ".cart .remove { align-self: flex-end; }",
  '<div style="font-size:9px"><div style="display:flex;align-items:flex-start;gap:4px;height:44px;border:1px dashed #94a3b8;padding:4px"><span style="background:#fda4af;padding:6px 8px">align-start</span><span style="background:#5eead4;padding:6px 8px;align-self:flex-end">align-self:flex-end</span></div></div>',
  "auto", ["align-items"])

p("flex-grow", "Flexbox", "How much an item grows to fill spare space (ratio).",
  "0 (default) = never grow. flex-grow: 1 = take a share of the leftover space. flex-grow: 2 = double the share of a flex-grow:1 item. The 3-column trick: two sidebars flex:1, main flex:2.",
  [("number ≥ 0", "Growth weight (default 0).")],
  ".layout { display: flex; gap: 16px; }\n.layout .main { flex-grow: 2; }\n.layout aside { flex-grow: 1; }",
  '<div style="font-size:9px"><div style="display:flex;gap:4px"><div style="flex-grow:1;background:#fdba74;padding:4px">grow:1</div><div style="flex-grow:2;background:#fb923c;padding:4px">grow:2 (double width)</div></div></div>',
  "0", ["flex-shrink", "flex-basis"])

p("flex-shrink", "Flexbox", "How much an item shrinks when space runs out (ratio).",
  "1 (default) = shrink proportionally. flex-shrink: 0 = never shrink (keeps its size, may overflow). The classic fix: logo { flex-shrink: 0; } so the logo doesn't squish.",
  [("number ≥ 0", "Shrink weight (default 1).")],
  ".brand { flex-shrink: 0; }",
  '<div style="font-size:9px;max-width:160px"><div style="display:flex;gap:4px"><span style="flex-shrink:0;background:#fca5a5;padding:4px 10px">shrink:0</span><span style="flex:1;background:#fecaca;padding:4px">shrink:1 (squishes)</span></div></div>',
  "1", ["flex-grow"])

p("flex-basis", "Flexbox", "The item's starting main-size before grow/shrink.",
  "auto (default) = use width/height/content. 0 = start from zero and grow to fill (the basis of flex:1). A fixed value = start from that size.",
  [("auto", "Use the item's size properties (default)."),
   ("length", "e.g. 200px."),
   ("0", "Start from nothing — combined with grow, fills evenly.")],
  ".col { flex-basis: 250px; flex-grow: 1; }",
  '<div style="font-size:9px"><div style="display:flex;gap:4px"><div style="flex:0 0 60px;background:#93c5fd;padding:4px">basis 60px</div><div style="flex:1;background:#60a5fa;padding:4px">basis 0 + grow 1</div></div></div>',
  "auto", ["flex", "flex-grow"])

p("flex", "Flexbox", "Shorthand: flex-grow flex-shrink flex-basis.",
  "flex: 1 = 1 1 0% (grow, shrink, zero basis) — the workhorse. flex: auto = 1 1 auto. flex: none = 0 1 auto (natural size). flex: 0 0 200px = fixed 200px, no grow/shrink.",
  [("grow shrink basis", "e.g. 1 1 0%, 0 0 auto, 2."),
   ("1", "= 1 1 0% — fill remaining space."),
   ("none", "= 0 1 auto — natural size."),
   ("auto", "= 1 1 auto.")],
  ".sidebar { flex: 0 0 240px; }\n.content { flex: 1; }",
  '<div style="font-size:9px"><div style="display:flex;gap:4px"><div style="flex:0 0 70px;background:#f0abfc;padding:4px">0 0 70px</div><div style="flex:1;background:#d946ef;color:#fff;padding:4px">flex:1 fills the rest</div></div></div>',
  "0 1 auto", ["flex-grow", "flex-shrink", "flex-basis"])

p("gap", "Flexbox & Grid", "Space between flex/grid items (row-gap + column-gap).",
  "The modern replacement for margin hacks: gap works in both flexbox and grid. One value = both directions; two = row, column. Margins between items no longer needed — and they don't collapse.",
  [("length", "One or two values: row-gap, column-gap.")],
  ".grid { display: grid; gap: 16px; }\n.nav { display: flex; gap: 8px; }",
  '<div style="font-size:9px"><div style="display:flex;gap:8px"><span style="background:#6ee7b7;padding:6px 10px">A</span><span style="background:#6ee7b7;padding:6px 10px">B</span><span style="background:#6ee7b7;padding:6px 10px">C</span></div><div style="font-size:9px;color:#047857;margin-top:2px">gap:8px — no margins on the items</div></div>',
  "normal", ["row-gap", "column-gap"])

p("row-gap", "Flexbox & Grid", "Space between rows (flex lines / grid rows).", "The vertical part of gap.", [("length", "e.g. 12px.")], ".list { display: grid; row-gap: 12px; }", '<div style="font-size:9px;display:grid;row-gap:8px"><span style="background:#fde68a;padding:4px 10px">row 1</span><span style="background:#fde68a;padding:4px 10px">row 2</span></div>', "normal", ["gap"])

p("column-gap", "Flexbox & Grid", "Space between columns (grid columns / flex columns).", "The horizontal part of gap.", [("length", "e.g. 16px.")], ".cards { column-gap: 16px; }", '<div style="font-size:9px;display:flex;column-gap:12px"><span style="background:#fbcfe8;padding:4px 10px">c1</span><span style="background:#fbcfe8;padding:4px 10px">c2</span></div>', "normal", ["gap"])

p("order", "Flexbox & Grid", "Changes the visual order of an item (without touching HTML).",
  "0 = default. Negative goes first, positive later. Order is visual only — DOM/keyboard order is unchanged, which matters for accessibility (don't restructure semantics with order).",
  [("integer", "e.g. -1, 0, 2.")],
  ".footer .social { order: -1; }",
  '<div style="font-size:9px"><div style="display:flex;gap:4px"><span style="order:2;background:#e9d5ff;padding:4px 10px">order:2</span><span style="order:-1;background:#a78bfa;padding:4px 10px">order:-1 (first)</span><span style="background:#d8b4fe;padding:4px 10px">order:0</span></div></div>',
  "0", ["flex", "grid-column"])

# ---------------- GRID ----------------
p("display: grid" if False else "grid-template-columns", "Grid",
  "Defines the columns of a grid (track sizes).",
  "The heart of grid layout. fr = fraction of free space; fixed units for fixed tracks; minmax() for flexible-with-limits; repeat() for repetition; auto-fit/auto-fill for responsive card grids without media queries. Example: repeat(auto-fit, minmax(220px, 1fr)) = as many 220px+ columns as fit, stretching to fill.",
  [("fr", "Fraction of free space (1fr = equal share)."),
   ("length / %", "Fixed or percentage track."),
   ("minmax(min, max)", "Between two sizes, e.g. minmax(200px, 1fr)."),
   ("repeat(n, …)", "Repeat a track list."),
   ("auto-fit / auto-fill", "Implicit columns that fill the row (auto-fit collapses empties)."),
   ("fit-content", "Size to content.")],
  ".gallery {\n  display: grid;\n  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));\n  gap: 16px;\n}",
  '<div style="font-size:9px"><div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(56px,1fr));gap:6px;max-width:230px"><div style="background:#bae6fd;padding:6px">a</div><div style="background:#7dd3fc;padding:6px">b</div><div style="background:#38bdf8;padding:6px">c</div><div style="background:#0ea5e9;padding:6px;color:#fff">d</div><div style="background:#0369a1;padding:6px;color:#fff">e</div></div><div style="color:#0369a1">repeat(auto-fit, minmax(56px, 1fr)) — responsive without media queries</div></div>',
  "none", ["grid-template-rows", "gap"])

p("grid-template-rows", "Grid", "Defines the rows of a grid (track sizes).",
  "Same values as columns: fr, lengths, minmax, repeat. grid-template-rows: auto 1fr auto; = the classic holy-grail skeleton (header, filling main, footer).",
  [("fr / length / minmax / repeat", "As in grid-template-columns.")],
  ".page { display: grid; grid-template-rows: auto 1fr auto; min-height: 100vh; }",
  '<div style="font-size:9px;display:grid;grid-template-rows:auto 1fr auto;height:90px;max-width:200px;gap:4px"><div style="background:#fde68a;padding:4px">auto (header)</div><div style="background:#bbf7d0;padding:4px">1fr (fills)</div><div style="background:#fde68a;padding:4px">auto (footer)</div></div>',
  "none", ["grid-template-columns"])

p("grid-template-areas", "Grid",
  "Names grid regions with an ASCII map — the most readable layout syntax.",
  "Draw the layout as text, then assign items with grid-area: .header { grid-area: hd; }. Dots are empty cells; repeated names span cells.",
  [("named map", "e.g. \"hd hd\" \"sb main\" \"ft ft\".")],
  ".layout {\n  display: grid;\n  grid-template-areas:\n    \"hd  hd\"\n    \"sb  main\"\n    \"ft  ft\";\n}",
  '<div style="font-size:9px;display:grid;grid-template-areas:"hd hd" "sb main" "ft ft";grid-template-columns:40px 1fr;max-width:210px;gap:4px"><div style="grid-area:hd;background:#fcd34d;padding:4px;text-align:center">hd</div><div style="grid-area:sb;background:#fdba74;padding:4px">sb</div><div style="grid-area:main;background:#93c5fd;padding:4px">main</div><div style="grid-area:ft;background:#fcd34d;padding:4px;text-align:center">ft</div></div>',
  "none", ["grid-area"])

p("grid-area", "Grid", "Places an item in a grid area (shorthand for row/column start+end).",
  "grid-area: header → the named area. Or explicit lines: grid-area: 1 / 1 / 3 / 4; = row 1→3, column 1→4.",
  [("name", "Named area from grid-template-areas."),
   ("row-start / col-start / row-end / col-end", "Explicit line numbers.")],
  ".nav { grid-area: hd; }",
  '<div style="font-size:9px;background:#f0fdf4;border:1px solid #6ee7b7;padding:6px">grid-area: name | r1 c1 r2 c2</div>',
  "auto", ["grid-template-areas"])

p("grid-row", "Grid", "Spans grid rows (shorthand: row-start / row-end).",
  "grid-row: 1 / 3 → from line 1 to line 3 (2 rows). -1 = the last line. span 2 = current line +2.",
  [("start / end", "e.g. 1 / 3, 1 / -1, span 2.")],
  ".banner { grid-row: 1 / -1; }",
  '<div style="font-size:9px;background:#fdf4ff;border:1px solid #e879f9;padding:6px">grid-row: 1 / -1 → first line to last line (full height)</div>',
  "auto", ["grid-column"])

p("grid-column", "Grid", "Spans grid columns (shorthand: col-start / col-end).",
  "grid-column: 2 / 4 spans columns 2 and 3. The classic full-width item in a card grid: .featured { grid-column: 1 / -1; }.",
  [("start / end", "e.g. 1 / -1, 2 / span 2.")],
  ".hero { grid-column: 1 / -1; }",
  '<div style="font-size:9px"><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:4px;max-width:210px"><div style="background:#fecdd3;grid-column:1/-1;padding:4px;text-align:center">grid-column: 1 / -1 (spans all)</div><div style="background:#fecdd3;padding:4px">a</div><div style="background:#fecdd3;padding:4px">b</div></div></div>',
  "auto", ["grid-row"])

p("grid-template", "Grid", "Shorthand: grid-template-rows / grid-template-columns / grid-template-areas.",
  "grid-template: \"a b\" auto \"c c\" 1fr / 1fr 2fr; — areas, rows and columns in one line (rows, then /, then columns).",
  [("rows / columns (areas)", "Full shorthand.")],
  "grid-template: \"hd\" auto \"main\" 1fr / 1fr;",
  '<div style="font-size:9px;background:#eff6ff;border:1px solid #93c5fd;padding:6px">grid-template: rows / columns in one declaration.</div>',
  "none", ["grid-template-columns"])

p("grid-auto-columns", "Grid", "Size of implicitly created columns (when items overflow the template).",
  "When content creates more columns than the template defines, this sets their size: minmax(0, 1fr) is the safe default.",
  [("track size", "fr, length, minmax, auto.")],
  ".grid { grid-auto-columns: minmax(0, 1fr); }",
  '<div style="font-size:9px;background:#fefce8;border:1px solid #fde047;padding:6px">grid-auto-columns: minmax(0,1fr) → implicit columns share space safely.</div>',
  "auto", ["grid-auto-rows"])

p("grid-auto-rows", "Grid", "Size of implicitly created rows.",
  "grid-auto-rows: minmax(160px, auto) → equal-height card rows that grow with content.",
  [("track size", "fr, length, minmax, auto.")],
  ".cards { grid-auto-rows: minmax(180px, auto); }",
  '<div style="font-size:9px"><div style="display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:minmax(34px,auto);gap:4px;max-width:210px"><div style="background:#ddd6fe;padding:4px">short</div><div style="background:#ddd6fe;padding:4px">longer card that makes its row grow</div><div style="background:#ddd6fe;padding:4px">short</div></div></div>',
  "auto", ["grid-auto-columns"])

p("grid-auto-flow", "Grid", "How auto-placed items fill the grid (row, column, dense).",
  "row (default) fills left-to-right, top-to-bottom. column fills down first. dense back-fills earlier holes — better packing, but visual order can differ from source order.",
  [("row", "Default flow direction."),
   ("column", "Fill columns first."),
   ("dense", "Back-fill holes (row dense / column dense).")],
  ".masonry-ish { grid-auto-flow: dense; }",
  '<div style="font-size:9px;background:#f8fafc;border:1px solid #d1d5db;padding:6px">grid-auto-flow: dense → items jump back to fill gaps left by spanning items.</div>',
  "row", ["grid-auto-rows"])

p("place-items", "Grid & Flex", "Shorthand: align-items + justify-items (align every cell's content).",
  "place-items: center; centers every grid item inside its cell — two words instead of four properties. Works in flex too (justify-items is main-axis).",
  [("align justify", "e.g. center, start center, stretch.")],
  ".cell { place-items: center; }",
  '<div style="font-size:9px"><div style="display:grid;place-items:center;width:110px;height:44px;border:1px dashed #94a3b8"><span style="background:#99f6e4;padding:3px 8px">centered in its cell</span></div></div>',
  "normal normal", ["place-content", "place-self"])

p("place-content", "Grid & Flex", "Shorthand: align-content + justify-content (align the tracks themselves).",
  "Place the whole set of tracks in the container: place-content: center; centers the grid block inside a taller container.",
  [("align justify", "e.g. center, space-between, stretch.")],
  "body { place-content: center; min-height: 100vh; }",
  '<div style="font-size:9px"><div style="display:grid;place-content:center;height:70px;max-width:180px;border:1px dashed #94a3b8"><div style="display:flex;gap:4px"><span style="background:#fde047;padding:4px 10px">tracks centered</span></div></div></div>',
  "normal normal", ["place-items"])

p("place-self", "Grid & Flex", "Shorthand: align-self + justify-self (one item).",
  "place-self: end; = align-self:end + justify-self:end for that single item.",
  [("align justify", "e.g. end, center start.")],
  ".logo { place-self: start; }",
  '<div style="font-size:9px"><div style="display:grid;place-self:end;width:110px;height:44px;border:1px dashed #94a3b8"><span style="background:#fda4af;padding:3px 8px">bottom-right of its cell</span></div></div>',
  "auto auto", ["place-items"])

p("justify-items", "Grid & Flex", "Aligns grid items on the main (inline) axis inside their cells.",
  "start/center/end/stretch per item on the inline axis — the other half of the centering duo.",
  [("start / center / end / stretch", "Main-axis alignment.")],
  ".cell { justify-items: center; }",
  '<div style="font-size:9px"><div style="display:grid;justify-items:center;width:110px;height:40px;border:1px dashed #94a3b8"><span style="background:#bfdbfe;padding:3px 8px">main-axis centered</span></div></div>',
  "stretch", ["place-items"])

p("justify-self", "Grid & Flex", "Aligns one grid item on the main axis inside its cell.",
  "Per-item justify-items override.",
  [("auto / start / center / end / stretch", "Main-axis alignment.")],
  ".cta { justify-self: end; }",
  '<div style="font-size:9px"><div style="display:grid;width:110px;height:40px;border:1px dashed #94a3b8"><span style="justify-self:end;background:#bbf7d0;padding:3px 8px">justify-self:end</span></div></div>',
  "stretch", ["place-self"])
