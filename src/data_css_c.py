# -*- coding: utf-8 -*-
# CSS — Part C: Transitions & Animation, Transforms, plus Selectors, At-Rules & Value Keywords
from data_css_a import P, p  # noqa: F401
from data_css_b import P  # noqa

# ---------------- TRANSITIONS & ANIMATIONS ----------------
p("transition", "Motion",
  "Shorthand: property + duration + timing-function + delay.",
  "transition: all .3s ease; — animate property changes (hover, class toggles). 'all' animates anything that changes; naming the property is faster and safer. Comma-separate multiple.",
  [("property duration timing delay", "e.g. transform .25s ease-out, opacity .2s .1s.")],
  ".btn { transition: transform .2s ease, box-shadow .2s; }\n.btn:hover { transform: translateY(-2px); }",
  '<div style="font-size:11px;display:flex;gap:10px;align-items:center"><span style="display:inline-block;background:#2563eb;color:#fff;padding:8px 14px;border-radius:8px;transition:transform .25s,box-shadow .25s">hover me (transition)</span><code style="font-size:10px;color:#6b7280">transition: transform .25s, box-shadow .25s</code></div>',
  "all 0s ease 0s", ["animation", "transform", "opacity"])

p("transition-property", "Motion", "Which properties transition (list).",
  "none (default), all, or a named list: transition-property: width, background-color;",
  [("property list", "e.g. transform, opacity.")],
  "a { transition-property: color, border-color; }",
  '<div style="font-size:11px;color:#4b5563">transition-property: transform, opacity — only these animate.</div>',
  "all", ["transition"])

p("transition-duration", "Motion", "How long the transition takes (s or ms).",
  "UI sweet spot: 150–300ms for micro-interactions, up to ~600ms for page-level moves.",
  [("time", "e.g. .2s, 300ms.")],
  ".panel { transition-duration: .3s; }",
  '<div style="font-size:11px;color:#4b5563">transition-duration: .3s — a 300 ms animation.</div>',
  "0s", ["transition"])

p("transition-timing-function", "Motion", "The speed curve of the transition (ease, cubic-bezier…).",
  "ease (default), linear, ease-in, ease-out (the most natural for entrances), ease-in-out, steps(n), cubic-bezier(x1,y1,x2,y2).",
  [("keyword", "linear|ease|ease-in|ease-out|ease-in-out|step-start|step-end|steps(n,jump)."),
   ("cubic-bezier()", "Custom curve, e.g. cubic-bezier(.2,.8,.2,1).")],
  ".toast { transition-timing-function: cubic-bezier(.2,.9,.3,1.2); }",
  '<div style="font-size:11px;display:flex;gap:14px;color:#4b5563"><span>linear ▬▬▬</span><span>ease-out ▂▅▇ (fast start)</span><span>ease-in ▁▃▅ (slow start)</span></div>',
  "ease", ["transition", "cubic-bezier()"])

p("transition-delay", "Motion", "Wait this long before the transition starts.",
  "Stagger lists: .item:nth-child(2) { transition-delay: .05s; } — or per-value in the shorthand.",
  [("time", "e.g. .1s, 0s.")],
  ".fade li { transition-delay: calc(var(--i) * 60ms); }",
  '<div style="font-size:11px;color:#4b5563">transition-delay: .1s → the change starts after 100 ms (stagger tricks).</div>',
  "0s", ["transition"])

p("animation", "Motion",
  "Shorthand: name + duration + timing + delay + iteration + direction + fill-mode + play-state.",
  "animation: pop .3s ease forwards; runs a @keyframes timeline on load/toggle. Unlike transitions, it plays without any property change — and can loop, reverse, and fill.",
  [("name duration timing delay count direction fill play", "e.g. spin 2s linear infinite.")],
  "@keyframes spin { to { transform: rotate(1turn); } }\n.loader { animation: spin 1s linear infinite; }",
  '<div style="font-size:11px;display:flex;gap:10px;align-items:center"><span style="display:inline-block;width:16px;height:16px;border:3px solid #e5e7eb;border-top-color:#2563eb;border-radius:50%;animation:mb_spin 1s linear infinite"></span><style>@keyframes mb_spin{to{transform:rotate(1turn)}}</style><code style="font-size:10px;color:#6b7280">animation: spin 1s linear infinite</code></div>',
  "none", ["@keyframes", "transition"])

p("animation-name", "Motion", "The @keyframes block to run.",
  "none stops any running animation.",
  [("keyframe name", "e.g. pop, slide-in.")],
  ".card { animation-name: fade-in-up; }",
  '<div style="font-size:11px;color:#4b5563">animation-name: fade-in-up → runs the @keyframes named fade-in-up.</div>',
  "none", ["animation", "@keyframes"])

p("animation-duration", "Motion", "One cycle's length.",
  "Loaders: ~1s; entrances: 300–500ms; ambient: several seconds.",
  [("time", "e.g. 1s, .4s.")],
  ".hero { animation-duration: .6s; }",
  '<div style="font-size:11px;color:#4b5563">animation-duration: 1s — each cycle takes a second.</div>',
  "0s", ["animation"])

p("animation-timing-function", "Motion", "Speed curve per keyframe segment.",
  "Applies between each pair of keyframes (each segment can override with its own timing).",
  [("keyword / cubic-bezier()", "As transition-timing-function.")],
  ".bounce { animation-timing-function: cubic-bezier(.34,1.56,.64,1); }",
  '<div style="font-size:11px;color:#4b5563">animation-timing-function: cubic-bezier(.34,1.56,.64,1) → an overshoot bounce.</div>',
  "ease", ["animation"])

p("animation-delay", "Motion", "Delay before the first cycle starts.",
  "Negative delay starts the animation mid-way (great for desyncing repeated elements: .bar:nth-child(n) { animation-delay: calc(-1s * n / 3); }).",
  [("time", "e.g. .2s, -0.5s.")],
  ".stagger > * { animation-delay: calc(var(--i) * 80ms); }",
  '<div style="font-size:11px;color:#4b5563">animation-delay: -0.5s → starts halfway through (desync trick).</div>',
  "0s", ["animation"])

