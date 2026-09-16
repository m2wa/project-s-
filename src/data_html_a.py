# -*- coding: utf-8 -*-
# HTML elements — Part A: Document Metadata, Document Structure, Text & Inline
# Compiled from: W3Schools HTML, GeeksforGeeks HTML5, TutorialsPoint HTML5,
# freeCodeCamp HTML5 course, Osama Elzero (Elzero Web School), Abdelrahman Gamal.

E = []

def add(t, n, cat, s, d, attrs, ex, dm, notes=(), rel=(), st="standard"):
    E.append(dict(t=t, n=n, cat=cat, s=s, d=d, A=list(attrs), ex=ex, dm=dm,
                  notes=list(notes), rel=list(rel), st=st))

# ---------------- DOCUMENT METADATA ----------------
add("html", "Root Element", "Document Metadata",
    "The root element of every HTML document.",
    "<html> is the top-level element that wraps everything else on the page. It normally has two children: <head> (metadata the browser uses) and <body> (the visible content).",
    [("lang", "BCP-47 code", "Declares the page language, e.g. lang=\"en\" or lang=\"ar\". Used by screen readers, speech and search engines."),
     ("dir", "ltr / rtl", "Optional. Sets the base text direction; default comes from lang."),
     ("xmlns", "URL", "Not required in HTML5. Historically declared the HTML namespace on XHTML.")],
    '<html lang="en">\n  <head>...</head>\n  <body>...</body>\n</html>',
    '<div style="font-family:monospace;background:#f6f8fa;padding:10px;border:1px solid #d0d7de">&lt;html&gt; &rarr; &lt;head&gt; + &lt;body&gt;</div>',
    ["Always set lang — it is your first accessibility and SEO win.", "Exactly one <html> element per document."],
    ["head", "body"])

add("head", "Document Head", "Document Metadata",
    "Container for all machine-oriented information about the document.",
    "<head> holds metadata that is not rendered on the page: the title, character encoding, viewport, stylesheets, scripts, and other machine-readable information. It sits between <html> and <body>.",
    [],
    '<head>\n  <meta charset="UTF-8">\n  <title>My Page</title>\n</head>',
    '<div style="font-family:monospace;background:#f6f8fa;padding:10px;border:1px solid #d0d7de">&lt;head&gt; = title + meta + link + style + script (invisible)</div>',
    ["Never put visible content inside <head>.", "Order: charset meta should be in the first 1024 bytes of the file."],
    ["title", "meta", "link", "style", "script"])

add("title", "Document Title", "Document Metadata",
    "Defines the document title, shown in the browser tab and search results.",
    "<title> is required in every HTML document. Its text appears in the browser tab, bookmarks, and as the default headline in search engine results. It is the single most important on-page SEO element.",
    [],
    "<title>Learn HTML — 8000 Page Bible</title>",
    '<div style="background:#202124;color:#fff;padding:8px 14px;border-radius:8px 8px 0 0;display:flex;gap:10px;align-items:center"><span style="width:16px;height:16px;border-radius:50%;background:#4285f4"></span><b style="font-size:13px">Learn HTML — 8000 Page Bible</b> <span style="margin-left:auto">✕</span></div>',
    ["Exactly one <title> per document, inside <head>.", "Keep it under ~60 characters so it is not truncated in search results."],
    ["head"])

add("base", "Document Base", "Document Metadata",
    "Sets the base URL for all relative URLs on the page.",
    "<base> is optional. When present, every relative URL (links, images, stylesheets) is resolved against its href. It can also define the default target for links. Use with care — it changes the meaning of every relative URL.",
    [("href", "URL", "Base URL. Must be an absolute URL if target is used."),
     ("target", "window name", "e.g. _blank — default target for all links without a target attribute.")],
    '<base href="https://docs.example.com/" target="_blank">',
    '<div style="font-family:monospace;background:#f6f8fa;padding:10px;border:1px solid #d0d7de">base URL = https://docs.example.com/ → &lt;img src="a.png"&gt; loads docs.example.com/a.png</div>',
    ["Only one <base> per document, and it must come before any element with a URL."],
    ["head"])

add("link", "External Resource Link", "Document Metadata",
    "Links an external resource, most commonly a stylesheet.",
    "<link> connects the document to outside resources: CSS stylesheets, site icons (favicons), preloads of fonts and scripts, and feed manifests. In <head> it is the standard way to include a stylesheet.",
    [("rel", "keyword", "Relationship: stylesheet, icon, preload, preconnect, manifest, alternate, dns-prefetch."),
     ("href", "URL", "URL of the linked resource."),
     ("type", "MIME type", "e.g. text/css for stylesheets."),
     ("media", "media query", "e.g. media=\"print\" or media=\"(max-width:600px)\"."),
     ("as", "resource type", "For preload/preconnect: style, script, font, image, fetch, script."),
     ("crossorigin", "keyword", "anonymous / use-credentials — for cross-origin preload.")],
    '<link rel="stylesheet" href="style.css">\n<link rel="icon" href="logo.svg">',
    '<div style="display:flex;gap:8px;align-items:center"><span style="width:18px;height:18px;border-radius:4px;background:linear-gradient(135deg,#4285f4,#34a853)"></span><code style="font-family:monospace;font-size:12px">style.css → linked</code></div>',
    ["rel=\"preload\" fetches early; rel=\"preconnect\" warms the network connection.", "Favicon: use <link rel=\"icon\"> before <title>."],
    ["meta", "style", "title"])

