import re, pathlib

SRC = pathlib.Path("/tmp/fam_packet/design_packet.html")
OUT = pathlib.Path("/Users/michael/Documents/Code/fam-site/design.html")

html = SRC.read_text()

# 1. Repath all bundled assets to fam-site's assets/design/ folder
html = html.replace('assets/', 'assets/design/')

# 2. Rewrite <title> + add favicon/theme-color/description + LINK fam-site styles.css
# The packet template already includes <meta charset> + <meta name="viewport">.
# Don't duplicate those; just replace the title and append site-specific tags.
new_head_top = """<title>Fam — Design</title>
<meta name="description" content="Fam's design system — principles, tokens, components, motion, and a screen-by-screen map. The visual companion to the engineering deep dive.">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="apple-touch-icon" href="assets/favicon.png">
<meta name="theme-color" content="#E37A6D">
<link rel="stylesheet" href="styles.css">"""

html = re.sub(
    r'<title>.*?</title>',
    new_head_top,
    html,
    count=1,
    flags=re.DOTALL,
)

# 3. Overrides — all white, no dividers, floating sidebar, dissolve the shell layout
OVERRIDES = """
<style>
  /* ============================================================
     fam-site integration overrides for the design packet.
     Goal: identical top nav + page chrome as the rest of the site.
     The packet's section sidebar floats to the left of the main
     column as a quiet TOC (no border, white bg, no chrome).
     ============================================================ */
  :root {
    --page-bg: #FFFFFF;
    --bg: #FFFFFF;
    --hair: transparent;       /* kill faint section dividers from packet */
  }
  html, body { background: #FFFFFF !important; }
  body { font-size: 17px; }

  /* Dissolve the packet's flex shell — let the standard <main class="page wide"> drive layout */
  .shell { display: block; min-height: 0; }

  /* Hide the packet's internal section borders (it draws them via section { border-bottom }) */
  .content section { border-bottom: none !important; }

  /* Floating TOC sidebar — fixed in the left gutter of the centered .page.wide column.
     We want roughly equal space between viewport-left and the sidebar, and between the
     sidebar and the content. The content column is 960px wide and centered, so the gutter
     to the LEFT of it spans (0 → 50% − 480px). Center of that gutter is (25% − 240px);
     sidebar width is 220px, so left edge = 25% − 240px − 110px = 25% − 350px. */
  .shell .sidebar {
    position: fixed;
    top: 130px;                  /* below the standard fam-site nav strip */
    left: calc(25% - 350px);
    width: 220px;
    max-height: calc(100vh - 160px);
    padding: 0;
    background: transparent;
    border-right: none;
    overflow-y: auto;
    z-index: 5;
    display: flex;
    flex-direction: column;
    gap: 18px;
  }
  /* Hide the packet's brand + meta blocks inside the sidebar — duplicate of top nav */
  .shell .sidebar .brand,
  .shell .sidebar .meta { display: none; }
  .shell .sidebar nav { gap: 4px; }
  .shell .sidebar nav a {
    font-size: 15px;             /* up from 13px so the TOC is easier to scan */
    line-height: 1.4;
    color: #6E6E73;
    padding: 7px 0;
    gap: 16px;                   /* a touch more space between number and label */
    border-bottom: none;
  }
  .shell .sidebar nav a .num {
    font-size: 12px;
    width: 24px;
  }
  .shell .sidebar nav a:hover { color: #1C1C1E; }
  .shell .sidebar nav a.active { color: #E37A6D; font-weight: 600; }
  .shell .sidebar nav a.active .num { color: #E37A6D; }

  /* Content column: drop the packet's padding so the standard .page.wide rules win */
  .shell .content {
    padding: 0;
    max-width: none;
    margin: 0;
  }

  /* Phone-mock backgrounds inside the packet expect a tinted page; force white */
  .frame, .mock { background: #FFFFFF; }

  /* Hide the floating TOC on narrower screens — below ~1440px the gutter is too small for
     the sidebar to sit nicely between the viewport edge and the centered content column.
     The top nav + in-page anchor jumps still work. */
  @media (max-width: 1440px) {
    .shell .sidebar { display: none; }
  }

  /* ─────────────────────────────────────────────────────────────
     Small-mobile responsive for the design packet.
     The packet has a single 980px breakpoint built in; below that
     a number of bespoke grids (cover TOC, key/value rows, swatches,
     icons, screens, motion cards, album cells) need further care.
     We also force long URLs / code to wrap rather than scroll.
     ───────────────────────────────────────────────────────────── */
  @media (max-width: 640px) {
    .content { overflow-wrap: anywhere; word-break: break-word; }

    /* Cover */
    .cover { padding-top: 16px; padding-bottom: 16px; min-height: 0; }
    .cover .stamp { flex-wrap: wrap; gap: 16px; }
    /* Default cover-title clamp (80px min) is too big on phones — rescale */
    .cover-title { font-size: clamp(48px, 13vw, 80px); line-height: 0.96; }
    .cover-sub { font-size: 17px; }
    .cover-toc { grid-template-columns: 1fr; gap: 0; margin-top: 32px; }
    .cover .colorway span { width: 44px; height: 44px; border-radius: 10px; }

    /* Key/value rows stack — label above value */
    .kv { grid-template-columns: 1fr; gap: 2px 0; }
    .kv dt { margin-top: 10px; }

    /* Grids that were already 2-col at the 980px breakpoint → 1 col on phones */
    .swatch-grid,
    .demo-grid,
    .motion-grid { grid-template-columns: 1fr; }

    /* Mini-mock grids: keep two side-by-side but tighten */
    .screen-grid { grid-template-columns: 1fr 1fr; gap: 20px 14px; }

    /* The icon catalogue is 8-col by default, 4-col at 980px — phones get 3 */
    .icon-grid { grid-template-columns: repeat(3, 1fr); }

    /* Album sample grid: 3 cells stay readable at small widths */
    .album-grid { grid-template-columns: repeat(3, 1fr); gap: 4px; }

    /* Reduce content padding so the packet's prose breathes within the
       outer .page.wide padding (which is 24px at 640px and 16px below). */
    .content { padding: 16px 0 56px; }
  }

  /* Smallest phones (iPhone SE, very narrow) ----------------------------- */
  @media (max-width: 420px) {
    .screen-grid { grid-template-columns: 1fr; }
    .icon-grid { grid-template-columns: repeat(2, 1fr); }
    .cover .stamp { gap: 12px; font-size: 10px; }
    .cover-sub { font-size: 16px; }
    .cover .colorway span { width: 36px; height: 36px; }
  }
</style>
"""