p("animation-iteration-count", "Motion", "How many times it loops (infinite = forever).",
  "1 (default) = once. infinite for loaders/ambient motion. Respect prefers-reduced-motion for infinite ones!",
  [("number | infinite", "e.g. 3, infinite.")],
  ".loader { animation-iteration-count: infinite; }",
  '<div style="font-size:11px;color:#4b5563">animation-iteration-count: infinite → loops forever (mind reduced-motion users).</div>',
  "1", ["animation"])

p("animation-direction", "Motion", "Forward / reverse / alternate playback.",
  "normal (forward), reverse, alternate (ping-pong: 1→2→1→2), alternate-reverse.",
  [("normal / reverse / alternate / alternate-reverse", "Playback direction.")],
  ".float { animation-direction: alternate; }",
  '<div style="font-size:11px;color:#4b5563">animation-direction: alternate → plays forward, then backward, forever.</div>',
  "normal", ["animation"])

p("animation-fill-mode", "Motion", "Which styles apply before start / after end.",
  "backwards: apply the 0% frame during the delay. forwards: keep the final frame after finishing (the classic fix for 'it snaps back'). both = backwards + forwards.",
  [("none", "Default — no extra frames."),
   ("forwards", "Hold the last keyframe."),
   ("backwards", "Apply the first keyframe during delay."),
   ("both", "Both.")],
  ".entrance { animation-fill-mode: both; }",
  '<div style="font-size:11px;color:#4b5563">animation-fill-mode: forwards → the element stays in its final state instead of snapping back.</div>',
  "none", ["animation"])

p("animation-play-state", "Motion", "Pause or resume a running animation.",
  "paused / running. The classic: .tooltip:hover .arrow { animation-play-state: running; }",
  [("running", "Default."),
   ("paused", "Frozen at the current frame.")],
  ".marquee { animation-play-state: paused; }\n.marquee:hover { animation-play-state: running; }",
  '<div style="font-size:11px;color:#4b5563">animation-play-state: paused → the timeline freezes (hover-to-pause pattern).</div>',
  "running", ["animation"])

p("animation-timeline", "Scroll-driven", "Drive an animation from a scroll position (new).",
  "animation-timeline: scroll(); or view() → the element's visibility progress. Scroll-linked animation with zero JS. Check support (Chrome/Edge; others behind flags).",
  [("scroll() / view() / scroll(axis) / view(block|inline)", "Timeline sources.")],
  ".progress { animation: grow linear; animation-timeline: scroll(); }",
  '<div style="font-size:11px;background:#f0f9ff;border:1px solid #7dd3fc;padding:8px;border-radius:6px">animation-timeline: scroll() → animation progress = scroll progress (no JS).</div>',
  "auto", ["animation"])

p("view-timeline", "Scroll-driven", "Name a view-timeline for descendants (new).",
  "view-timeline-name: --card; + animation-timeline: --card; on a child → children animate as the parent moves through the viewport.",
  [("timeline name", "--custom-name.")],
  ".card { view-timeline: --card block; }",
  '<div style="font-size:11px;background:#eff6ff;border:1px solid #93c5fd;padding:8px;border-radius:6px">view-timeline: --card → descendants can animate against this element\'s viewport progress.</div>',
  "auto", ["animation-timeline"])

p("animation-range", "Scroll-driven", "Which part of the timeline the animation plays in (new).",
  "animation-range: entry 0% entry 100%; — play while the element enters the viewport (ranges: cover, contain, entry, exit + % offsets).",
  [("range start / end", "e.g. entry, exit 50%, cover 0% cover 100%.")],
  ".reveal { animation-range: entry 0% entry 100%; }",
  '<div style="font-size:11px;background:#fdf4ff;border:1px solid #e9d5ff;padding:8px;border-radius:6px">animation-range: entry 0% entry 100% → animate while entering the viewport.</div>',
  "auto", ["animation-timeline"])

# ---------------- TRANSFORMS ----------------
p("transform", "Motion & 3D",
  "Move/rotate/scale/skew the element (GPU-friendly, doesn't reflow).",
  "Functions chain in order: transform: translateX(20px) rotate(45deg) scale(1.1). The classic hover lift: transform: translateY(-4px) scale(1.02);. 2D + 3D functions (translate3d for layer promotion).",
  [("function list", "translate(x,y) translateX/Y, rotate(deg) rotateX/Y/Z, scale(x,y) scale3d, skewX/Y(deg), matrix(a,b,c,d,e,f), matrix3d(…), perspective(d)."),
   ("none", "No transform (default).")],
  ".card:hover { transform: translateY(-4px); }\n.spin { transform: rotate(45deg); }",
  '<div style="display:flex;gap:12px;font-size:10px;align-items:center;flex-wrap:wrap"><span style="display:inline-block;padding:8px 12px;background:#60a5fa;color:#fff;border-radius:6px;transform:translateY(-6px)">translateY(-6px)</span><span style="display:inline-block;padding:8px 12px;background:#f472b6;color:#fff;border-radius:6px;transform:rotate(6deg)">rotate(6deg)</span><span style="display:inline-block;padding:8px 12px;background:#34d399;color:#fff;border-radius:6px;transform:scale(1.15)">scale(1.15)</span><span style="display:inline-block;padding:8px 12px;background:#fbbf24;color:#fff;border-radius:6px;transform:skewX(-12deg)">skewX(-12°)</span></div>',
  "none", ["transform-origin", "transition", "will-change"])

