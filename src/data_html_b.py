# -*- coding: utf-8 -*-
# HTML elements — Part B: Lists, Media, Forms, Tables, Interactive, Legacy/Obsolete

from data_html_a import E, add  # noqa: F401  (extend the same list)

# ---------------- LISTS ----------------
add("ul", "Unordered List", "Lists",
    "A bulleted list of items.",
    "<ul> is a list where order does not matter — each <li> gets a bullet. You can nest lists for sub-items. Use it for feature lists, menus, and collections of related items.",
    [("type", "—", "Obsolete. Bullet style is controlled by CSS list-style-type.")],
    '<ul>\n  <li>HTML</li>\n  <li>CSS</li>\n  <li>JavaScript</li>\n</ul>',
    '<ul style="font-size:13px;margin:0;padding-left:22px;line-height:1.7"><li>HTML</li><li>CSS</li><li>JavaScript</li></ul>',
    ["Custom bullets → CSS list-style (none, disc, square, custom image, ::marker)."],
    ["ol", "li", "dl"])

add("ol", "Ordered List", "Lists",
    "A numbered list of items.",
    "<ol> is a list where order matters — each <li> gets a number (or letter/roman via type/start/reversed attributes). Use for steps, rankings, and sequential instructions.",
    [("type", "1 / a / A / i / I", "Number style: digits, lowercase/uppercase Latin letters, lowercase/uppercase Roman numerals."),
     ("start", "integer", "The number of the first item."),
     ("reversed", "boolean", "Counts down instead of up.")],
    '<ol start="2">\n  <li>Second step</li>\n  <li>Third step</li>\n</ol>',
    '<ol start="2" style="font-size:13px;margin:0;padding-left:22px;line-height:1.7"><li>Second step</li><li>Third step</li></ol>',
    ["type=\"i\" gives i, ii, iii — no CSS needed."],
    ["ul", "li"])

add("li", "List Item", "Lists",
    "A single item inside <ul>, <ol> or <menu>.",
    "<li> is one entry of a list. It may contain any flow content, including nested lists. Inside <ol>, the ol.value property or value attribute can renumber from any point.",
    [("value", "integer", "Inside <ol>: sets the item's own number (renumbers the sequence)."),
     ("type", "—", "Obsolete per-item type; use CSS instead.")],
    '<ol>\n  <li>Start</li>\n  <li value="10">Jumps to 10</li>\n  <li>Then 11</li>\n</ol>',
    '<ol style="font-size:13px;margin:0;padding-left:22px;line-height:1.7"><li>Start</li><li value="10">Jumps to 10</li><li>Then 11</li></ol>',
    ["li.value lets a list skip numbers — handy for long documents."],
    ["ul", "ol"])

add("dl", "Description List", "Lists",
    "A list of term–description pairs (glossaries, metadata).",
    "<dl> is a two-column list: <dt> terms and <dd> descriptions. Perfect for glossaries, key–value metadata, and FAQ-like blocks.",
    [],
    '<dl>\n  <dt>HTML</dt>\n  <dd>The markup language of the web.</dd>\n  <dt>CSS</dt>\n  <dd>The styling language of the web.</dd>\n</dl>',
    '<dl style="font-size:13px;margin:0"><dt style="font-weight:700">HTML</dt><dd style="margin:0 0 6px 18px;color:#4b5563">The markup language of the web.</dd><dt style="font-weight:700">CSS</dt><dd style="margin:0 0 0 18px;color:#4b5563">The styling language of the web.</dd></dl>',
    ["A <div> may wrap dt/dd groups for styling (valid in HTML5)."],
    ["ul", "ol"])

add("dt", "Description Term", "Lists",
    "The term (name) in a description list.",
    "<dt> marks the term being described inside a <dl>. It renders bold by convention and must be followed by at least one <dd>.",
    [],
    "<dl><dt>term</dt><dd>definition</dd></dl>",
    '<div style="font-size:13px;font-weight:700">term <span style="font-weight:400;color:#6b7280">(dt)</span></div>',
    ["Must live inside a <dl>."],
    ["dd", "dl"])

add("dd", "Description Details", "Lists",
    "The description (details) for a term in a description list.",
    "<dd> provides the description for the preceding <dt> inside a <dl>. Multiple <dd> elements can follow one <dt>.",
    [],
    "<dl><dt>Web</dt><dd>World Wide Web — the document-based part of the Internet.</dd></dl>",
    '<div style="font-size:13px;color:#4b5563;margin-left:18px">World Wide Web — the document-based part of the Internet. <i>(dd)</i></div>',
    ["Multiple <dd> per <dt> are allowed."],
    ["dt", "dl"])

# ---------------- MEDIA & EMBEDDED ----------------
add("img", "Image", "Media & Embedded",
    "Embeds an image.",
    "<img> embeds an image. The src attribute is the URL and alt is the text alternative for screen readers and broken images. You control size with width/height (or CSS) — always set them to avoid layout shift.",
    [("src", "URL", "Required. Location of the image."),
     ("alt", "text", "Required (use alt=\"\" for decorative images). Alternative text."),
     ("width", "integer", "Intrinsic width in pixels."),
     ("height", "integer", "Intrinsic height in pixels."),
     ("loading", "eager / lazy", "lazy defers loading until near the viewport."),
     ("referrerpolicy", "policy", "Which referrer to send (no-referrer, origin, strict-origin-when-cross-origin…)."),
     ("srcset", "URLs + descriptors", "Candidate images for different resolutions/DPRs."),
     ("sizes", "media conditions", "With srcset: the rendered width per media condition."),
     ("decoding", "async / sync", "Hint for when to decode the image."),
     ("crossorigin", "anonymous / use-credentials", "CORS mode (needed for canvas readback).")],
    '<img src="cat.jpg" alt="A cat sleeping on a laptop" width="400">\n<img srcset="cat-400.jpg 400w, cat-800.jpg 800w"\n     sizes="(max-width: 600px) 90vw, 400px">',
    '<div style="width:130px;height:86px;border-radius:8px;background:radial-gradient(circle at 30% 30%,#fbbf24,#92400e);position:relative;overflow:hidden"><span style="position:absolute;bottom:4px;right:6px;font-size:10px;color:#fff;text-shadow:0 1px 2px #000">cat.jpg 400×260</span></div>',
    ["Always write alt text — empty alt only for purely decorative images.", "Set width/height (or aspect-ratio in CSS) to prevent layout shift (Core Web Vitals)."],
    ["picture", "source", "figure"])

add("picture", "Adaptive Image Container", "Media & Embedded",
    "Wraps multiple <source> candidates to serve the right image per condition.",
    "<picture> is an art-directed image: a set of <source> elements with media/type conditions, each pointing at a different image, with a final <img> as fallback. The browser picks the first matching source.",
    [],
    '<picture>\n  <source media="(max-width: 600px)" srcset="thumb.jpg">\n  <source type="image/webp" srcset="hero.webp">\n  <img src="hero.jpg" alt="Hero">\n</picture>',
    '<div style="display:flex;gap:6px;align-items:center;font-size:11px;font-family:monospace"><span>≤600px → thumb.jpg</span><span>webp → hero.webp</span><span>fallback → hero.jpg</span></div>',
    ["The last child must be an <img> (the default).", "Use for format switching (WebP/AVIF) or art direction."],
    ["img", "source"])