add("meta", "Metadata", "Document Metadata",
    "Machine-readable metadata about the document (encoding, viewport, description, authors).",
    "<meta> carries information for the browser, search engines and social networks. Key uses: character set, viewport for mobile, page description, author, theme color, Open Graph and Twitter card tags.",
    [("charset", "character set", "charset=\"UTF-8\" — should be the very first thing in <head>."),
     ("name", "keyword", "viewport, description, author, robots, theme-color, color-scheme, keywords."),
     ("content", "string", "Value for the named meta, e.g. content=\"width=device-width, initial-scale=1\"."),
     ("http-equiv", "header name", "e.g. Content-Security-Policy, refresh, X-UA-Compatible (legacy).")],
    '<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<meta name="description" content="A huge HTML+CSS reference.">',
    '<div style="font-family:monospace;font-size:12px;background:#f6f8fa;padding:10px;border:1px solid #d0d7de">charset=UTF-8<br>viewport=width=device-width<br>description="A huge HTML+CSS reference."</div>',
    ["Viewport meta is mandatory for responsive design.", "Social sharing: add og:title, og:description, og:image, og:url."],
    ["title", "head"])

add("style", "Embedded Styles", "Document Metadata",
    "CSS rules that apply to the current document.",
    "<style> contains CSS written directly in the HTML. It is handy for small or one-off styles; for real projects, keep CSS in external files linked with <link> so it can be cached. <style> is also used inside server-side templates and components.",
    [("media", "media query", "Applies the rules only when the query matches, e.g. media=\"print\"."),
     ("type", "MIME type", "Historical; defaults to text/css.")],
    "<style>\n  body { font-family: system-ui; }\n  h1 { color: teal; }\n</style>",
    '<h1 style="margin:6px 0;color:teal;font-size:20px">Styled with &lt;style&gt;</h1><p style="margin:0;font-family:system-ui">body font set to system-ui</p>',
    ["External stylesheets are cacheable — prefer them for production."],
    ["link"])

add("script", "Executable Script", "Document Metadata",
    "Embeds or references executable JavaScript.",
    "<script> runs JavaScript in the page. It can contain inline code or point to an external file with src. Modern best practice: external file with defer (runs after parsing, in order) or async (runs as soon as downloaded).",
    [("src", "URL", "URL of the external script."),
     ("type", "MIME type", "text/javascript (default), module, text/json (data blocks), text/template."),
     ("defer", "boolean", "External scripts execute after HTML parsing, in document order."),
     ("async", "boolean", "External scripts execute as soon as they download."),
     ("nomodule", "boolean", "Skip this script in browsers that support modules."),
     ("crossorigin", "keyword", "anonymous / use-credentials for CORS.")],
    '<script src="app.js" defer></script>\n<script>\n  console.log("hi");\n</script>',
    '<div style="font-family:monospace;font-size:12px;background:#0d1117;color:#7ee787;padding:10px;border-radius:6px">console.log("hi");  →  "hi"</div>',
    ["defer keeps scripts from blocking rendering.", "Place scripts at the end of <body> or use defer — both work; pick one convention."],
    ["noscript", "module"])

add("noscript", "No-Script Fallback", "Document Metadata",
    "Content rendered only when scripting is disabled or unsupported.",
    "<noscript> shows its content only if JavaScript is off or the browser does not support it. Use it for fallback navigation links, a notice, or to hide script-only widgets gracefully.",
    [],
    "<noscript>You need to enable JavaScript to view this map.</noscript>",
    '<div style="font-size:13px;background:#fff8e1;border:1px solid #ffe082;color:#795548;padding:8px 12px;border-radius:6px">⚠ You need to enable JavaScript to view this map.</div>',
    ["<noscript> is allowed inside <body> and inside <head> (for <link> fallbacks)."],
    ["script"])

add("template", "Inert Content Template", "Document Metadata",
    "An inert container of markup that can be cloned by JavaScript.",
    "<template> holds HTML that is not rendered, not executed (scripts do not run, images do not load) until JavaScript clones its content. It is the standard building block for Web Components and JS-driven lists.",
    [("shadowrootmode", "open / closed", "Optional. If present, the template is the shadow root of a custom element.")],
    '<template id="card">\n  <div class="card"><h3></h3><p></p></div>\n</template>',
    '<div style="font-family:monospace;font-size:12px;background:#f6f8fa;border:2px dashed #8b949e;padding:10px;color:#57609a">&lt;template&gt; content is <b>inert</b> — rendered only when JS clones it into the DOM</div>',
    ["Content lives in a separate DocumentFragment — access it with template.content.", "Scripts inside <template> never auto-execute."],
    ["script"])

# ---------------- DOCUMENT STRUCTURE ----------------
add("body", "Document Body", "Document Structure",
    "Contains all the visible content of the HTML document.",
    "<body> is the container for everything the user sees: text, images, media, forms and layout elements. A document must have exactly one <body>, and it should come after <head>.",
    [],
    "<body>\n  <h1>Hello</h1>\n  <p>World</p>\n</body>",
    '<div style="border:2px solid #d0d7de;border-radius:8px;padding:12px;background:#fff"><h1 style="margin:0 0 6px;font-size:18px">Hello</h1><p style="margin:0;font-size:13px">Everything visible lives inside <b>&lt;body&gt;</b></p></div>',
    ["Exactly one <body> per document (browsers auto-insert it if missing)."],
    ["html", "main"])