p("transform-origin", "Motion & 3D", "The point transforms rotate/scale around.",
  "Default: center. transform-origin: top left; rotates from the corner; transform-origin: 50% 0; from top-center (the swinging-door effect).",
  [("x y", "Lengths, %, or keywords: center, top left…")],
  ".pendulum { transform-origin: top center; }",
  '<div style="font-size:10px;display:flex;gap:14px;align-items:flex-start"><div style="position:relative;width:40px;height:60px;border-top:3px solid #ef4444"><div style="position:absolute;top:0;left:18px;width:6px;height:52px;background:#fca5a5;transform:rotate(20deg);transform-origin:top center"></div></div><div style="position:relative;width:40px;height:60px"><div style="position:absolute;top:0;left:8px;width:6px;height:52px;background:#93c5fd;transform:rotate(20deg);transform-origin:bottom center"></div></div><span>origin: top vs bottom</span></div>',
  "50% 50% 0", ["transform"])

p("transform-box", "Motion & 3D", "Which box the transform coordinates use (content-box / border-box / fill-box / view-box).",
  "For SVG: fill-box makes percentages/origin relative to the element's own box (the fix for 'my SVG rotates around the page corner').",
  [("content-box / border-box / fill-box / stroke-box / view-box", "The reference box.")],
  ".icon { transform-box: fill-box; transform-origin: center; }",
  '<div style="font-size:11px;color:#4b5563">transform-box: fill-box → transform-origin:center means the center of THIS svg element.</div>',
  "view-box", ["transform-origin"])

p("translate", "Motion & 3D", "Independent translate (composes with transform).",
  "translate: 10px; / translate: 0 -50%; — combines with transform without overwriting it (transform: rotate(…) + translate: …).",
  [("x y z", "Lengths/%.")],
  ".toast { translate: 0 -20px; opacity: 0; }\n.toast.show { translate: 0 0; opacity: 1; transition: .3s; }",
  '<div style="font-size:10px"><span style="display:inline-block;padding:6px 10px;background:#a78bfa;color:#fff;border-radius:6px">normal</span><span style="display:inline-block;padding:6px 10px;background:#7c3aed;color:#fff;border-radius:6px;translate:0 6px">translate: 0 6px (composed)</span></div>',
  "none", ["transform"])

p("rotate", "Motion & 3D", "Independent rotate (composes with transform).",
  "rotate: 45deg; (or x y z axes: rotate: 0 0 45deg).",
  [("angle | x y z", "e.g. 45deg, y 180deg.")],
  ".badge { rotate: -8deg; }",
  '<div style="font-size:10px"><span style="display:inline-block;padding:6px 10px;background:#fb923c;color:#fff;border-radius:6px;rotate:-6deg">rotate: -6deg</span></div>',
  "none", ["transform"])

p("scale", "Motion & 3D", "Independent scale (composes with transform).",
  "scale: 1.1; or scale: 1.2 0.9; (x, y).",
  [("x | x y", "Factors (1 = unchanged).")],
  ".zoom:hover { scale: 1.05; }",
  '<div style="font-size:10px"><span style="display:inline-block;padding:6px 10px;background:#2dd4bf;color:#fff;border-radius:6px">1</span><span style="display:inline-block;padding:6px 10px;background:#0d9488;color:#fff;border-radius:6px;scale:1.2">scale:1.2</span></div>',
  "none", ["transform"])

p("perspective-origin", "Motion & 3D", "Where the vanishing point sits (x y).",
  "perspective-origin: center 20%; shifts the 3D horizon.",
  [("x y", "Lengths/%/keywords.")],
  ".scene { perspective-origin: center 30%; }",
  '<div style="font-size:11px;color:#4b5563">perspective-origin: center 30% → the 3D horizon moves up.</div>',
  "50% 50%", ["perspective"])

p("offset-path", "Motion & 3D", "Move the element along an SVG path (motion path).",
  "offset-path: path(\"M0,50 C50,0 150,100 200,50\"); + offset-distance: 0%→100% animated = a dot traveling a curve (no JS).",
  [("path(…)", "SVG path data."),
   ("ray()/inset()/rect()/circle()", "Shape paths.")],
  "@keyframes travel { to { offset-distance: 100%; } }\n.dot { offset-path: path(\"M0 50 Q 100 0 200 50\"); animation: travel 2s linear infinite alternate; }",
  '<div style="font-size:11px;color:#4b5563">offset-path: path(…) + offset-distance animation → an element travels a curve (pure CSS motion path).</div>',
  "none", ["offset-distance", "transform"])

p("offset-distance", "Motion & 3D", "Position along the offset-path (0%–100%).",
  "offset-distance: 50% = halfway along the path. Animate it for travel effects.",
  [("percentage", "Along the path.")],
  ".comet { offset-distance: 50%; }",
  '<div style="font-size:11px;color:#4b5563">offset-distance: 50% → sits at the middle of its path.</div>',
  "0%", ["offset-path"])

p("offset-rotate", "Motion & 3D", "Rotation of the element relative to the path (auto follows the tangent).",
  "auto (default with offset-path) rotates the element to follow the curve; 0deg keeps it upright.",
  [("auto | angle", "auto = along the path tangent.")],
  ".train { offset-rotate: auto; }",
  '<div style="font-size:11px;color:#4b5563">offset-rotate: auto → the element turns to follow the path direction.</div>',
  "auto", ["offset-path"])

# ---------------- CSS SELECTORS ----------------
SEL = []
def sel(name, kind, s, d, ex, dm):
    SEL.append(dict(n=name, k=kind, s=s, d=d, ex=ex, dm=dm))