add("source", "Resource for media/picture", "Media & Embedded",
    "A candidate resource for <video>, <audio> or <picture>.",
    "<source> lists one candidate for a media element or picture: different formats for <video>/<audio>, or a media/type condition for <picture>. The browser tries them in order until one works.",
    [("src", "URL", "For <picture>: the candidate image."),
     ("srcset", "URLs", "For <picture>: candidates by width/DPR."),
     ("media", "media query", "Apply only when the query matches."),
     ("type", "MIME type", "e.g. video/webm, audio/ogg, image/avif."),
     ("sizes", "media conditions", "With srcset in <picture>.")],
    '<video controls>\n  <source src="movie.webm" type="video/webm">\n  <source src="movie.mp4" type="video/mp4">\n</video>',
    '<div style="font-family:monospace;font-size:11px;background:#f6f8fa;border:1px solid #d0d7de;border-radius:6px;padding:8px">1) movie.webm  ✓ plays<br>2) movie.mp4  (fallback, skipped)</div>',
    ["Order matters: best format first.", "In <video>/<audio>, never add a plain URL attribute to the parent when using <source>."],
    ["video", "audio", "picture"])

add("video", "Video Player", "Media & Embedded",
    "Embeds a video player with optional controls, autoplay, loop and captions.",
    "<video> plays video. Without the controls attribute it renders a bare media box (JS controls the playback). src can point at a file, or you can list <source> formats. Add <track> for captions.",
    [("src", "URL", "Video file, when not using <source>."),
     ("controls", "boolean", "Show native playback controls."),
     ("autoplay", "boolean", "Start playing (must be muted to work on mobile)."),
     ("muted", "boolean", "Start muted (required for autoplay)."),
     ("loop", "boolean", "Restart at the end."),
     ("poster", "URL", "Image shown before playback starts."),
     ("preload", "none / metadata / auto", "How much to fetch before playing."),
     ("playsinline", "boolean", "Play inline (iOS) instead of fullscreen takeover."),
     ("width / height", "integer", "Intrinsic size of the player.")],
    '<video controls width="320" poster="thumb.jpg">\n  <source src="clip.webm" type="video/webm">\n  <source src="clip.mp4" type="video/mp4">\n  <track kind="captions" src="en.vtt" srclang="en" label="EN">\n</video>',
    '<div style="width:230px;height:120px;background:linear-gradient(135deg,#1e3a5f,#0f172a);border-radius:8px;position:relative"><span style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center"><span style="width:0;height:0;border-left:22px solid rgba(255,255,255,.9);border-top:14px solid transparent;border-bottom:14px solid transparent"></span></span><span style="position:absolute;bottom:6px;left:8px;font-size:10px;color:#e5e7eb">▶ clip.mp4 — controls</span></div>',
    ["autoplay requires muted in all modern browsers.", "Always provide a poster + dimensions to avoid layout shift."],
    ["audio", "source", "track", "picture"])

add("audio", "Audio Player", "Media & Embedded",
    "Embeds an audio player (music, podcasts, sound effects).",
    "<audio>  plays sound. Same model as <video>: src or <source> children, controls for the native UI, track for transcripts. Without src it renders nothing visible (useful as a pure JS audio engine).",
    [("src", "URL", "Audio file."),
     ("controls", "boolean", "Show native controls."),
     ("autoplay / muted / loop / preload", "—", "Same meanings as <video>."),
     ("crossorigin", "anonymous / use-credentials", "CORS for Web Audio API processing.")],
    '<audio controls src="podcast.mp3"></audio>',
    '<div style="width:220px;background:#f9fafb;border:1px solid #e5e7eb;border-radius:8px;padding:8px;display:flex;align-items:center;gap:8px;font-size:11px"><span style="width:0;height:0;border-left:14px solid #2563eb;border-top:9px solid transparent;border-bottom:9px solid transparent"></span><div style="flex:1"><div style="height:5px;background:#e5e7eb;border-radius:3px"><div style="width:40%;height:100%;background:#2563eb;border-radius:3px"></div></div><small style="color:#6b7280">03:12 / 07:45 — podcast.mp3</small></div></div>',
    ["No src + no children → invisible element (good for JS audio)."],
    ["video", "source", "track"])

add("track", "Media Text Track", "Media & Embedded",
    "Captions, subtitles or chapters for <video>/<audio>.",
    "<track> attaches a text track file (WebVTT) to a media element: captions, subtitles, chapters, descriptions or metadata. Browsers expose them in the player's CC menu.",
    [("src", "URL", "Required. The .vtt file."),
     ("kind", "subtitles / captions / descriptions / chapters / metadata", "Type of track (default: subtitles)."),
     ("srclang", "BCP-47", "Required. Language of the track."),
     ("label", "text", "Shown in the track menu."),
     ("default", "boolean", "Load and show this track first.")],
    '<video controls>\n  <source src="movie.mp4">\n  <track kind="captions" src="en.vtt" srclang="en" label="English" default>\n</video>',
    '<div style="font-family:monospace;font-size:11px;background:#000;color:#fff;border-radius:6px;padding:10px;text-align:center">“Welcome to the course”</div><div style="text-align:center;font-size:10px;color:#6b7280">CC · English (default) · Chapters</div>',
    ["kind=\"captions\" for the deaf/hard-of-hearing; \"subtitles\" for translation."],
    ["video", "audio"])

add("canvas", "Programmable Drawing Surface", "Media & Embedded",
    "A bitmap drawing surface controlled by the 2D API or WebGL.",
    "<canvas>  is a raster surface you draw on with JavaScript: charts, games, image editing, particle effects. It has width/height in pixels and exposes a 2D context or a WebGL context.",
    [("width", "integer", "Buffer width in pixels (default 300)."),
     ("height", "integer", "Buffer height in pixels (default 150).")],
    '<canvas id="c" width="200" height="80"></canvas>\n<script>\n  const x = document.querySelector("#c").getContext("2d");\n  x.fillStyle = "#4285f4"; x.fillRect(10, 10, 80, 40);\n  x.fillStyle = "#34a853"; x.fillRect(100, 20, 80, 40);\n</script>',
    '<canvas width="200" height="80" style="border:1px solid #e5e7eb;border-radius:6px;background:#fff"></canvas>',
    ["Canvas is not accessible by default — add a fallback inside or an aria-label.", "For charts that must be readable/printable, consider SVG instead."],
    ["svg", "img"])

# (fill canvas demo after DOM: small script in build)
E[-1]["dm"] += '<script>document.querySelector("canvas").getContext("2d").fillStyle="#4285f4",document.querySelector("canvas").getContext("2d").fillRect(10,10,80,40)</script>'