add("div", "Generic Block Container", "Document Structure",
    "A neutral block-level container with no semantic meaning.",
    "<div> is the universal building block: it groups content for layout and styling without implying any meaning. Reach for semantic elements first; use <div> when no semantic element fits.",
    [],
    '<div class="card">\n  <h2>Card title</h2>\n  <p>Card text</p>\n</div>',
    '<div style="border:1px solid #d0d7de;border-radius:8px;padding:12px;background:#fafbfc;width:220px"><b style="font-size:13px">&lt;div class="card"&gt;</b><br><span style="font-size:12px;color:#57606a">a layout box with no meaning</span></div>',
    ["If you give it a class, it starts to look like a component — keep the meaning in the class name (e.g. .card)."],
    ["span", "section"])

add("section", "Thematic Section", "Document Structure",
    "A thematic grouping of content, typically with a heading.",
    "<section> represents a self-contained block of content that belongs to the document outline — usually a chapter, section of a page, or tab panel. Give it a heading (h1–h6) when it should appear in the outline.",
    [],
    '<section>\n  <h2>Shipping</h2>\n  <p>We ship worldwide.</p>\n</section>',
    '<div style="border-left:4px solid #4285f4;padding:8px 12px;background:#f0f6ff;width:250px"><b style="font-size:13px">Shipping</b><br><span style="font-size:12px;color:#444">A thematic <b>section</b> of the page</span></div>',
    ["Use <div> instead when the grouping is only for styling.", "Nest <section> only when the inner content is itself a distinct thematic section."],
    ["article", "aside", "nav"])

add("article", "Self-Contained Composition", "Document Structure",
    "A complete, independent piece of content that makes sense on its own.",
    "<article> is for content that could be distributed or reused independently: a blog post, a news story, a forum comment, a product card, a review. If it would still make sense in an RSS feed or shared page, it is an article.",
    [],
    '<article>\n  <h2>My First Post</h2>\n  <p>Published by Ana on 2026-09-16</p>\n</article>',
    '<div style="border:1px solid #d0d7de;border-radius:8px;padding:12px;background:#fff;width:260px;box-shadow:0 1px 3px rgba(0,0,0,.08)"><b style="font-size:13px">My First Post</b><br><small style="color:#8b949e">by Ana · 2026-09-16</small><br><span style="font-size:12px">Self-contained: it could live in an RSS feed.</span></div>',
    ["Article vs section: article = independent content; section = part of the document's own structure."],
    ["section", "header", "footer", "time"])

add("aside", "Aside Content", "Document Structure",
    "Content tangentially related to the main content (sidebar, box, pull quote).",
    "<aside> holds content that is related to, but separable from, the surrounding content: sidebars, callout boxes, lists of links, advertisements, or a \"related posts\" module.",
    [],
    '<aside>\n  <h3>Did you know?</h3>\n  <p>HTML5 added 40+ new elements.</p>\n</aside>',
    '<div style="background:#fff3e0;border:1px solid #ffcc80;padding:10px 12px;border-radius:8px;width:230px"><b style="font-size:12px">Did you know?</b><br><span style="font-size:12px">An <b>aside</b> box — related but optional.</span></div>',
    ["An <aside> can sit inside an <article> (related to that article) or outside (related to the whole page)."],
    ["article", "section"])

add("nav", "Navigation Block", "Document Structure",
    "A major block of navigation links.",
    "<nav> marks up a section of the page that consists of major navigation links: the main menu, table of contents, breadcrumbs, or pagination. Not every group of links is a <nav> — only major navigation.",
    [],
    '<nav>\n  <ul>\n    <li><a href="/">Home</a></li>\n    <li><a href="/about">About</a></li>\n  </ul>\n</nav>',
    '<nav style="background:#1f2937;border-radius:8px;padding:6px 4px;display:flex;gap:4px"><a href="#" style="color:#d1d5db;font-size:12px;text-decoration:none;padding:6px 10px;background:#374151;border-radius:6px">Home</a><a href="#" style="color:#d1d5db;font-size:12px;text-decoration:none;padding:6px 10px">About</a><a href="#" style="color:#d1d5db;font-size:12px;text-decoration:none;padding:6px 10px">Contact</a></nav>',
    ["Use role=\"navigation\" only if you cannot use <nav> (rare).", "A page may have several <nav> blocks (header menu, footer menu, pagination)."],
    ["ul", "a", "header"])

add("header", "Header Block", "Document Structure",
    "Introductory content or a set of navigational links for a section or page.",
    "<header> contains introductory material: the page title, a logo, a tagline, or a navigation menu. It may appear once for the whole page, or inside an <article>/<section> to head that section. It must not be nested inside another <header> or <footer>.",
    [],
    '<header>\n  <h1>My Blog</h1>\n  <nav>...</nav>\n</header>',
    '<div style="background:linear-gradient(90deg,#4285f4,#34a853);border-radius:8px;padding:12px;color:#fff"><b style="font-size:15px">My Blog</b><div style="font-size:11px;opacity:.85;margin-top:2px">header — intro content for the page</div></div>',
    ["<header> cannot contain <footer> or another <header> as a direct descendant."],
    ["footer", "nav", "h1"])

add("footer", "Footer Block", "Document Structure",
    "Footer content for a page or section: copyright, contact, related links.",
    "<footer> holds the closing content of a page or section: author info, copyright, table of contents, and related links. It may appear once per page or once per <article>/<section>.",
    [],
    '<footer>\n  <p>© 2026 Mega Book Inc.</p>\n</footer>',
    '<div style="background:#111827;color:#9ca3af;border-radius:8px;padding:10px 14px;font-size:12px;text-align:center">© 2026 Mega Book Inc. — <i>footer</i></div>',
    ["A footer inside an article describes that article, not the whole page."],
    ["header", "article"])