sel("*", "Universal", "Matches every element.", "The starting point of universal resets: * { margin:0; box-sizing:border-box; } — prefer scoping over raw * in large apps.", "* { box-sizing: border-box; }", '<div style="font-size:11px">* matches ALL elements (div, p, span…).</div>')
sel("element", "Type selector", "Matches by tag name (p, a, h1…).", "p { color: #333; } — the most basic selector. Specificity: 0,0,1.", "a { color: #2563eb; }", '<a href="#" style="color:#2563eb">a { color: blue; }</a>')
sel(".class", "Class selector", "Matches by class attribute (the workhorse).", ".card { … } — one element can hold many classes. Specificity: 0,1,0. Use multiple: .card.dark.", ".btn { display:inline-block; }", '<span class="demo" style="border:1px solid #d1d5db;padding:4px 8px;font-size:11px">.btn → matches this span</span>')
sel("#id", "ID selector", "Matches by unique id.", "#hero { … } — ids must be unique; prefer classes for styling (ids are for anchors/JS). Specificity: 1,0,0 — often too strong.", "#nav { position: sticky; }", '<div id="x" style="border:1px solid #d1d5db;padding:4px 8px;font-size:11px">#x matches this div</div>')
sel("[attr]", "Attribute selector", "Matches elements that HAVE the attribute.", "[disabled] { opacity:.5; } — select any element with the attribute, regardless of value.", "input[required]::after { content: \"*\"; }", '<div style="font-size:11px">[required] → any input carrying the required attribute</div>')
sel("[attr=value]", "Attribute = ", "Matches when the attribute equals a value (exact, case-sensitive).", "[type=\"submit\"] { background: blue; } — also how you target form controls.", "img[alt=\"\"] { outline: 2px solid red; }", '<div style="font-size:11px">[type="submit"] → only submit buttons</div>')
sel("[attr^=…]", "Attribute starts with", "The value starts with the string.", "[href^=\"https://\"] a → external links only. Great for icons.", "a[href^=\"https://\"]::after { content: \" ↗\"; }", '<div style="font-size:11px">[href^="https://"] → external links (icon/behavior per origin)</div>')
sel("[attr$=…]", "Attribute ends with", "The value ends with the string.", "[href$=\".pdf\"] → PDF links. [href$=\".png\"] → png images.", "a[href$=\".pdf\"]::after { content: \" (PDF)\"; }", '<div style="font-size:11px">[href$=".pdf"] → file-type detection</div>')
sel("[attr*=…]", "Attribute contains", "The value contains the substring.", "[id*=\"gallery\"] → any id containing 'gallery'.", ".tile[data-icon*=\"heart\"] { … }", '<div style="font-size:11px">[id*=\"gallery\"] → substring match</div>')
sel(":", "Pseudo-class (state)", "Matches an element in a state.", "The : family targets states: :hover, :focus, :first-child… (full list below).", "li:hover { background: #f3f4f6; }", '<div style="font-size:11px;padding:4px 8px;border:1px solid #d1d5db">li:hover — style by STATE</div>')
sel(":hover", "State", "The element is under the pointer.", "a:hover { color: darker; } — the classic interactive feedback.", ".card:hover { transform: translateY(-2px); }", '<span style="border:1px solid #2563eb;padding:4px 10px;font-size:11px">hover over me</span>')
sel(":focus", "State", "The element has keyboard/click focus.", "Always style :focus (a11y): input:focus { outline: 2px solid #2563eb; }.", "input:focus { border-color: #2563eb; }", '<input style="border:1px solid #2563eb;border-radius:6px;padding:4px 8px;font-size:11px" placeholder="click me → :focus">')
sel(":focus-visible", "State", "Focus via keyboard (not mouse click).", "The modern focus-ring standard: only show rings when they help: a:focus-visible { outline: 2px solid; }.", ":focus-visible { outline: 3px solid #2563eb; }", '<div style="font-size:11px">Tab through the page: :focus-visible fires for keyboard users.</div>')
sel(":active", "State", "The element is being pressed/clicked.", "button:active { transform: scale(.97); } — press feedback.", ".btn:active { transform: translateY(1px); }", '<span style="border:1px solid #d1d5db;padding:4px 10px;font-size:11px">press and hold me (:active)</span>')
sel(":first-child", "Structural", "First child of its parent.", "ul li:first-child { margin-top: 0; } — remove the top margin on the first item.", "h1, h2 { margin-top: 0; } /* or */ li:first-child { … }", '<div style="font-size:11px"><b>first-child:</b> this box (the only first child of its parent)</div>')
sel(":last-child", "Structural", "Last child of its parent.", "li:last-child { border-bottom: none; } — remove separators on the last item.", ".list li:last-child { border: 0; margin: 0; }", '<div style="font-size:11px"><b>last-child:</b> the final element in its parent</div>')
sel(":only-child", "Structural", "The sole child of its parent.", "article:only-child { margin-inline: auto; }", ":only-child { … }", '<div style="font-size:11px"><b>only-child:</b> a parent with exactly one child</div>')
sel(":nth-child(n)", "Structural", "The n-th child (An+B formulas).", "Zebra stripes: tr:nth-child(even) { background: #f9fafb; }. :nth-child(3n) every third. :nth-child(-n+3) first three. :nth-child(2n+1) odd.", "tbody tr:nth-child(even) { background: #f8fafc; }", '<table style="font-size:11px;border-collapse:collapse"><tr><td style="border:1px solid #e5e7eb;padding:3px 8px">1</td></tr><tr><td style="border:1px solid #e5e7eb;padding:3px 8px;background:#eef2ff">2 (even)</td></tr><tr><td style="border:1px solid #e5e7eb;padding:3px 8px">3</td></tr><tr><td style="border:1px solid #e5e7eb;padding:3px 8px;background:#eef2ff">4 (even)</td></tr></table>')
sel(":nth-of-type(n)", "Structural", "The n-th child OF ITS TAG type (ignores other tags).", "p:nth-of-type(2) → second <p>, even if spans sit between.", "h2:nth-of-type(2) { … }", '<div style="font-size:11px">p:nth-of-type(2) → counts only &lt;p&gt; siblings</div>')
sel(":first-of-type", "Structural", "First of its tag among siblings.", "p:first-of-type { margin-top: 0; }", ":first-of-type { … }", '<div style="font-size:11px">the first &lt;p&gt; inside its parent</div>')
sel(":last-of-type", "Structural", "Last of its tag among siblings.", ":last-of-type { margin-bottom: 0; }", "", '<div style="font-size:11px">the last &lt;p&gt; inside its parent</div>')
sel(":empty", "Structural", "No children at all (not even text).", "ul:empty::after { content: \"Nothing here\"; }", ".folder:empty { … }", '<div style="font-size:11px">:empty matches elements with zero children</div>')
sel(":not(sel)", "Logical", "Everything EXCEPT the selector inside.", "li:not(.active) { color: gray; } — invert a selection. :not accepts complex lists since 2023.", "*:not(:focus) { … }", '<div style="font-size:11px">p:not(.lead) → every paragraph that is NOT .lead</div>')
sel(":is(sel, …)", "Logical", "Matches if ANY listed selector matches (zero specificity!).", ".is(.btn, .link) → the lower-specificity version of the \"or\". Replaces the old :any().", ":is(a, button):hover { … }", '<div style="font-size:11px">:is(a, button) → either one, with minimal specificity</div>')
sel(":where(sel, …)", "Logical", "Like :is but with ZERO specificity.", "Reset without fighting specificity: :where(p, h1, h2) { margin: 0; }", ":where(header, footer) a { color: white; }", '<div style="font-size:11px">:where(…) adds no specificity — the reset-friendly :is</div>')
sel(":has(sel)", "Logical", "Parent selector! Matches if it CONTAINS the selector.", "The long-awaited :has — .card:has(img) { border: … }, form:has(:invalid) button:submit { disabled look }.", "li:has(ul) { padding-left: 12px; }", '<div style="font-size:11px">.card:has(img) → cards that contain an image</div>')
sel(":checked", "Form state", "Checkbox/radio is checked.", "Pure-CSS tabs & toggles: input:checked + label { … }, input:checked ~ .panel { display:block; }", "#tab1:checked ~ .panels .p1 { display: block; }", '<label style="font-size:11px"><input type="checkbox" checked> :checked drives CSS-only toggles</label>')
sel(":enabled / :disabled", "Form state", "Form control usable or not.", "button:disabled { opacity: .5; cursor: not-allowed; }", "input:disabled { background: #f3f4f6; }", '<button disabled style="opacity:.5;border:1px solid #d1d5db;padding:4px 10px;font-size:11px">:disabled button</button>')
sel(":required / :optional", "Form state", "Field required or not.", "label the required: input:required + ::after { content: \" *\"; color: red; }", "input:required::after { content: \" *\"; }", '<div style="font-size:11px">input:required → mark mandatory fields</div>')
sel(":valid / :invalid", "Form state", "Value passes / fails validation.", "Live feedback: input:valid { border-color: green; } input:invalid { border-color: red; } (only when filled — combine with :not(:placeholder-shown)).", "input:invalid:not(:placeholder-shown) { border-color: #ef4444; }", '<div style="font-size:11px">:valid / :invalid → style by constraint validation</div>')
sel(":placeholder-shown", "Form state", "The placeholder is currently visible (field empty).", "Grow labels, style empty states: input::placeholder { … } + :placeholder-shown.", "input:placeholder-shown + .label { … }", '<div style="font-size:11px">:placeholder-shown → the input is empty</div>')
sel(":in-range / :out-of-range", "Form state", "Number input within / outside min-max.", "input[type=number]:in-range { border-color: green; }", "input:out-of-range { border-color: #f59e0b; }", '<div style="font-size:11px">:in-range → value between min and max</div>')
sel(":target", "State", "The element is the target of the URL fragment (#id).", ":target { scroll-margin-top: 80px; } + highlight the section the user jumped to.", "section:target { border-left: 4px solid #2563eb; }", '<div style="font-size:11px">section:target → highlighted when the URL is #that-id</div>')
sel(":lang(code)", "Language", "Element's language matches the code.", ":lang(ar) { font-family: …; direction: rtl; }", "p:lang(fr) { … }", '<div style="font-size:11px">:lang(ar) → Arabic text gets the right font/direction</div>')
sel(":dir(dir)", "Direction", "Element's text direction matches.", ":dir(rtl) .arrow { transform: scaleX(-1); }", "button:dir(rtl) { … }", '<div style="font-size:11px">:dir(rtl) → flip icons for RTL</div>')
sel(">", "Combinator: child", "Direct children only.", "ul > li { … } — li directly inside ul (not deeper). Specificity: 0,0,1.", "nav > ul > li { display: inline; }", '<div style="font-size:11px">ul &gt; li → only the direct children</div>')
sel("descendant (space)", "Combinator: descendant", "Any depth descendant.", "article p { … } — every p inside article, however deep. (The default when you separate selectors by a space.)", ".card p { color: #555; }", '<div style="font-size:11px">.card p → any descendant &lt;p&gt; (all depths)</div>')
sel("+", "Combinator: adjacent sibling", "The NEXT sibling, immediately after.", "h2 + p { margin-top: 0; } — the first paragraph after a heading. The pure-CSS toggle glue: input + label.", "label + input { margin-left: 8px; }", '<div style="font-size:11px">h2 + p → ONLY the immediately following sibling</div>')
sel("~", "Combinator: general sibling", "ALL following siblings.", ".error ~ input { border-color: red; } — every input after the error message.", "h2 ~ p { … }", '<div style="font-size:11px">.msg ~ input → every later sibling input</div>')
sel("::before", "Pseudo-element", "Generated content INSIDE the start of the element.", "content + styling = icons, decorations, layouts (the clearfix!).", ".chip::before { content: \"● \"; color: green; }", '<div style="font-size:11px"><span style="border:1px solid #d1d5db;padding:3px 8px">chip</span> with ::before { content: \"● \" }</div>')
sel("::after", "Pseudo-element", "Generated content INSIDE the end of the element.", "Arrows (a::after { content:\"→\" }), underlines, the classic clearfix: .wrap::after { content:\"\"; display:block; clear:both; }.", "a::after { content: \" ↗\"; }", '<div style="font-size:11px">text with ::after { content: \" →\" }</div>')
sel("::first-letter", "Pseudo-element", "The very first letter of a block.", "Drop caps: p::first-letter { font-size: 3em; float: left; }", "p:first-of-type::first-letter { font-size: 2.5em; }", '<p style="font-size:13px;max-width:200px;margin:0"><span style="float:left;font-size:3em;line-height:.9;font-weight:800;margin-right:6px">F</span>irst letter via ::first-letter</p>')
sel("::first-line", "Pseudo-element", "The first line of a block.", "p::first-line { font-weight: bold; } — only the first line's styles apply.", "p::first-line { color: #111; font-weight: 600; }", '<p style="font-size:12px;max-width:200px;margin:0"><span style="font-weight:700">The first line can carry its own styles</span> while the rest stays normal in this paragraph box.</p>')
sel("::selection", "Pseudo-element", "The user's text selection.", "Customize the selection color (a brand touch): ::selection { background: #2563eb; color: #fff; }", "::selection { background: #2563eb; color: #fff; }", '<div style="font-size:12px">select some of this text to see ::selection</div>')
sel("::placeholder", "Pseudo-element", "The placeholder text inside inputs.", "input::placeholder { color: #9ca3af; } (Safari: ::-webkit-input-placeholder).", "input::placeholder { color: #94a3b8; font-style: italic; }", '<input placeholder="::placeholder styles this hint" style="border:1px solid #d1d5db;border-radius:6px;padding:4px 8px;font-size:11px">')
sel("::marker", "Pseudo-element", "The list bullet/number marker.", "ul li::marker { color: #2563eb; content: \"▶ \"; } — style or replace markers.", "li::marker { color: teal; }", '<ul style="font-size:12px;padding-left:18px"><li style="--m:teal">::marker colored teal</li><li>normal marker</li></ul>')
sel("::backdrop", "Pseudo-element", "The dim layer behind an open <dialog>.showModal().", "dialog::backdrop { background: rgba(0,0,0,.5); }", "dialog::backdrop { backdrop-filter: blur(2px); }", '<div style="font-size:11px;background:rgba(0,0,0,.08);padding:8px;border-radius:6px">dialog::backdrop → the dimmed area behind the dialog</div>')
sel("::file-selector-button", "Pseudo-element", "The button part of <input type=\"file\">.", "Restyle the default file button: input[type=file]::file-selector-button { … }", "input[type=file]::file-selector-button { background: #2563eb; color: #fff; }", '<div style="font-size:11px">input[type=file] → its button half is ::file-selector-button</div>')
sel("::cue", "Pseudo-element", "The text cues of media <track> subtitles.", "video::cue { background: #0008; color: #fff; font-size: 14px; }", "::cue { color: #ffd700; }", '<div style="font-size:11px">video::cue → style the subtitle text of media tracks</div>')