add("svg", "Vector Graphics (inline)", "Media & Embedded",
    "Scalable vector graphics written inline in HTML.",
    "<svg> embeds vector graphics directly in the page: icons, charts, logos, illustrations. It scales without quality loss, is styleable with CSS, and each shape is a DOM node (scriptable). Use viewBox for scalable coordinate systems.",
    [("viewBox", "min-x min-y w h", "The coordinate system the drawing is scaled into."),
     ("width / height", "length", "Rendered size (CSS can override)."),
     ("role / aria-label", "—", "Accessibility for decorative/informational graphics.")],
    '<svg viewBox="0 0 40 40" width="40" height="40" aria-hidden="true">\n  <circle cx="20" cy="20" r="18" fill="#4285f4"></circle>\n  <path d="M12 21 L18 27 L29 14" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"></path>\n</svg>',
    '<svg viewBox="0 0 40 40" width="56" height="56" aria-hidden="true"><circle cx="20" cy="20" r="18" fill="#4285f4"></circle><path d="M12 21 L18 27 L29 14" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"></path></svg>',
    ["Add role=\"img\" + <title> for meaningful graphics; aria-hidden=\"true\" for decorative icons."],
    ["canvas", "img"])

add("math", "MathML Math", "Media & Embedded",
    "Mathematical notation using MathML.",
    "<math> wraps MathML content for equations and formulas (fractions, matrices, integrals). Browsers render MathML natively now (Chrome shipped it). Use it for real math instead of styled spans.",
    [("display", "inline / block", "Block for display equations.")],
    '<math display="block"><mfrac><mi>a</mi><mi>b</mi></mfrac><mo>=</mo><mfrac><mi>c</mi><mi>d</mi></mfrac></math>',
    '<div style="font-family:serif;font-size:16px;text-align:center;padding:6px"><span style="display:inline-block;text-align:center;vertical-align:middle"><span style="display:block;border-bottom:1px solid #333;padding:0 4px 2px">a</span><span style="display:block;padding:2px 4px 0">b</span></span> = <span style="display:inline-block;text-align:center;vertical-align:middle"><span style="display:block;border-bottom:1px solid #333;padding:0 4px 2px">c</span><span style="display:block;padding:2px 4px 0">d</span></span></div>',
    ["MathML 3.0 core is supported in all modern browsers."],
    ["sub", "sup"])

add("iframe", "Inline Frame", "Media & Embedded",
    "Embeds another HTML page in a nested browsing context.",
    "<iframe>  embeds a separate HTML document: maps, embedded players, widgets, or a whole app inside a shell. It creates an isolated browsing context (own DOM, cookies, JS). Use the sandbox attribute to restrict what the content can do.",
    [("src", "URL", "The embedded document."),
     ("srcdoc", "HTML", "Inline HTML to render (no URL needed)."),
     ("name", "string", "Target name for links/forms."),
     ("width / height", "length", "Frame size."),
     ("sandbox", "tokens", "Security: strips permissions (allow-scripts, allow-same-origin…)."),
     ("allow", "feature-policy", "Permissions Policy: e.g. allow=\"camera; fullscreen\"."),
     ("referrerpolicy", "policy", "Referrer to send to the embedded page."),
     ("loading", "eager / lazy", "Lazy-load the frame."),
     ("allowfullscreen", "boolean", "Permit fullscreen (media embeds).")],
    '<iframe srcdoc="<h1>Hello from an iframe</h1>"\n        width="260" height="70" sandbox="allow-same-origin"></iframe>',
    '<div style="border:2px solid #8b949e;border-radius:6px;width:250px;padding:8px;background:#fff"><h1 style="font-size:14px;margin:2px 0 0">Hello from an iframe</h1><div style="font-size:10px;color:#8b949e">separate document, own DOM</div></div>',
    ["Embedding content you don't control → add sandbox + referrerpolicy.", "Maps/video embeds often require allowfullscreen + allow attributes."],
    ["object", "embed"])

add("embed", "Plug-in Content", "Media & Embedded",
    "Embeds an external application (legacy plugin interface).",
    "<embed>  loads a plugin/external resource defined by its type (PDF, media). It is largely historical — modern web uses <video>, <audio>, <canvas>, <iframe> instead. Still seen for PDFs in some browsers.",
    [("src", "URL", "Required. The resource."),
     ("type", "MIME type", "e.g. application/pdf."),
     ("width / height", "length", "Size of the embed.")],
    '<embed src="document.pdf" type="application/pdf" width="100%" height="400">',
    '<div style="border:1px solid #d1d5db;border-radius:6px;width:220px;padding:10px;background:#f9fafb;font-size:11px;font-family:monospace">document.pdf<br><span style="color:#6b7280">application/pdf — 100% × 400</span></div>',
    ["Prefer modern elements; <embed> is the legacy path."],
    ["object", "iframe"])

add("object", "External Resource Object", "Media & Embedded",
    "Embeds an external resource (legacy alternative to <embed>), with <param> children and fallback content.",
    "<object>  embeds a resource by data URL, with named parameters via <param> children. Unlike <embed>, it supports fallback content (shown when the resource can't load) — which is why it is the more 'proper' legacy element.",
    [("data", "URL", "The resource to embed."),
     ("type", "MIME type", "Resource type."),
     ("name", "string", "Form name (if used in a form)."),
     ("width / height", "length", "Size."),
     ("form", "ID", "Associates with a form.")],
    '<object data="model.glb" type="model/gltf-binary" width="200" height="150">\n  <p>Your browser cannot show 3D models. <a href="model.glb">Download</a>.</p>\n</object>',
    '<div style="border:1px solid #d1d5db;border-radius:6px;width:200px;padding:10px;background:#eff6ff;font-size:11px">model.glb not supported here → fallback shows: "Download the model".</div>',
    ["Fallback content = the whole point over <embed>."],
    ["embed", "param"])

add("param", "Parameter for <object>", "Media & Embedded",
    "A named parameter passed to an <object> resource.",
    "<param>  defines a name/value pair for an <object>. It is meaningful only inside <object> (applets/legacy plugins consumed it). Rarely needed in the modern web.",
    [("name", "string", "Parameter name."),
     ("value", "string", "Parameter value."),
     ("type", "—", "Historical.")],
    '<object data="game.swf" type="application/x-shockwave-flash">\n  <param name="quality" value="high">\n</object>',
    '<div style="font-family:monospace;font-size:11px;background:#f6f8fa;border:1px solid #d0d7de;border-radius:6px;padding:8px">name="quality" value="high" → passed to the object</div>',
    ["Effectively obsolete with the death of Flash/applets."],
    ["object"])

