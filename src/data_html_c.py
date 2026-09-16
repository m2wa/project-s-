# -*- coding: utf-8 -*-
# HTML elements — Part C: the remaining core elements (a, del, ins)
from data_html_b import E, add  # noqa: F401

add("a", "Anchor (Hyperlink)", "Links & Navigation",
    "Creates a hyperlink to a page, a section, a file, an email, or a phone number.",
    "<a> is the element that makes the web a web: it turns text into a navigation. The href attribute is the destination — URLs, in-page fragments (#id), mailto: addresses, tel: numbers, data: URIs. The link's visible text is what gets read out, so make it meaningful.",
    [("href", "URL", "Destination: https://…, #section, mailto:hi@x.com, tel:+20…"),
     ("target", "window name", "_blank opens a new tab (add rel=\"noopener\"!), _self, or a named window."),
     ("rel", "tokens", "Relationship: noopener, noreferrer, nofollow, external, author, license…"),
     ("download", "filename?", "Force download; the value is the suggested filename."),
     ("type", "MIME type", "Hints the resource type of href."),
     ("ping", "URLs", "Space-separated URLs notified in the background when the link is followed."),
     ("hreflang", "BCP-47", "Language of the linked document."),
     ("referrerpolicy", "policy", "Which referrer to send."),
     ("media", "media query", "For links to alternate resources.")],
    '<a href="https://w3schools.com/html/" target="_blank" rel="noopener">W3Schools HTML</a>\n<a href="#contact">Jump to contact</a>\n<a href="mailto:hi@example.com">Email us</a>',
    '<div style="font-size:13px;display:grid;gap:4px"><a href="#" style="color:#2563eb">W3Schools HTML <span style="font-size:10px">↗ (target=_blank)</span></a><a href="#" style="color:#2563eb">Jump to #contact</a><a href="#" style="color:#2563eb">Email us (mailto:)</a></div>',
    ["Always add rel=\"noopener\" with target=\"_blank\" (security).", "Fragment links (#id) need scroll-margin-top if you have a sticky header.", "Meaningful link text beats “click here” (a11y + SEO)."],
    ["link", "map", "area"])

add("del", "Deleted Text", "Text & Inline",
    "Marks text removed from the document (change tracking).",
    "<del> records that content was deleted, with when/cite attributes for the timestamp and source. It renders strikethrough. Use it in diffs, price changes, and edit histories — unlike <s>, it carries change-tracking semantics.",
    [("cite", "URL", "Source of the deletion (e.g. an edit log)."),
     ("datetime", "ISO date", "When the deletion happened.")],
    '<del datetime="2026-09-10">Old price: $99</del> → $79',
    '<div style="font-size:13px"><del style="color:#9ca3af">Old price: $99</del> → <b>$79</b> <small>(deleted 2026-09-10)</small></div>',
    ["<del> = change tracking (what/when); <s> = “no longer accurate” (no time)."],
    ["ins", "s"])

add("ins", "Inserted Text", "Text & Inline",
    "Marks text added to the document (change tracking).",
    "<ins> records newly added content, with cite and datetime for source and time. It renders underlined. The partner of <del> for edit histories and tracked changes.",
    [("cite", "URL", "Source of the insertion."),
     ("datetime", "ISO date", "When the insertion happened.")],
    '<p>The team is <ins datetime="2026-09-16">now 5 people</ins>.</p>',
    '<div style="font-size:13px">The team is <ins style="text-decoration-color:#16a34a">now 5 people</ins> <small style="color:#6b7280">(added 2026-09-16)</small></div>',
    ["Use del/ins pairs for real change tracking; plain <s>/<u> for style."],
    ["del", "u"])