# ---------------- AT-RULES ----------------
ATR = []
def atr(name, s, d, ex, note=""):
    ATR.append(dict(n=name, s=s, d=d, ex=ex, note=note))

atr("@media", "Apply CSS when a condition matches (screen size, color scheme, print…).",
    "The responsive-design engine: @media (max-width: 600px) { … }, (prefers-color-scheme: dark), (prefers-reduced-motion), (orientation: portrait), (min-width: 1024px) and (max-width: 1279px). Mobile-first: base = small, min-width queries add up.",
    "@media (max-width: 768px) {\n  .grid { grid-template-columns: 1fr; }\n}\n@media (prefers-color-scheme: dark) { :root { --bg: #111; } }")
atr("@supports", "Feature query: apply only when a property/value is supported.",
    "@supports (display: grid) { … } — progressive enhancement without fallback soup. Test any declaration: @supports (aspect-ratio: 1).",
    "@supports (gap: 1px) {\n  .flex { gap: 16px; }\n}")
atr("@container", "Container query: style by the PARENT's size, not the viewport.",
    "The component-responsive era: @container (min-width: 400px) { .card { … } } — the card adapts to its container wherever it lives. Needs container-type on the parent.",
    "@container sidebar (min-width: 320px) {\n  .widget { grid-template-columns: 1fr 1fr; }\n}")