add("map", "Image Map Container", "Media & Embedded",
    "Defines a client-side image map: clickable regions on an image.",
    "<map>  holds <area> elements that define clickable shapes over an image. Link the image to it with <img usemap=\"#name\" map> name=\"name\">.",
    [("name", "string", "Required. Matches the image's usemap attribute (without #).")],
    '<img src="island.png" usemap="#island" alt="Island map">\n<map name="island">\n  <area shape="rect" coords="0,0,120,80" href="/beach" alt="Beach">\n  <area shape="circle" coords="150,60,30" href="/lake" alt="Lake">\n</map>',
    '<div style="width:190px;height:90px;background:linear-gradient(135deg,#bae6fd,#34d399);border-radius:8px;position:relative;font-size:10px"><span style="position:absolute;top:8px;left:10px;color:#0c4a6e;border:1px dashed #0c4a6e;padding:2px 6px;border-radius:4px">rect: Beach</span><span style="position:absolute;bottom:8px;right:14px;color:#064e3b;border:1px dashed #064e3b;padding:2px 6px;border-radius:4px">circle: Lake</span></div>',
    ["Accessibility: give every <area> an alt — it's hard to navigate by keyboard."],
    ["area", "img"])

add("area", "Interactive Region of an Image Map", "Media & Embedded",
    "A clickable region (shape + coordinates) inside a <map>.",
    "<area>  defines one interactive region of an image map: its shape (rect/circle/poly), coordinates, and target URL. Each area needs alt text.",
    [("shape", "default / rect / circle / poly", "Region shape."),
     ("coords", "numbers", "Coordinates matching the shape."),
     ("href", "URL", "Navigation target."),
     ("alt", "text", "Required. Accessible label for the region."),
     ("target", "window name", "Where to open."),
     ("nohref", "boolean", "Makes the region non-navigable (decorative).")],
    '<map name="m">\n  <area shape="rect" coords="0,0,100,50" href="/a" alt="Section A">\n</map>',
    '<div style="font-family:monospace;font-size:11px;background:#f6f8fa;border:1px solid #d0d7de;border-radius:6px;padding:8px">shape=rect coords=0,0,100,50 → /a</div>',
    ["poly allows arbitrary polygons: x1,y1,x2,y2,…"],
    ["map"])

# ---------------- FORMS ----------------
add("form", "Form Container", "Forms",
    "A section for user input, submitted to a server.",
    "<form>  groups input controls and submits them. action is the URL and method is GET or POST. Native validation works when required/pattern etc. are set — no JS needed for basic validation. A submit <button> or <input type=\"submit\"> triggers submission.",
    [("action", "URL", "Where to send the data. Empty = current page."),
     ("method", "get / post", "get puts data in the URL; post in the body (default: get)."),
     ("enctype", "multipart/form-data | application/x-www-form-urlencoded | text/plain", "Encoding; multipart is required for file uploads."),
     ("autocomplete", "on / off", "Password manager / autofill behavior (overridable per field)."),
     ("accept-charset", "charset list", "Accepted character sets (rarely used).")],
    '<form action="/search" method="get">\n  <input name="q" placeholder="Search…" required>\n  <button type="submit">Search</button>\n</form>',
    '<form style="display:flex;gap:6px"><input placeholder="Search…" style="flex:1;border:1px solid #d1d5db;border-radius:6px;padding:6px 10px;font-size:12px"><button style="background:#2563eb;color:#fff;border:none;border-radius:6px;padding:6px 14px;font-size:12px">Search</button></form>',
    ["method=\"get\" → data in the URL (shareable); \"post\" → in the body (private).", "enctype=\"multipart/form-data\" is mandatory for <input type=\"file\">."],
    ["input", "button", "select", "textarea"])

add("input", "Input Field (18+ types)", "Forms",
    "The most versatile form control: text, email, number, date, file, checkbox, radio, range, color, search and more.",
    "<input>  is the swiss-army knife of forms. Its type attribute switches the control: text, search, email, url, tel, password, number, range, date, time, datetime-local, month, week, color, checkbox, radio, file, hidden, submit, reset, image, button. Types unlock native validation, pickers and keyboard input (inputmode).",
    [("type", "keyword", "The control type (see summary)."),
     ("name", "string", "Key used in the submitted data."),
     ("value", "string", "Default/current value."),
     ("placeholder", "text", "Hint text (not a label replacement!)."),
     ("required", "boolean", "Must be filled to submit."),
     ("min / max", "number/date", "Numeric or date bounds (validation + stepper)."),
     ("minlength / maxlength", "integer", "Text length bounds."),
     ("pattern", "regex", "Value must match (no ^$)."),
     ("step", "number", "Increment for number/range/date."),
     ("checked", "boolean", "Default state for checkbox/radio."),
     ("disabled", "boolean", "Not interactable, not submitted."),
     ("readonly", "boolean", "Selectable but not editable (still submitted)."),
     ("multiple", "boolean", "email: several values; file: several files; select: multi-select."),
     ("accept", "MIME list", "file: filter file types (e.g. image/*, .pdf)."),
     ("list", "ID", "Links to a <datalist> for suggestions."),
     ("inputmode", "none/text/decimal/numeric/tel/email/url/search", "Mobile keyboard type."),
     ("autofocus", "boolean", "Focus on page load."),
     ("autocomplete", "token", "Autofill hint: name, email, cc-number, on, off…")],
    '<form>\n  <label>Full name\n    <input type="text" name="name" required autocomplete="name">\n  </label>\n  <label>Email\n    <input type="email" name="email" required>\n  </label>\n  <label>Age\n    <input type="number" name="age" min="0" max="120">\n  </label>\n  <label><input type="checkbox" name="news" checked> Newsletter</label>\n  <button>Send</button>\n</form>',
    '<form style="display:grid;gap:8px;font-size:12px;max-width:250px"><label style="display:grid;gap:3px"><b>Full name</b><input style="border:1px solid #d1d5db;border-radius:6px;padding:5px 8px"></label><label style="display:grid;gap:3px"><b>Email</b><input type="email" style="border:1px solid #d1d5db;border-radius:6px;padding:5px 8px"></label><label style="display:flex;gap:6px;align-items:center"><input type="checkbox" checked> Newsletter</label><button style="justify-self:start;background:#2563eb;color:#fff;border:none;border-radius:6px;padding:6px 16px">Send</button></form>',
    ["One name+value per input; radios group by sharing name.", "placeholder is a hint, not a label — always use <label>."],
    ["button", "datalist", "label", "select"])

add("button", "Button", "Forms",
    "A clickable button: submit, reset, or script-triggered action.",
    "<button>  is the standard button. type=\"submit\" (default in a form) submits the form, type=\"reset\" clears it, type=\"button\" does nothing by default (JS handles it). It can contain rich content (icon + text) unlike <input type=\"submit\">.",
    [("type", "submit / reset / button", "Behavior. Default inside a form: submit."),
     ("name / value", "string", "Submitted with the form when it submits."),
     ("form", "ID", "Associates with a form outside it."),
     ("formaction / formmethod", "URL / method", "Override the form's action/method for this button."),
     ("disabled", "boolean", "Not clickable, not submitted."),
     ("autofocus", "boolean", "Focus on load.")],
    '<form>\n  <input name="q" required>\n  <button type="submit">Search</button>\n  <button type="button" id="clear">Clear</button>\n</form>',
    '<div style="display:flex;gap:8px"><button style="background:#2563eb;color:#fff;border:none;border-radius:6px;padding:7px 16px;font-size:12px">Search (submit)</button><button style="background:#f3f4f6;color:#374151;border:1px solid #d1d5db;border-radius:6px;padding:7px 14px;font-size:12px">Clear (button)</button></div>',
    ["Outside a form, a button has no default action — add a click handler."],
    ["input", "form"])