add("main", "Main Content", "Document Structure",
    "The dominant, unique content of the document.",
    "<main> wraps the primary content of the page — the part users care about, excluding sidebars, menus, footers and headers. There must be exactly one visible <main> per page. Screen-reader users can jump straight to it.",
    [("hidden", "boolean", "Hides the element (used for A/B testing duplicate mains).")],
    "<main>\n  <article>...the post...</article>\n</main>",
    '<div style="border:2px solid #4285f4;border-radius:8px;padding:12px;background:#f8fbff;width:260px"><b style="color:#1a56db;font-size:12px">MAIN CONTENT</b><br><span style="font-size:12px">Everything the user came here for lives inside <b>&lt;main&gt;</b>.</span></div>',
    ["Only one visible <main> per page — it is a landmark for assistive tech."],
    ["article", "section"])

add("address", "Contact Information", "Document Structure",
    "Contact information for the author/owner of an article or page.",
    "<address> provides contact details: a physical address, email, phone, or social links. It is not for arbitrary addresses (e.g. in a form about someone else). Browsers render it in italic by default.",
    [],
    '<address>\n  <a href="mailto:hi@example.com">hi@example.com</a> · Cairo, EG\n</address>',
    '<div style="font-style:italic;font-size:13px;border:1px solid #d0d7de;border-radius:6px;padding:8px 12px;background:#fafbfc"><a href="#" style="color:#1a56db">hi@example.com</a> · Cairo, Egypt</div>',
    ["Italic by default — override with CSS if your design needs it."],
    ["article"])

add("figure", "Figure with Caption", "Document Structure",
    "Self-contained media (image, diagram, code) with an optional caption.",
    "<figure> marks content referenced from the main flow: an image with its caption, a diagram, a code listing, a chart. Pair it with <figcaption> to caption it. It is usually displayed as a block.",
    [],
    '<figure>\n  <img src="chart.png" alt="Revenue 2026">\n  <figcaption>Figure 1: Revenue 2026</figcaption>\n</figure>',
    '<div style="border:1px solid #d0d7de;border-radius:8px;padding:10px;background:#fff;width:250px"><div style="height:70px;background:linear-gradient(90deg,#c3d4f5 0 20%,#a7c4f0 0 45%,#8ab4ec 0 70%,#6da3e8 0 100%);border-radius:4px"></div><div style="font-size:11px;color:#6b7280;margin-top:6px">Figure 1: Revenue 2026 (chart)</div></div>',
    ["<figcaption> must be the first or last child of <figure>."],
    ["figcaption", "img", "pre"])

add("figcaption", "Figure Caption", "Document Structure",
    "The caption for a <figure>.",
    "<figcaption> gives a title or description to a <figure>. It must be the first or last child of the figure, and can contain phrasing content.",
    [],
    "<figure><img src=\"a.png\"><figcaption>Sunrise in Cairo</figcaption></figure>",
    '<div style="font-size:11px;color:#6b7280;border-top:1px solid #e5e7eb;padding-top:4px;width:250px">Sunrise in Cairo — <i>the figcaption</i></div>',
    ["One <figcaption> per <figure>, as first or last child."],
    ["figure"])

for i in range(1, 7):
    add(f"h{i}", f"Heading Level {i}", "Document Structure",
        f"A section heading of importance level {i} (h1 = highest).",
        f"<h{i}> creates a heading of level {i}. Headings form the document outline that browsers, search engines and screen readers use to navigate the page. Use them in order (h1 → h2 → h3), never skip levels to change size." if i == 1 else
        f"<h{i}> is a heading of level {i} — used for sub-sections inside content headed by lower numbers. The browser renders it progressively smaller and bolder. Always keep heading levels ordered (no h1 → h4 jumps).",
        [],
        f"<h{i}>Heading level {i}</h{i}>",
        f'<div style="font-weight:700;font-size:{26-i*2.5}px;line-height:1.25;margin:2px 0">Heading level {i}</div>',
        ["Style headings with CSS (font-size) — never pick a level because of its default size."],
        ["p", "section", "article"])

add("p", "Paragraph", "Document Structure",
    "A block of text — the basic unit of written content.",
    "<p> is a paragraph. The browser adds vertical margin above and below it automatically. A <p> can contain phrasing content (text, inline elements, media) but not other block elements like <div>, <p> or <h1>.",
    [],
    "<p>This is a paragraph of text.</p>",
    '<p style="margin:0;font-size:13px;line-height:1.6">A <b>&lt;p&gt;</b> is a paragraph. The browser adds vertical space around it automatically.</p>',
    ["No line breaks are needed between <p> elements.", "Never nest block elements inside <p> — the browser will close it early."],
    ["span", "a"])

add("hr", "Horizontal Rule", "Document Structure",
    "A thematic break between paragraphs (scene change, topic shift).",
    "<hr> is a horizontal line that separates content at a thematic break: a scene change in a story, a topic shift in an article. It is not just a design line — it carries meaning for assistive tech.",
    [("align", "—", "Obsolete/deprecated. Use CSS margin/border instead."),
     ("width", "—", "Obsolete/deprecated. Use CSS width instead."),
     ("size", "—", "Obsolete/deprecated. Use CSS height instead.")],
    "<p>Before the break.</p>\n<hr>\n<p>After the break.</p>",
    '<div style="font-size:13px"><p style="margin:0 0 6px">Before the break.</p><hr style="border:none;border-top:2px solid #d1d5db;margin:8px 0"><p style="margin:0">After the break.</p></div>',
    ["Meaning: thematic break, not decoration. For decoration use a styled div."],
    ["p"])

