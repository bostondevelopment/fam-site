# fam-site

Public static site for the Fam app: landing page, engineering deep dive, design packet, and privacy policy. Hosted on GitHub Pages.

Plain HTML/CSS, no Jekyll, no build step. Edit the files, commit, push, and GitHub Pages serves the change in under a minute.

## Files

| Path | Purpose |
|---|---|
| `index.html` | Landing page (`https://<gh-user>.github.io/fam-site/`) |
| `engineering.html` | Engineering deep dive — stack, architecture, automation pipeline, agent workflow. |
| `design.html` | Design packet — principles, tokens, components, motion, screen map. Self-contained (Inter fonts + screens bundled in `assets/design/`). |
| `privacy.html` | Privacy policy (`https://<gh-user>.github.io/fam-site/privacy.html`) — this is the URL to paste into App Store Connect → App Information → Privacy Policy URL |
| `styles.css` | Shared styles (top nav, footer, landing/engineering/privacy pages). `design.html` has its own scoped styles for the packet shell. |
| `assets/design/` | PNG screens + Inter woff2 fonts bundled for `design.html`. |
| `.nojekyll` | Tells GitHub Pages to serve files as-is (no Jekyll processing) |

## Publishing — first time

1. Create a new repository on GitHub named `fam-site` (public).
2. From this directory:
   ```bash
   git init
   git add .
   git commit -m "Initial site"
   git branch -M main
   git remote add origin https://github.com/<your-gh-user>/fam-site.git
   git push -u origin main
   ```
3. On GitHub, go to **Settings → Pages**:
   - **Source:** Deploy from a branch
   - **Branch:** `main` / `/ (root)`
   - Save.
4. Wait ~30 seconds. The published URL appears at the top of the Pages settings panel, e.g.
   `https://<your-gh-user>.github.io/fam-site/`
5. Paste `https://<your-gh-user>.github.io/fam-site/privacy.html` into App Store Connect.

## Publishing — updates

```bash
git add .
git commit -m "Update privacy policy"
git push
```

Pages picks up the change automatically.

## Adding a custom domain later

When you're ready to host this at `https://fam.app/`:

1. Add a `CNAME` file in this repo containing one line: `fam.app`
2. In your DNS provider, create a CNAME record for `fam.app` (or `www.fam.app`) pointing to `<your-gh-user>.github.io`.
3. In GitHub repo Settings → Pages, set the custom domain to `fam.app` and enable "Enforce HTTPS".
4. Update the privacy policy URL in App Store Connect to `https://fam.app/privacy.html`.

## Editing the privacy policy

Open `privacy.html` and edit the sections. Bump the "Last updated" date at the top of the page. Material changes should also bump the "Effective date" — and you should notify users inside the app or by email.

Keep the language plain. The current version intentionally avoids legalese.