add("select", "Dropdown Select", "Forms",
    "A dropdown list of options (single or multiple choice).",
    "<select>  is a dropdown. Its children are <option> (and <optgroup> for groups). With multiple it becomes a multi-select listbox. The selected option is what gets submitted under the select's name.",
    [("name", "string", "Key in the submitted data."),
     ("size", "integer", "Height in rows (turns it into a listbox)."),
     ("multiple", "boolean", "Allow selecting several options."),
     ("required", "boolean", "A valid option must be chosen."),
     ("disabled", "boolean", "Whole control disabled."),
     ("autofocus", "boolean", "Focus on load.")],
    '<select name="country">\n  <option value="" selected>Choose…</option>\n  <option value="eg">Egypt</option>\n  <option value="sa">Saudi Arabia</option>\n  <optgroup label="Europe">\n    <option value="de">Germany</option>\n  </optgroup>\n</select>',
    '<div style="font-size:12px"><div style="border:1px solid #d1d5db;border-radius:6px;padding:6px 10px;background:#fff;min-width:170px;display:flex;justify-content:space-between">Choose… <span style="color:#6b7280">▾</span></div><div style="border:1px solid #d1d5db;border-top:none;border-radius:0 0 6px 6px;background:#fff"><div style="padding:5px 10px;background:#eff6ff">✔ Egypt</div><div style="padding:5px 10px">Saudi Arabia</div><div style="padding:5px 10px;font-weight:600;font-size:11px;color:#6b7280">Europe</div><div style="padding:5px 10px 5px 18px">Germany</div></div></div>',
    ["First <option> is selected by default — use value=\"\" + disabled for a real placeholder.", "multiple + Ctrl/Cmd for multi-select (or use checkboxes for better UX)."],
    ["option", "optgroup", "datalist"])

add("option", "Select Option", "Forms",
    "A single choice inside <select> or <datalist>.",
    "<option>  is one choice. value is what gets submitted (defaults to its text). selected pre-selects it; disabled greys it out (still submittable if pre-selected).",
    [("value", "string", "Submitted value (defaults to the option text)."),
     ("selected", "boolean", "Initially selected."),
     ("disabled", "boolean", "Cannot be selected (by the user)."),
     ("label", "text", "Label shown in the dropdown (else the text content is used).")],
    '<select>\n  <option value="a" selected>Alpha</option>\n  <option value="b" disabled>Beta (soon)</option>\n</select>',
    '<div style="font-size:12px"><div style="padding:4px 8px;background:#eff6ff;border-radius:4px 4px 0 0">✔ Alpha</div><div style="padding:4px 8px;color:#9ca3af">Beta (soon) — disabled</div></div>',
    ["Disabled options can still be submitted if they were pre-selected."],
    ["select", "optgroup", "datalist"])

add("optgroup", "Option Group", "Forms",
    "A labeled group of <option> elements inside a <select>.",
    "<optgroup>  groups related options under a label (like a section in a dropdown). The label attribute is required for the group name.",
    [("label", "text", "Required. Group heading shown in the dropdown."),
     ("disabled", "boolean", "Disables all options in the group.")],
    '<select>\n  <optgroup label="Fruits">\n    <option>Apple</option>\n    <option>Banana</option>\n  </optgroup>\n</select>',
    '<div style="font-size:12px;border:1px solid #e5e7eb;border-radius:6px;padding:4px;background:#fff"><div style="font-weight:600;font-size:11px;color:#6b7280;padding:2px 8px">Fruits</div><div style="padding:3px 8px 3px 18px">Apple</div><div style="padding:3px 8px 3px 18px">Banana</div></div>',
    ["label is the only required attribute — the group has no value."],
    ["option", "select"])

add("datalist", "Suggestions List", "Forms",
    "A list of suggestions an <input> can autocomplete from.",
    "<datalist>  provides suggestion values for an <input> linked via the input's list attribute. The browser shows them in a dropdown while typing — the user may also type their own value (unlike <select>).",
    [],
    '<input list="browsers" placeholder="Browser…">\n<datalist id="browsers">\n  <option value="Chrome">\n  <option value="Firefox">\n  <option value="Safari">\n</datalist>',
    '<div style="font-size:12px;max-width:180px"><div style="border:1px solid #d1d5db;border-radius:6px;padding:6px 8px;color:#9ca3af">Bro▮</div><div style="border:1px solid #d1d5db;border-top:none;border-radius:0 0 6px 6px;background:#fff;font-size:11px"><div style="padding:4px 8px">Chrome</div><div style="padding:4px 8px">Firefox</div></div></div>',
    ["Only certain input types support datalist: text, search, url, tel, email, number, range, date, month, week, time, datetime-local, color."],
    ["input", "option"])

add("textarea", "Multi-line Text Input", "Forms",
    "A multi-line plain-text input field.",
    "<textarea>  is a resizable multi-line text box. The initial value is its text content (not a value attribute). wrap controls how long lines are submitted (soft = \\n per line).",
    [("name", "string", "Submitted key."),
     ("rows", "integer", "Visible number of lines (default 2)."),
     ("cols", "integer", "Visible width in characters (default 20)."),
     ("placeholder", "text", "Hint text."),
     ("required", "boolean", "Must not be empty."),
     ("maxlength", "integer", "Max characters."),
     ("wrap", "soft / hard", "soft (default): break visually only; hard: insert \\n on submit."),
     ("readonly / disabled", "boolean", "As on <input>."),
     ("autocomplete", "token", "e.g. off, street-address.")],
    '<label>Message\n  <textarea rows="3" maxlength="200" placeholder="Write here…"></textarea>\n</label>',
    '<div style="font-size:12px;max-width:220px"><b style="font-size:11px">Message</b><div style="border:1px solid #d1d5db;border-radius:6px;padding:6px 8px;color:#9ca3af;min-height:44px">Write here…</div></div>',
    ["Initial value = inner text, e.g. <textarea>Hi</textarea> starts with “Hi”."],
    ["input", "label"])

add("label", "Form Label", "Forms",
    "A caption for a form control — clickable, and read by screen readers.",
    "<label>  associates text with a control: clicking the label focuses/activates the control, and screen readers announce it as the control's name. Link explicitly with for=\"id\" or wrap the control inside the label.",
    [("for", "ID", "ID of the labeled control."),
     ("form", "ID", "Associate with a form even when outside it.")],
    '<label for="email">Email address</label>\n<input id="email" type="email">\n\n<label>Accept terms\n  <input type="checkbox" id="t">\n</label>',
    '<div style="font-size:12px;max-width:230px"><div style="display:flex;gap:8px;align-items:center"><span style="font-weight:600">Email address</span><input style="flex:1;border:1px solid #d1d5db;border-radius:6px;padding:5px 8px"></div><div style="display:flex;gap:6px;align-items:center;margin-top:8px"><input type="checkbox" checked> <span>Accept terms (wrapped label — click the text to toggle)</span></div></div>',
    ["Every control needs a label — accessibility requirement #1 for forms."],
    ["input", "fieldset"])