add("br", "Line Break", "Document Structure",
    "A single line break (forced newline) in the text.",
    "<br> forces a line break where it occurs. Use it only where a break belongs in the content itself: postal addresses, poetry, signatures — not for layout spacing (that is CSS's job).",
    [],
    "<address>12 Main St.<br>Cairo, Egypt<br>12611</address>",
    '<div style="font-size:12px;line-height:1.5;background:#fafbfc;border:1px solid #e5e7eb;padding:8px;border-radius:6px">12 Main St.<br>Cairo, Egypt<br>12611</div>',
    ["Layout spacing → CSS margin/padding, never stacked <br> tags."],
    ["wbr", "pre"])

add("wbr", "Word Break Opportunity", "Document Structure",
    "An optional line-break position inside long words/URLs.",
    "<wbr> hints to the browser that it may break the line at that point, without forcing a break. Ideal for long URLs and compound words that would otherwise overflow narrow screens.",
    [],
    "<a href=\"https://example.com/very/long/path\">https://example<wbr>.com/very/long/path</a>",
    '<div style="width:110px;font-size:12px;word-break:break-word">https://example<wbr>.com/very/wbr/allows/line-breaks/here</div>',
    ["<wbr> suggests, it does not force — the browser decides."],
    ["br"])

add("pre", "Preformatted Text", "Document Structure",
    "Preformatted text where whitespace and line breaks matter (code, diagrams).",
    "<pre> preserves exactly the whitespace and newlines written in the source and renders in a monospace font. Use it for code listings, ASCII art, and log output. Inner content is parsed as flow content, so you can style inline highlights with <code>, <span>, etc.",
    [("type", "—", "Deprecated; the type attribute never did what people expected.")],
    '<pre><code>function sum(a, b) {\n  return a + b;\n}</code></pre>',
    '<pre style="background:#0d1117;color:#e6edf3;font-size:11px;padding:10px;border-radius:6px;margin:0">function sum(a, b) {\n  return a + b;\n}</pre>',
    ["Whitespace in the HTML source is visible — indent code with real spaces, not tabs-only assumptions."],
    ["code", "figure"])

add("blockquote", "Block Quotation", "Document Structure",
    "A section quoted from another source.",
    "<blockquote> marks a longer quotation taken from another source. Cite it with the cite attribute (the source URL) and/or show the source in the content (with <cite>). Use <q> for short inline quotations instead.",
    [("cite", "URL", "URL of the source of the quotation (not the displayed text).")],
    '<blockquote cite="https://www.w3.org/">The power to affect the world...</blockquote>',
    '<div style="border-left:4px solid #6b7280;margin-left:8px;padding-left:12px;color:#374151;font-size:13px;font-style:italic">“The power to affect the world comes from the ability to connect people.”</div>',
    ["cite = the URL of the source; the attribution text goes in the content."],
    ["q", "cite"])

add("details", "Disclosure Widget", "Document Structure",
    "A native disclosure (collapse/expand) widget — no JavaScript needed.",
    "<details> shows a summary and hides its content until the user clicks. With open it starts expanded. It is the built-in accordion: great for FAQs, settings panels and tooltips.",
    [("open", "boolean", "Starts the disclosure expanded."),
     ("name", "string", "Groups <details> widgets in the same radio-like group (newer feature).")],
    '<details>\n  <summary>What is HTML?</summary>\n  <p>The markup language of the web.</p>\n</details>',
    '<details open style="border:1px solid #d1d5db;border-radius:6px;padding:8px 12px;font-size:13px;width:240px"><summary><b>What is HTML?</b></summary><p style="margin:6px 0 0">The markup language of the web.</p></details>',
    ["Zero-JS accordion — the browser handles a11y for you.", "Only <summary> is always visible; the rest toggles."],
    ["summary"])

add("summary", "Summary / Caption", "Document Structure",
    "The visible caption of a <details> disclosure.",
    "<summary> is the part of a <details> widget that is always shown and clickable. It labels the disclosure (like an accordion header). It must be the first child of its <details> parent.",
    [],
    "<details><summary>FAQ</summary><p>Answer...</p></details>",
    '<div style="font-size:13px">Click ▸ <b>FAQ</b> to expand — <i>summary is the label</i></div>',
    ["Must be the first child of <details>."],
    ["details"])

add("dialog", "Native Dialog", "Document Structure",
    "A native dialog box: modal when shown with showModal(), non-modal when shown with show().",
    "<dialog> is the HTML5 native dialog. Calling el.show() displays it inline; el.showModal() displays it as a modal with a ::backdrop and focus trapping. Close it with el.close() or a <form method=\"dialog\">. Before HTML5 this required a lot of JavaScript.",
    [("open", "boolean", "Reflects whether the dialog is open."),
     ("method", "dialog", "On a <form> inside the dialog: closes the dialog with formValue.")],
    '<dialog id="dlg">\n  <form method="dialog">\n    <p>Are you sure?</p>\n    <button value="cancel">Cancel</button>\n    <button formnovalidate>OK</button>\n  </form>\n</dialog>',
    '<div style="width:240px;background:#fff;border:1px solid #d1d5db;border-radius:10px;box-shadow:0 8px 24px rgba(0,0,0,.18);padding:14px;font-size:13px"><b>Are you sure?</b><div style="margin-top:10px;text-align:right"><button style="border:1px solid #d1d5db;background:#f9fafb;border-radius:6px;padding:4px 10px;margin-right:6px;font-size:12px">Cancel</button><button style="border:none;background:#2563eb;color:#fff;border-radius:6px;padding:4px 12px;font-size:12px">OK</button></div></div>',
    ["showModal() gives focus trap + backdrop for free.", "Use <form method=\"dialog\"> to close with a value (event.returnValue)."],
    ["button", "form"])