atr("@layer", "CSS cascade layers: control which rules win by layer order.",
    "@layer reset, components, utilities; — later layers win regardless of source order. The clean fix for 'my override gets eaten' without !important.",
    "@layer base { h1 { font-size: 2rem; } }\n@layer app { h1 { font-size: 1.5rem; } } /* wins */")
atr("@keyframes", "Define the animation timeline (from/to or %).",
    "The building block of animation: @keyframes name { 0% {…} 50% {…} 100% {…} } (from/to sugar). Animate transform/opacity (GPU), not top/left (layout).",
    "@keyframes fade-in-up {\n  from { opacity: 0; transform: translateY(12px); }\n  to   { opacity: 1; transform: none; }\n}")
atr("@font-face", "Register a custom font family.",
    "Declare a font file: @font-face { font-family: \"MyFont\"; src: url(f.woff2) format(\"woff2\"); font-weight: 100 900; font-display: swap; } — then use font-family: \"MyFont\". woff2 first, preconnect to the font host.",
    "@font-face {\n  font-family: \"Inter\";\n  src: url(inter.woff2) format(\"woff2\");\n  font-weight: 100 900;\n  font-display: swap;\n}")
atr("@import", "Import another stylesheet (usually at the top of the first one).",
    "@import url(themes/dark.css); — blocks rendering until fetched: prefer <link> in production; @import is fine for small dev setups.",
    "@import url(\"base.css\");\n@import url(\"theme.css\") (prefers-color-scheme: dark);")
atr("@charset", "Declare the stylesheet's character set (first rule only).",
    "@charset \"utf-8\"; — required in external files with non-ASCII characters when the server/encoding is ambiguous. HTML-embedded CSS takes charset from the document.",
    "@charset \"utf-8\";")
atr("@namespace", "XML namespaces (XSLT era; ignored in HTML CSS).",
    "@namespace svg url(\"http://www.w3.org/2000/svg\"); — mostly historical; inline SVG in HTML needs no namespaces.",
    "@namespace svg url(\"http://www.w3.org/2000/svg\");")
atr("@property", "Register a custom property (type, initial, inherits) → animate it!",
    "@property --angle { syntax: \"<angle>\"; initial-value: 0deg; inherits: false; } — now transition/animation can interpolate --angle (conic-gradient spinners, hover glows).",
    "@property --a { syntax: \"<angle>\"; initial-value: 0deg; }\n.ring { transition: --a .5s; }")