add("fieldset", "Form Field Group", "Forms",
    "Groups related form controls with a border and a <legend> caption.",
    "<fieldset>  visually groups related controls (delivery options, address fields). Its first child should be a <legend>. Disabling a fieldset disables all controls inside it — handy for read-only forms.",
    [("disabled", "boolean", "Disables every control inside."),
     ("form", "ID", "Associate with a form outside it."),
     ("name", "string", "Name (if it has a value).")],
    '<fieldset>\n  <legend>Delivery</legend>\n  <label><input type="radio" name="d" checked> Standard (3 days)</label>\n  <label><input type="radio" name="d"> Express (1 day, +$5)</label>\n</fieldset>',
    '<div style="border:1px solid #d1d5db;border-radius:8px;padding:10px 12px 10px 4px;font-size:12px;max-width:250px"><span style="position:relative;top:-13px;left:8px;background:#fff;padding:0 6px;font-weight:600">Delivery</span><div style="display:grid;gap:5px;margin-top:4px"><label style="display:flex;gap:6px;align-items:center"><input type="radio" name="d" checked> Standard (3 days)</label><label style="display:flex;gap:6px;align-items:center"><input type="radio" name="d"> Express (1 day, +$5)</label></div></div>',
    ["fieldset disabled = all children disabled. Powerful for 'review' mode."],
    ["legend", "label"])

add("legend", "Fieldset Caption", "Forms",
    "The caption of a <fieldset>.",
    "<legend>  labels a <fieldset>: the text the group is about. It must be the first child of its <fieldset>.",
    [("float", "left/right/none", "Deprecated positioning — use CSS.")],
    "<fieldset><legend>Contact details</legend>…</fieldset>",
    '<div style="font-size:12px;border:1px solid #d1d5db;border-radius:8px;padding:14px 12px 8px 4px;max-width:200px"><span style="position:relative;top:-13px;left:8px;background:#fff;padding:0 6px;font-weight:600">Contact details</span><div style="color:#6b7280;margin-top:2px">name, phone, address…</div></div>',
    ["First child of <fieldset>, or it is ignored."],
    ["fieldset"])

add("output", "Calculation Result", "Forms",
    "The result of a form calculation or user action.",
    "<output>  displays the result of a computation tied to form controls (a live total, a converted value). The for attribute lists the IDs of the controls that produce it.",
    [("for", "ID list", "Space-separated IDs of the input controls."),
     ("name", "string", "Submitted name (if in a form)."),
     ("form", "ID", "Associate with a form outside it.")],
    '<input type="number" id="a" value="3" aria-label="A">\n× <input type="number" id="b" value="4" aria-label="B">\n= <output name="result" for="a b">12</output>',
    '<div style="font-size:13px;font-family:monospace;background:#f0fdf4;border:1px solid #86efac;border-radius:6px;padding:8px;display:flex;gap:6px;align-items:center"><span>3</span>×<span>4</span>=<b style="background:#dcfce7;padding:2px 8px;border-radius:4px">12</b></div>',
    ["It is a display, not an input — update it with JS (or server output)."],
    ["input", "form"])

# ---------------- TABLES ----------------
add("table", "Table", "Tables",
    "A two-dimensional table of data.",
    "<table>  presents tabular data: rows of related values. The anatomy is table > (caption, colgroup) + thead + tbody (one or more) + tfoot > tr > th/td. Use it for real data — never for page layout.",
    [("border", "—", "Obsolete; use CSS border-collapse/borders."),
     ("cellpadding / cellspacing", "—", "Obsolete; use CSS padding/gap."),
     ("width", "—", "Obsolete; use CSS width.")],
    '<table>\n  <caption>Monthly sales</caption>\n  <thead><tr><th>Month</th><th>Sales</th></tr></thead>\n  <tbody>\n    <tr><td>Aug</td><td>$12,400</td></tr>\n    <tr><td>Sep</td><td>$14,100</td></tr>\n  </tbody>\n</table>',
    '<table style="border-collapse:collapse;font-size:11px;width:210px"><caption style="caption-side:top;font-weight:600;padding:4px">Monthly sales</caption><thead><tr><th style="border:1px solid #d1d5db;background:#f3f4f6;padding:4px 8px;text-align:left">Month</th><th style="border:1px solid #d1d5db;background:#f3f4f6;padding:4px 8px;text-align:left">Sales</th></tr></thead><tbody><tr><td style="border:1px solid #e5e7eb;padding:4px 8px">Aug</td><td style="border:1px solid #e5e7eb;padding:4px 8px">$12,400</td></tr><tr><td style="border:1px solid #e5e7eb;padding:4px 8px">Sep</td><td style="border:1px solid #e5e7eb;padding:4px 8px">$14,100</td></tr></tbody></table>',
    ["Tables are for data, not layout — layout = CSS flex/grid.", "th scope=\"col\"/\"row\" is the accessibility must."],
    ["tr", "th", "td", "caption", "colgroup"])

add("caption", "Table Caption", "Tables",
    "The title/caption of a <table>.",
    "<caption>  is the table's title, shown above the table by default (flip with CSS caption-side). It must be the first child of the table.",
    [("align", "—", "Obsolete; use CSS caption-side/borders.")],
    '<table><caption>Population 2026</caption>…</table>',
    '<div style="font-size:11px;font-weight:600;text-align:center;border-bottom:2px solid #374151;padding:4px;width:210px">Population 2026</div>',
    ["One per table, as the first child."],
    ["table"])

add("colgroup", "Column Group", "Tables",
    "Groups columns so they can be styled via <col>.",
    "<colgroup>  contains <col> elements that apply styles (width, background) to whole columns. It is the only way to style an entire column without touching every cell.",
    [("span", "integer", "Number of columns the group applies to.")],
    '<table>\n  <colgroup>\n    <col style="width:70px">\n    <col span="2" style="background:#fef9c3">\n  </colgroup>\n  …rows…\n</table>',
    '<div style="font-family:monospace;font-size:11px;background:#f6f8fa;border:1px solid #d0d7de;border-radius:6px;padding:8px">col[0] width:70px<br>col[1..2] background:#fef9c3 <span style="display:inline-block;width:10px;height:10px;background:#fef9c3;vertical-align:-1px"></span></div>',
    ["Styling via <col> beats repeating CSS on every cell."],
    ["col", "table"])

add("col", "Column Definition", "Tables",
    "Defines a single column inside a <colgroup> (for styling).",
    "<col>  styles one column: width, background, alignment (via CSS). With span it covers several columns. It contains no content — it is pure styling metadata.",
    [("span", "integer", "Apply to this many columns (default 1)."),
     ("width", "—", "Obsolete; use CSS width.")],
    '<colgroup><col span="1"><col span="3" style="background:#eef2ff"></colgroup>',
    '<div style="display:flex;font-size:10px;height:26px"><div style="flex:1;border:1px solid #d1d5db">1</div><div style="flex:1;border:1px solid #d1d5db;background:#eef2ff">2</div><div style="flex:1;border:1px solid #d1d5db;background:#eef2ff">3</div><div style="flex:1;border:1px solid #d1d5db;background:#eef2ff">4</div></div>',
    ["No content model — it is not visible itself."],
    ["colgroup"])