# ---------------- TEXT & INLINE ----------------
add("span", "Generic Inline Container", "Text & Inline",
    "A neutral inline container with no meaning.",
    "<span> is the inline cousin of <div>: it wraps a run of text for styling or scripting without adding meaning. Use it when no semantic inline element (<strong>, <code>, <mark>...) fits.",
    [],
    '<p>Total: <span class="price">$49</span></p>',
    '<p style="margin:0;font-size:13px">Total: <span style="color:#16a34a;font-weight:700">$49</span> <span style="color:#9ca3af;text-decoration:line-through;font-size:11px">$60</span></p>',
    ["Prefer semantic elements; <span> is the fallback."],
    ["div", "b", "i"])

add("b", "Stylistic Emphasis (no importance)", "Text & Inline",
    "Highlights text for utilitarian reasons without extra importance.",
    "<b> draws attention to text for reasons like keywords, product names, or lead words — without the stress emphasis of <strong>. It renders bold by default but carries no importance semantics.",
    [("part", "—", "Global attribute, see Global Attributes.")],
    "<p>The <b>Cairo</b> branch opens at 9am.</p>",
    '<p style="margin:0;font-size:13px">The <b>Cairo</b> branch opens at 9am. — bold, but not “important”</p>',
    ["Use <strong> when the text is genuinely important."],
    ["strong", "i", "u"])

add("strong", "Strong Importance", "Text & Inline",
    "Marks text of strong importance, seriousness or urgency.",
    "<strong> indicates that its content has strong importance — screen readers may pronounce it differently. It renders bold by default, but its meaning is importance, not weight.",
    [],
    "<p><strong>Warning:</strong> This action cannot be undone.</p>",
    '<p style="margin:0;font-size:13px"><strong>Warning:</strong> This action cannot be undone.</p>',
    ["Meaning first: use it for urgent/important text, not just bold text."],
    ["b", "em"])

add("i", "Idiomatic Text", "Text & Inline",
    "Text in an alternate voice or mood (technical terms, foreign phrases, ship names).",
    "<i> marks a span of text in an alternate voice: a technical term, a foreign phrase, a taxonomic designation, or the name of a ship. It renders italic by default but is not emphasis.",
    [],
    "<p>The word <i>rendezvous</i> is borrowed from French.</p>",
    '<p style="margin:0;font-size:13px">The word <i>rendezvous</i> is borrowed from French.</p>',
    ["Use <em> for emphasis; <i> for a different voice."],
    ["em", "b"])

add("em", "Stress Emphasis", "Text & Inline",
    "Marks stress emphasis — change in meaning if removed.",
    "<em> stresses its content: removing it changes the sentence's meaning (“I love <em>you</em>” vs “I <em>love</em> you”). It renders italic by default and is announced as emphasized by screen readers.",
    [],
    "<p>I love <em>you</em>.</p>",
    '<p style="margin:0;font-size:13px">I love <em>you</em>. — <i>em changes who is stressed</i></p>',
    ["Nested <em><em> can indicate even stronger stress (browsers may bold it)."],
    ["i", "strong"])

add("u", "Unarticulated Annotation", "Text & Inline",
    "Non-extractive information: a spell-check red line, a signature.",
    "<u> is for text with a non-textual annotation that does not relate to emphasis or importance: misspelled words, names in Chinese social text, or a signature. It renders underlined by default — but for links and styling, use CSS.",
    [],
    "<p>My name is <u>Ali</u>.</p>",
    '<p style="margin:0;font-size:13px">My name is <u>Ali</u>. — underlined, no meaning</p>',
    ["Prefer text-decoration: underline in CSS for pure styling."],
    ["s", "b"])

add("s", "No Longer Accurate", "Text & Inline",
    "Marks text that is no longer accurate or relevant (not a strikethrough for style).",
    "<s> marks content that is no longer accurate: a price that was corrected, a cancelled event. It renders with a strikethrough. Use <del>/<ins> when you want to track the change over time.",
    [],
    "<p>Price: <s>$99</s> $79</p>",
    '<p style="margin:0;font-size:13px">Price: <s style="color:#9ca3af">$99</s> <b>$79</b></p>',
    ["Use <del> when you also want to record what was removed and when."],
    ["u", "del"])

add("small", "Side Comment / Small Print", "Text & Inline",
    "Side comments and small print: fine print, copyrights, legal notes.",
    "<small> shrinks its text by one font-size step by default and is intended for fine print — legal notes, copyrights, disclaimers — not for de-emphasizing content.",
    [],
    "<p>Offer ends Friday. <small>T&Cs apply.</small></p>",
    '<p style="margin:0;font-size:13px">Offer ends Friday. <small style="font-size:11px;color:#6b7280">T&amp;Cs apply.</small></p>',
    ["It is a style hint, not a meaning of “unimportant content”."],
    ["p"])

add("mark", "Highlighted Text", "Text & Inline",
    "Highlights text for reference, like a highlighter pen.",
    "<mark> highlights a span of text within the page — for example, the matched word in search results. It renders with a yellow background by default.",
    [],
    "<p>Search results for <mark>html</mark></p>",
    '<p style="margin:0;font-size:13px">Search results for <mark style="background:#fef08a;padding:0 2px;border-radius:2px">html</mark> on this page</p>',
    ["The standard use is search-result highlighting."],
    ["span"])