atr("@view-transition", "Name a view-transition pair (new).",
    "View Transitions API: @view-transition { navigation: auto; } lets same-document navigation animate between old and new snapshots. Progressive: check support.",
    "@view-transition {\n  navigation: auto;\n}")

# ---------------- VALUE KEYWORDS & FUNCTIONS ----------------
VAL = []
def val(name, s, d, ex, dm=""):
    VAL.append(dict(n=name, s=s, d=d, ex=ex, dm=dm))

val("calc()", "Math on lengths/values.", "calc(100% - 40px) — the mixed-unit math engine: 100vw minus scrollbar, padding + gap, etc. Spaces around + and - are required.", ".hero { height: calc(100vh - 64px); }", '<div style="font-size:11px;background:#f0f9ff;padding:6px;border:1px solid #7dd3fc;border-radius:4px">calc(100vw - 40px) → math with mixed units</div>')
val("var() / custom properties", "CSS variables: --name: value; var(--name, fallback).", "Define once, theme everywhere: :root { --brand: #2563eb; } … color: var(--brand);. var(--x, #333) supplies a fallback.", ".btn { background: var(--brand, #2563eb); }", '<div style="font-size:11px;color:#1e40af">var(--brand, #2563eb) → theming tokens + fallbacks</div>')
val("min() / max() / clamp()", "Bound values responsively without media queries.", "clamp(MIN, PREF, MAX): fluid type & spacing: font-size: clamp(1rem, .5rem + 2vw, 2rem); min()/max() pick one side.", ".h { font-size: clamp(1.5rem, 1rem + 2vw, 3rem); }", '<div style="font-size:clamp(14px, 4vw, 22px);font-weight:700">clamp(14px, 4vw, 22px) — fluid between bounds</div>')
val("rgb() / rgba()", "Colors by red/green/blue channels.", "rgb(37 99 235) — modern syntax with spaces; rgb(37 99 235 / .5) or rgba(37,99,235,.5) for alpha. 8-digit hex #2563eb80 works too.", ".link { color: rgb(37 99 235); }", '<div style="font-size:11px;color:rgb(37 99 235)">rgb(37 99 235) — channel-based color</div>')
val("hsl() / hsla()", "Colors by hue/saturation/lightness (intuitive).", "hsl(217 91% 60%) = that blue. Rotate themes with hue-rotate or calc on hue. / for alpha: hsl(217 91% 60% / .5).", ".accent { background: hsl(160 84% 39%); }", '<div style="font-size:11px;color:hsl(217 91% 45%)">hsl(217 91% 60%) — hue-based color</div>')
val("oklch() / lab()", "Perceptual color spaces (modern).", "oklch(L C H): lightness, chroma, hue — equal perceptual steps (a 10-step lightness ramp looks uniform). The future of design tokens.", ".btn { background: oklch(0.6 0.2 250); }", '<div style="font-size:11px;color:#2563eb">oklch(0.6 0.2 250) — perceptually uniform color</div>')
val("color-mix()", "Mix two colors (and more) in a color space.", "color-mix(in srgb, var(--brand) 10%, white) → a 10% tint. Design tokens without a build step: --bg-soft: color-mix(in oklab, var(--brand) 8%, white).", ".chip { background: color-mix(in srgb, var(--brand) 12%, white); }", '<div style="font-size:11px;background:color-mix(in srgb,#2563eb 12%,white);padding:6px;border-radius:6px">color-mix(in srgb, blue 12%, white)</div>')
val("linear-gradient()", "A straight color ramp (angle or direction).", "linear-gradient(135deg, #4285f4, #34a853) — the workhorse background: hero sections, buttons, text fills (with background-clip: text).", ".hero { background: linear-gradient(135deg, #6366f1, #ec4899); }", '<div style="background:linear-gradient(135deg,#6366f1,#ec4899);font-size:11px;color:#fff;padding:10px;border-radius:8px">linear-gradient(135deg, indigo → pink)</div>')
val("radial-gradient()", "A circular/elliptical color ramp.", "radial-gradient(circle at top left, #fde047, #f59e0b) — glows, vignettes, spotlight effects.", ".glow { background: radial-gradient(circle at 30% 20%, #fde047, transparent 60%); }", '<div style="background:radial-gradient(circle at 30% 30%, #fde047, #f59e0b);font-size:11px;color:#78350f;padding:10px;border-radius:8px">radial-gradient(circle at 30% 30%)</div>')
val("conic-gradient()", "A circular sweep from a center point (pie, spinners).", "conic-gradient(from 0deg, #2563eb, #22d3ee, #2563eb) — pie charts, conic masks, the @property spinner.", ".spinner { background: conic-gradient(#2563eb 0 25%, #e5e7eb 0); }", '<div style="background:conic-gradient(from 0deg,#2563eb,#22d3ee,#a78bfa,#f472b6,#2563eb);width:56px;height:56px;border-radius:50%;display:grid;place-items:center"><span style="width:34px;height:34px;background:#fff;border-radius:50%"></span></div>')
val("repeating-linear/radial/conic-gradient()", "Gradients that repeat (stripes, dots, checkers).", "repeating-linear-gradient(45deg, #0002 0 10px, transparent 10px 20px) → diagonal stripes. repeating-radial → rings. The pattern toolbox.", ".warn { background: repeating-linear-gradient(45deg,#fde047 0 12px,#f59e0b 12px 24px); }", '<div style="background:repeating-linear-gradient(45deg,#fde047 0 8px,#f59e0b 8px 16px);font-size:11px;color:#78350f;padding:8px;border-radius:6px">repeating-linear-gradient(45deg, stripes)</div>')
val("url()", "Reference an external resource (image, font, cursor).", "background-image: url(img.png); — also data URIs: url(data:image/svg+xml,…). Quote paths with spaces.", ".hero { background: url(cover.jpg) center/cover; }", '<div style="font-size:11px">url(cover.jpg) — image/font/cursor references</div>')
val("Length units: px em rem %", "Absolute vs relative measurement.", "px: fixed. em: × the ELEMENT's font-size (nested multiplies). rem: × the ROOT font-size (the sane default: 16px). %: of the containing block. Choose rem for type, % for widths, px for hairlines.", "body { font-size: 1rem; } h1 { font-size: 2rem; } .box { width: 50%; }", '<div style="font-size:12px">1rem = 16px · 2rem = 32px · em = parent-relative</div>')
val("Viewport units: vw vh vmin vmax dvh", "Relative to the viewport.", "1vw = 1% of viewport width; 1vh = 1% of height; vmin/vmax = the smaller/larger. dvh/svh/lvh account for mobile browser chrome. 100vh pitfalls → use 100dvh or svh for mobile full-screen.", ".hero { height: 100dvh; }", '<div style="font-size:11px">100dvh = the full visible mobile screen (no address-bar jumps)</div>')
val("Text units: ch ex cap", "Relative to the text itself.", "ch = width of \"0\" (70ch ≈ a comfortable line length); ex = the x-height; cap = cap height (newer). .measure { max-width: 70ch; } is the typography gold rule.", "p { max-width: 70ch; }", '<div style="font-size:12px;max-width:70ch">max-width: 70ch — a line length tuned by the font itself</div>')
val("fr (grid fractions)", "The grid unit for free space.", "1fr = one share of the remaining space: grid-template-columns: 1fr 2fr; → second column is double. Combine with minmax: minmax(200px, 1fr).", ".grid { grid-template-columns: 250px 1fr; }", '<div style="font-size:10px;display:grid;grid-template-columns:1fr 2fr;gap:4px;max-width:180px"><div style="background:#bfdbfe;padding:4px">1fr</div><div style="background:#60a5fa;color:#fff;padding:4px">2fr (double)</div></div>')
val("cover / contain", "background-size behaviors.", "cover: scale to FILL the box (crops). contain: scale to FIT the whole image (letterboxes). Photos → cover; logos/icons → contain.", ".photo { background-size: cover; }", '<div style="font-size:10px;display:flex;gap:6px"><div style="width:60px;height:40px;background:linear-gradient(135deg,#f472b6,#8b5cf6) center/cover;border-radius:6px"></div><div style="width:60px;height:40px;background:#e5e7eb;display:grid;place-items:center"><div style="width:60px;height:28px;background:linear-gradient(135deg,#f472b6,#8b5cf6) center/contain"></div></div></div>')
val("fit-content / min-content / max-content", "Size to the content.", "fit-content: shrink to content within the available space. min/max-content: the theoretical narrowest/widest (single line). Used in width, grid tracks, and flex-basis.", ".badge { width: fit-content; }", '<div style="font-size:11px"><span style="width:fit-content;background:#f3f4f6;border:1px solid #e5e7eb;padding:4px 8px">width: fit-content</span></div>')
val("ease keywords: ease / ease-in / ease-out / linear / steps()", "Timing function keywords.", "ease (default): slow-fast-slow. ease-out: fast→slow (best for elements ENTERING). ease-in: slow→fast (exiting). linear: constant. steps(4): jump in 4 frames (tickers).", ".x { transition: .3s ease-out; }", '<div style="font-size:11px;color:#4b5563">ease-out ▂▅▇ · ease-in ▁▃▅ · linear ▬▬▬ · steps(3) ▁▁▃▃▅▅</div>')
val("cubic-bezier(x1,y1,x2,y2)", "Custom timing curves (the pro move).", "Control points define the speed curve: (0,0) start, (1,1) end; y beyond 1 = overshoot (bounce). Popular: (.2,.8,.2,1) smooth decel; (.34,1.56,.64,1) spring.", ".card { transition: .4s cubic-bezier(.2,.8,.2,1); }", '<div style="font-size:11px;color:#4b5563">cubic-bezier(.34,1.56,.64,1) → overshoot spring curve</div>')
val("steps(n, jump)", "Step (discrete) timing.", "steps(4, end) jumps in 4 equal steps — loading dots, tickers, flip clocks. jump-start/none control the first/last jump.", ".dot { animation: blink 1s steps(2, jump-none) infinite; }", '<div style="font-size:11px;color:#4b5563">steps(2, jump-none) → A/B/A/B discrete frames</div>')
val("transform functions (translate/rotate/scale/skew/matrix)", "The 2D/3D math inside transform.", "translateX/Y/Z, rotate(X/Y/Z), scale(X/Y/Z), skew(X/Y), matrix(a,b,c,d,e,f), matrix3d(12 values), perspective(d). Functions compose left→right.", ".c { transform: translateX(20px) rotate(45deg) scale(1.1); }", '<div style="font-size:10px"><span style="display:inline-block;padding:6px 10px;background:#60a5fa;transform:rotate(12deg);margin-right:8px">rotate</span><span style="display:inline-block;padding:6px 10px;background:#f472b6;transform:scaleY(.7)">scaleY(.7)</span></div>')
val("inset() / rect() / circle()/polygon() (for clip-path & shapes)", "Shape functions for clipping and offset paths.", "clip-path: inset(10px round 8px) (rounded inset box), circle(50%), polygon(0 0, 100% 0, 100% 100%), path(\"M…\"). rect() is the legacy box syntax.", ".badge { clip-path: inset(0 round 6px); }", '<div style="font-size:10px"><span style="display:inline-block;width:52px;height:34px;background:#34d399;clip-path:inset(4px round 8px);margin-right:8px"></span><span style="display:inline-block;width:52px;height:34px;background:#fbbf24;clip-path:polygon(0 0,100% 0,85% 100%,0 100%)"></span></div>')
val("from/to/0%/100% (keyframe steps)", "Keyframe position syntax.", "@keyframes x { from {…} to {…} } or explicit: 0%, 50%, 100% — multiple stops define the full motion path.", "@keyframes pulse { 0%,100% { scale:1 } 50% { scale:1.08 } }", '<div style="font-size:11px;color:#4b5563">0% → 50% → 100%: three stops, full control</div>')