add("thead", "Table Header Row Group", "Tables",
    "Groups the header rows of a table.",
    "<thead>  contains the header rows (usually <tr> with <th scope=\"col\">). When a table is tall, browsers can repeat <thead> on each printed page.",
    [],
    '<table>\n  <thead><tr><th>Name</th><th>Role</th></tr></thead>\n  <tbody>…</tbody>\n</table>',
    '<div style="font-size:11px;display:flex"><div style="border:1px solid #d1d5db;background:#f3f4f6;font-weight:700;padding:4px 10px">Name</div><div style="border:1px solid #d1d5db;background:#f3f4f6;font-weight:700;padding:4px 10px">Role</div></div>',
    ["Print: thead repeats automatically per page in most browsers."],
    ["tbody", "tfoot", "tr"])

add("tbody", "Table Body Row Group", "Tables",
    "Groups the body (data) rows of a table.",
    "<tbody>  wraps the data rows. A table may have several <tbody> blocks (e.g. to group sections of rows). Browsers insert one implicitly if you omit it.",
    [],
    '<table>\n  <thead>…</thead>\n  <tbody><tr><td>Row 1</td></tr></tbody>\n  <tbody class="totals"><tr><td>Total</td></tr></tbody>\n</table>',
    '<div style="font-size:11px"><div style="border:1px solid #e5e7eb;padding:4px 10px">Row 1</div><div style="border:1px solid #e5e7eb;padding:4px 10px;background:#f9fafb;font-weight:600">Total</div></div>',
    ["Multiple <tbody> = visual row groups (style each differently)."],
    ["thead", "tfoot", "tr"])

add("tfoot", "Table Footer Row Group", "Tables",
    "Groups the footer (summary) rows of a table.",
    "<tfoot>  holds summary/footer rows (totals, notes). It renders after <tbody> even if written before it in the source.",
    [],
    '<table>\n  <tfoot><tr><th>Total</th><td>$26,500</td></tr></tfoot>\n  <tbody>…</tbody>\n</table>',
    '<div style="font-size:11px;border-top:2px solid #374151;display:flex"><div style="padding:4px 10px;font-weight:700">Total</div><div style="padding:4px 10px">$26,500</div></div>',
    ["Written first, rendered last — the browser reorders it."],
    ["thead", "tbody", "tr"])

add("tr", "Table Row", "Tables",
    "A single row inside a table body/head/footer.",
    "<tr>  is one row. Its children are <th>/<td> (and technically <caption> is allowed inside tr but useless). Row groups: thead/tbody/tfoot.",
    [("align", "—", "Obsolete; use CSS text-align."),
     ("valign", "—", "Obsolete; use CSS vertical-align.")],
    '<tr><td>Aug</td><td>$12,400</td></tr>',
    '<div style="font-size:11px;display:flex;border-top:1px solid #e5e7eb"><div style="padding:4px 10px;flex:1">Aug</div><div style="padding:4px 10px;flex:1">$12,400</div></div>',
    ["Cells per row should match the column count."],
    ["td", "th", "tbody"])

add("th", "Table Header Cell", "Tables",
    "A header cell — labels a row or a column.",
    "<th>  is a header cell. scope declares what it labels: scope=\"col\" (labels the column below) or scope=\"row\" (labels the row across). Without scope, screen readers can't tell what the header means.",
    [("scope", "col / row / colgroup / rowgroup", "What the header labels. col is the default."),
     ("abbr", "—", "Obsolete (was: abbreviated header title)."),
     ("colspan", "integer", "Span this many columns (default 1)."),
     ("rowspan", "integer", "Span this many rows (default 1).")],
    '<table>\n  <tr><th scope="col">Name</th><th scope="col">Score</th></tr>\n  <tr><th scope="row">Ali</th><td>92</td></tr>\n  <tr><th colspan="2">Top scorer: Ali</th></tr>\n</table>',
    '<table style="border-collapse:collapse;font-size:11px"><tr><th style="border:1px solid #d1d5db;background:#f3f4f6;padding:4px 10px">Name</th><th style="border:1px solid #d1d5db;background:#f3f4f6;padding:4px 10px">Score</th></tr><tr><th style="border:1px solid #e5e7eb;padding:4px 10px;background:#fafafa">Ali</th><td style="border:1px solid #e5e7eb;padding:4px 10px">92</td></tr><tr><td colspan="2" style="border:1px solid #e5e7eb;padding:4px 10px;background:#eff6ff;font-weight:600">Top scorer: Ali</td></tr></table>',
    ["Always set scope on th — it is the difference between an accessible table and a data soup."],
    ["td", "tr"])

add("td", "Table Data Cell", "Tables",
    "A standard data cell.",
    "<td>  is a data cell. colspan/rowspan merge cells across columns/rows — use sparingly, they complicate screen-reader navigation.",
    [("colspan", "integer", "Span this many columns."),
     ("rowspan", "integer", "Span this many rows."),
     ("headers", "ID list", "IDs of the th cells that describe this td (for complex tables).")],
    '<tr><td rowspan="2">Q1</td><td>Jan</td></tr>\n<tr><td>Feb</td></tr>',
    '<table style="border-collapse:collapse;font-size:11px"><tr><td rowspan="2" style="border:1px solid #d1d5db;padding:4px 10px;background:#fef9c3">Q1</td><td style="border:1px solid #e5e7eb;padding:4px 10px">Jan</td></tr><tr><td style="border:1px solid #e5e7eb;padding:4px 10px">Feb</td></tr></table>',
    ["headers=\"id1 id2\" links a cell to its header(s) in complex tables."],
    ["th", "tr"])

# ---------------- LEGACY / OBSOLETE ----------------
def legacy(t, n, d, ex, dm, tip):
    add(t, n, "Legacy & Obsolete", f"Legacy/obsolete element: {n}.",
        d,
        [("—", "—", "No meaningful attributes — do not use.")],
        ex, dm,
        [tip],
        [], st="obsolete")

legacy("font", "Font (obsolete)",
    "Obsolete. Set font-family/size/color via CSS. Replaced by <span> + CSS.",
    "<font face=\"Arial\" color=\"red\">text</font>",
    '<span style="font-family:serif;color:#ef4444;font-size:13px">Legacy: <font> is dead — use CSS</span>',
    "Use <span> + font-family/color in CSS.")

legacy("center", "Center (obsolete)",
    "Obsolete. Centering is done with CSS: text-align or margin: 0 auto / flex.",
    "<center>Centered text</center>",
    '<div style="text-align:center;font-size:13px;background:#f3f4f6;padding:6px">Centered via CSS, not &lt;center&gt;</div>',
    "text-align: center (text) or margin-inline: auto (blocks).")