add("cite", "Title of a Work", "Text & Inline",
    "The title of a creative work (book, film, song, page).",
    "<cite> marks the title of a work: a book, film, song, article, or web page. It renders italic by convention.",
    [],
    '<p>Read <cite>Learn HTML5</cite> by freeCodeCamp.</p>',
    '<p style="margin:0;font-size:13px">Read <cite><i>Learn HTML5</i></cite> by freeCodeCamp.</p>',
    ["For a work's title — not for the author's name."],
    ["blockquote", "q"])

add("q", "Inline Quotation", "Text & Inline",
    "A short inline quotation (rendered with quotation marks).",
    "<q> marks a short inline quotation. Browsers add quotation marks automatically; the cite attribute points to the source URL.",
    [("cite", "URL", "Source URL of the quotation.")],
    '<p>As the docs say, <q cite="https://w3.org/">HTML is the skeleton</q>.</p>',
    '<p style="margin:0;font-size:13px">As the docs say, <q>HTML is the skeleton</q>.</p>',
    ["Use <blockquote> for multi-paragraph quotes."],
    ["blockquote"])

add("abbr", "Abbreviation", "Text & Inline",
    "An abbreviation or acronym, with its expansion in the title attribute.",
    "<abbr> marks an abbreviation. Putting the full form in the title attribute gives a native tooltip on hover: <abbr title=\"Hypertext Markup Language\">HTML</abbr>.",
    [("title", "string", "The expansion of the abbreviation — shows as a tooltip.")],
    "<abbr title=\"Hypertext Markup Language\">HTML</abbr>",
    '<p style="margin:0;font-size:13px"><abbr title="Hypertext Markup Language" style="text-decoration:underline dotted;cursor:help">HTML</abbr> — hover me for the tooltip</p>',
    ["Use <data> for machine-readable values, <abbr> for human expansions."],
    ["data"])

add("data", "Machine-Readable Value", "Text & Inline",
    "A machine-readable value behind human-readable text.",
    "<data> associates a machine-readable value (in the value attribute) with human-readable content: dates, weights, coordinates, IDs.",
    [("value", "string", "The machine-readable equivalent, e.g. value=\"2026-09-16\".")],
    '<p>Weight: <data value="85">85 kg</data></p>',
    '<p style="margin:0;font-size:13px">Weight: <span title="85">85 kg</span> — value=\"85\" is stored for machines</p>',
    ["value is what scripts and validators read."],
    ["abbr", "time"])

add("dfn", "Definition Term", "Text & Inline",
    "The term being defined on the page.",
    "<dfn> marks the defining instance of a term — the word a definition explains. It renders italic by convention. Pair it with <dd> in a <dl>, or wrap the term inside the defining sentence.",
    [],
    "<p><dfn>semantics</dfn>: the meaning of markup.</p>",
    '<p style="margin:0;font-size:13px"><dfn style="font-style:italic"><b>semantics</b></dfn>: the meaning carried by markup, not just its appearance.</p>',
    ["One <dfn> per term per page — it is the defining occurrence."],
    ["em", "dd"])

add("time", "Machine-Readable Time", "Text & Inline",
    "A machine-readable date, time, or duration (calendar integration).",
    "<time> wraps a human-readable date/time and stores it in datetime (or value for durations) so browsers and search engines can parse it: events, publish dates, countdowns.",
    [("datetime", "ISO date/time", "e.g. datetime=\"2026-09-16\" or \"2026-09-16T15:30\"."),
     ("value", "duration", "For durations: value=\"PT1H30M\" (1h30m).")],
    "<time datetime=\"2026-09-16\">16 September 2026</time>",
    '<p style="margin:0;font-size:13px">Published <time datetime="2026-09-16" style="color:#1a56db;font-weight:600">16 September 2026</time></p>',
    ["Use ISO 8601 in datetime — that's what machines parse."],
    ["data", "article"])

add("kbd", "Keyboard Input", "Text & Inline",
    "Represents user input, usually from a keyboard (shortcut keys).",
    "<kbd> represents input the user should provide, typically keyboard shortcuts. It renders monospace, often styled as a key cap.",
    [],
    "<p>Press <kbd>Ctrl</kbd> + <kbd>S</kbd> to save.</p>",
    '<p style="margin:0;font-size:13px">Press <kbd style="font-family:monospace;border:1px solid #d1d5db;border-bottom-width:2px;border-radius:4px;padding:1px 6px;font-size:12px;background:#f9fafb">Ctrl</kbd> + <kbd style="font-family:monospace;border:1px solid #d1d5db;border-bottom-width:2px;border-radius:4px;padding:1px 6px;font-size:12px;background:#f9fafb">S</kbd> to save.</p>',
    ["<kbd> for keys, <samp> for sample output, <code> for source code."],
    ["samp", "code"])

add("samp", "Sample Output", "Text & Inline",
    "Sample output from a program or computer.",
    "<samp> marks sample output from a program, a quote from code, or a piece of system text — e.g. an error message a user should recognize.",
    [],
    "<p>If you see <samp>404 Not Found</samp>, the page is missing.</p>",
    '<p style="margin:0;font-size:13px">If you see <samp style="font-family:monospace;background:#fef2f2;color:#b91c1c;padding:1px 5px;border-radius:4px;font-size:12px">404 Not Found</samp>, the page is missing.</p>',
    ["Output, not input — for keys use <kbd>."],
    ["kbd", "code"])