html = html.replace("</head>", OVERRIDES + "</head>", 1)

# 4. Replace packet body wrapper with fam-site's standard <main class="page wide"> + <nav class="site-nav">,
#    and wrap the packet's .shell inside it. We capture the original <body> ... </body> contents,
#    then rebuild.
m = re.search(r'<body>\s*(.*?)\s*</body>', html, re.DOTALL)
assert m, "could not find body"
body_inner = m.group(1)  # this starts with <div class="shell">

new_body = '''<body>
  <main class="page wide">
    <nav class="site-nav" aria-label="Primary">
      <a class="nav-brand" href="index.html">Fam</a>
      <div class="nav-links">
        <a href="index.html">Product</a>
        <a href="engineering.html">Engineering</a>
        <a href="design.html" class="active">Design</a>
        <a href="privacy.html">Privacy</a>
      </div>
    </nav>

''' + body_inner + '''

    <footer class="site-footer">
      <p>© Boston Development · A private place for your family.</p>
      <div class="footer-links">
        <a href="index.html">Product</a>
        <a href="engineering.html">Engineering</a>
        <a href="privacy.html">Privacy</a>
        <a href="mailto:bostondevelopmentco@gmail.com">bostondevelopmentco@gmail.com</a>
      </div>
    </footer>
  </main>
</body>'''

html = html.replace(m.group(0), new_body, 1)

OUT.write_text(html)
print(f"Wrote {OUT} ({len(html):,} chars)")

# Sanity checks
assert 'class="site-nav"' in html and 'class="nav-brand"' in html, "missing standard fam-site nav"
assert 'class="site-nav-band"' not in html, "old custom nav band still present"
assert 'class="shell"' in html, "packet shell missing"
assert 'assets/design/' in html, "asset paths not repathed"
assert '<link rel="stylesheet" href="styles.css">' in html, "missing styles.css link"
print("Sanity checks passed.")