legacy("marquee", "Marquee (obsolete)",
    "Obsolete and non-standard. Scrolling text is done with CSS animation (or not at all — it is an a11y hazard).",
    "<marquee>Scrolling text</marquee>",
    '<div style="overflow:hidden;background:#111827;border-radius:6px;height:28px"><span style="display:inline-block;color:#fbbf24;font-size:12px;padding-left:100%;animation:none">Scrolling text — do the same with CSS keyframes + translateX</span></div>',
    "If you must scroll, use a CSS animation and respect prefers-reduced-motion.")

legacy("big", "Big (obsolete)",
    "Obsolete. Make text bigger with CSS font-size.",
    "<big>Bigger text</big>",
    '<span style="font-size:15px">Bigger text — via CSS font-size</span>',
    "font-size in CSS.")

legacy("blink", "Blink (obsolete)",
    "Obsolete (removed). Blinking text was an accessibility disaster — do not recreate it.",
    "<blink>Blinking</blink>",
    '<span style="font-size:13px;color:#9ca3af">Blink no longer exists — and blinking text hurts accessibility.</span>',
    "Draw attention with color/weight/position — not flashing.")

legacy("strike", "Strike (obsolete)",
    "Obsolete. Strikethrough is <s> or CSS text-decoration: line-through.",
    "<strike>Struck text</strike>",
    '<span style="text-decoration:line-through;font-size:13px">Struck text — use <s> or CSS</span>',
    "<s> for “no longer accurate”, CSS line-through for style.")

legacy("tt", "Teletype (obsolete)",
    "Obsolete. Monospace text is <code>/<kbd> or CSS font-family: monospace.",
    "<tt>teletype</tt>",
    '<span style="font-family:monospace;font-size:13px">teletype — use <code> or CSS</span>',
    "<code> for code, CSS monospace stacks for anything else.")

legacy("acronym", "Acronym (obsolete)",
    "Obsolete. HTML5 merged <acronym> into <abbr>.",
    "<acronym title=\"World Wide Web\">WWW</acronym>",
    '<span style="font-size:13px"><abbr title="World Wide Web" style="text-decoration:underline dotted;cursor:help">WWW</abbr> — use <abbr> now</span>',
    "Use <abbr title=\"…\">.")

legacy("frame", "Frame (obsolete)",
    "Obsolete. Frames were replaced by <iframe> (single) and good layout practice.",
    '<frameset><frame src="nav.html"><frame src="main.html"></frameset>',
    '<div style="font-family:monospace;font-size:11px;background:#fef2f2;border:1px solid #fecaca;border-radius:6px;padding:8px">frameset/frame → dead since HTML5. Use <iframe> or real CSS layout.</div>',
    "Modern layout: CSS grid/flex + <iframe> for embedded documents only.")

legacy("frameset", "Frame Set (obsolete)",
    "Obsolete. Divided the window into <frame> panes — dead with HTML5.",
    '<frameset cols="20%,80%"><frame src="a.html"><frame src="b.html"></frameset>',
    '<div style="display:flex;font-size:11px;font-family:monospace;height:30px"><div style="width:20%;background:#e5e7eb">nav</div><div style="flex:1;background:#f9fafb">main</div><span style="position:absolute;margin-top:40px;color:#6b7280">the above: what people did with framesets — now a CSS grid</span></div>',
    "CSS grid/flex layout.")

legacy("noframes", "No Frames Fallback (obsolete)",
    "Obsolete. Fallback content for browsers without frames — irrelevant today.",
    "<noframes>Your browser doesn't support frames.</noframes>",
    '<div style="font-size:12px;color:#9ca3af">Frames are gone — so is <noframes>.</div>',
    "Remove it.")

legacy("applet", "Applet (obsolete)",
    "Obsolete. Ran Java applets in the page — Java in browsers is dead.",
    "<applet code=\"Game.class\" width=200 height=100></applet>",
    '<div style="font-size:12px;color:#9ca3af">Java applets: extinct. Games are now <canvas>/WebGL/JS.</div>',
    "<canvas> / WebGL / JavaScript.")

legacy("basefont", "Base Font (obsolete)",
    "Obsolete. Set the default font via CSS on body (font-family/size).",
    "<basefont face=\"Verdana\" size=\"2\">",
    '<div style="font-size:12px">body { font-family: Verdana; font-size: 14px; } — that replaced <basefont></div>',
    "CSS on the root/body.")

legacy("isindex", "Single Index Prompt (obsolete)",
    "Obsolete. A single-page search prompt from the HTML 2 era.",
    "<isindex prompt=\"Search: \">",
    '<div style="font-size:12px;color:#9ca3af">“Search: [________]” — from 1993. Use a real form.</div>',
    "<form> + <input> + <button>.")

legacy("nextid", "NextID (obsolete)",
    "Obsolete. Hints where to continue reading — no modern equivalent.",
    "<nextid href=\"part2.html\">",
    '<div style="font-size:12px;color:#9ca3af">No longer in the spec — just use links.</div>',
    "Plain <a> links.")

legacy("dir", "Directory List (obsolete)",
    "Obsolete. A two-level list — replaced by <ul>/<ol> + CSS.",
    "<dir><item>a</item><item>b</item></dir>",
    '<div style="font-size:12px">Use <ul>/<ol> and style with CSS list-style.</div>',
    "<ul>/<ol>.")

# ---------------- MISC / WEB COMPONENTS ----------------
add("menu", "Menu / Command List", "Lists",
    "A list of commands or items (context menus); behaves like <ul>.",
    "<menu>  originally meant a context menu (type=\"context\"). In practice it renders like an unordered list and is rarely needed — use <ul> unless you have a real command list.",
    [("type", "context / toolbar", "context = user-initiated menu (no browser support), toolbar = deprecated.")],
    "<menu><li>New</li><li>Open…</li><li>Save</li></menu>",
    '<div style="font-size:12px;border:1px solid #d1d5db;border-radius:6px;box-shadow:0 4px 12px rgba(0,0,0,.12);padding:4px;min-width:110px"><div style="padding:4px 10px;border-radius:4px;background:#eff6ff">New</div><div style="padding:4px 10px">Open…</div><div style="padding:4px 10px">Save</div></div>',
    ["<li> is the only valid child (like <ul>)."],
    ["ul", "li"])

add("slot", "Shadow DOM Slot", "Web Components",
    "A placeholder in a shadow DOM template where light-DOM content is projected.",
    "<slot>  marks where a shadow DOM template expects content. Light-DOM children of the host element are projected into matching slots (named slots match via the slot attribute).",
    [("name", "string", "Slot name; matches the slot attribute on projected children.")],
    '<template shadowrootmode="open">\n  <style>span { color: teal; }</style>\n  <span><slot></slot></span>\n</template>\n<my-comp>Hello shadow</my-comp>',
    '<span style="color:#0d9488;font-size:13px">Hello shadow <i>(projected into the slot)</i></span>',
    ["slot fallback content shows when nothing is projected in."],
    ["template"])