add("code", "Fragment of Computer Code", "Text & Inline",
    "A fragment of computer code.",
    "<code> marks a short fragment of source code, a variable name, or a command in running text. It renders monospace. For multi-line listings, wrap it in <pre>.",
    [],
    "<p>Use <code>display: grid</code> for layouts.</p>",
    '<p style="margin:0;font-size:13px">Use <code style="font-family:monospace;background:#eef2ff;color:#4338ca;padding:1px 5px;border-radius:4px;font-size:12px">display: grid</code> for layouts.</p>',
    ["<pre><code> for full listings; <code> alone for inline snippets."],
    ["pre", "var"])

add("var", "Variable Name", "Text & Inline",
    "A variable in a math expression or program, or a user agent string.",
    "<var> marks a variable: a program variable, a mathematical variable, or a placeholder. It renders italic by convention, distinguishing it from the surrounding code.",
    [],
    "<p><code>price = <var>rate</var> × <var>qty</var></code></p>",
    '<p style="margin:0;font-size:13px">price = <var style="font-style:italic;font-family:monospace">rate</var> × <var style="font-style:italic;font-family:monospace">qty</var></p>',
    ["Distinguishes the variable from the code that uses it."],
    ["code"])

add("sub", "Subscript", "Text & Inline",
    "Subscript text (rendered below the baseline).",
    "<sub> places text below the baseline, smaller than the surrounding text: chemical formulas (H<sub>2</sub>O), mathematical subscripts.",
    [],
    "<p>H<sub>2</sub>O and x<sub>1</sub></p>",
    '<p style="margin:0;font-size:13px">H<sub>2</sub>O and x<sub>1</sub></p>',
    ["For math, prefer the <math> element (MathML)."],
    ["sup"])

add("sup", "Superscript", "Text & Inline",
    "Superscript text (rendered above the baseline).",
    "<sup> places text above the baseline, smaller: x<sup>2</sup>, footnotes, ordinals.",
    [],
    "<p>E = mc<sup>2</sup></p>",
    '<p style="margin:0;font-size:13px">E = mc<sup>2</sup></p>',
    ["Footnotes are usually <sup> + a link back."],
    ["sub"])

add("ruby", "Ruby Annotation", "Text & Inline",
    "Japanese/Chinese pinyin-style pronunciation annotation.",
    "<ruby> provides a small annotation (pronunciation or meaning) above or beside a base character — used for CJK text. <rt> holds the annotation, <rp> holds fallback parentheses for old browsers.",
    [],
    '<ruby>中<rt>zhōng</rt></ruby><ruby>国<rt>guó</rt></ruby>',
    '<div style="font-size:13px;font-family:serif"><ruby>中<rt style="font-size:9px">zhōng</rt></ruby>国<rp>(</rp><rt style="font-size:9px">guó</rt><rp>)</rp></div>',
    ["Supported mainly for CJK languages."],
    ["rt", "rp"])

add("rt", "Ruby Text", "Text & Inline",
    "The annotation text inside <ruby>.",
    "<rt> is the annotation (reading/pronunciation) inside a <ruby> element. It renders smaller, above the base text.",
    [],
    "<ruby>木<rt>mù</rt></ruby>",
    '<div style="font-size:13px;font-family:serif"><ruby>木<rt style="font-size:9px">mù</rt></ruby></div>',
    ["Must be inside <ruby>."],
    ["ruby"])

add("rp", "Ruby Fallback Parentheses", "Text & Inline",
    "Fallback parentheses for ruby annotations in browsers without ruby support.",
    "<rp> provides opening/closing parentheses around a ruby annotation for browsers that do not support <ruby> (old ones). Modern browsers hide it.",
    [],
    "<ruby>木<rp>(</rp><rt>mù</rt><rp>)</rp></ruby>",
    '<div style="font-size:12px;font-family:serif;color:#6b7280">木(mù) — what old browsers would see</div>',
    ["Deprecated in practice — every modern browser supports ruby."],
    ["rt", "ruby"])

add("bdi", "Bidi Isolation", "Text & Inline",
    "Isolates text so its direction does not affect surrounding text.",
    "<bdi> isolates a run of text whose direction (LTR/RTL) may differ from the page, so it does not break the surrounding bidi layout — e.g. user-entered names or search terms.",
    [("dir", "ltr/rtl/auto", "Optional direction for the isolated text.")],
    "<p>Hello <bdi dir=\"auto\">مرحبا</bdi> world</p>",
    '<p style="margin:0;font-size:13px">Hello <bdi dir="auto" style="background:#fef9c3;padding:0 4px;border-radius:3px">مرحبا</bdi> world — isolated, layout-safe</p>',
    ["The modern replacement for manually sprinkling dir=\"auto\"."],
    ["bdo"])

add("bdo", "Bidi Override", "Text & Inline",
    "Forces the visual direction of text (use sparingly).",
    "<bdo> forces the displayed direction of its content with the dir attribute, overriding the natural direction. Almost always wrong — use <bdi> or <span dir=\"auto\"> instead. It is mainly kept for legacy content.",
    [("dir", "ltr/rtl", "Required. Forced direction.")],
    "<bdo dir=\"rtl\">12:30 → 03:21</bdo>",
    '<p style="margin:0;font-size:13px"><bdo dir="rtl" style="background:#fee2e2;padding:0 4px;border-radius:3px">12:30</bdo> — forced RTL rendering</p>',
    ["99% of the time you want <bdi> or dir=\"auto\", not <bdo>."],
    ["bdi"])
