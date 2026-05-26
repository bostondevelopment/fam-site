# Screenshot slots

All marketing-page slots are currently wired with high-resolution
captures (Simpsons-themed seed data) sourced from `../screens2/`. To
replace any of them, drop a new PNG into this folder using the same
filename and it'll swap in on the next page load.

## Marketing page (`/index.html`) — currently wired

Phone screenshots — target **9:19.5** aspect (iPhone 15/16 portrait).

| File | Slot | Currently shows |
|---|---|---|
| `01_tree.png` | Hero strip · left | Family Tree with Marge as focal node |
| `02_pulse.png` | Hero strip · center | Pulse feed: "Hi Marge", upcoming birthdays, RSVP |
| `03_photos.png` | Hero strip · right | Album grid organized by decade |
| `04_onboarding.png` | "How to use it" feature row | Tag-your-people face tagging step |
| `arc_01.png` | Arc strip · frame 1 | Brand new family: Marge alone, "add parent" prompts |
| `arc_02.png` | Arc strip · frame 2 | Mid-build: 8 people, 24 photos tagged, 5 birthdays |
| `arc_03.png` | Arc strip · frame 3 | Family List timeline — accumulated births / marriages |
| `05_pulse_card.png` | "Habits that make it feel alive" feature row | Memory card detail: "Maggie's first words" |
| `06_living_summary.png` | "Family Pulse" feature row | Calendar with upcoming birthdays |
| `07_hero.png` | Closing CTA | Pulse feed (bookend reuse of 02) |

## Engineering page (`/engineering.html`) — currently wired

The "Analytics & observability" card has two wide screenshot slots, both
filled with real Django admin captures from May 26.

| File | Slot | Currently shows |
|---|---|---|
| `eng_analytics_01.png` | Analytics card · top | Database snapshots panel — 23 families, 7.78 avg persons/family, 94.3% top-uploader share |
| `eng_analytics_02.png` | Analytics card · middle | Event charts panel — DAU line, Contribution by segment, Retention bars, Sessions by surface |

Three additional dashboard PNGs live in `../dashboards/` as raw
material (period numbers, top events / platform donut, top-uploader
table with UUIDs). They're intentionally not wired — adding them
would be padding rather than narrative.

## Notes

- Don't worry about phone bezels — the CSS adds an App-Store-style white
  panel with rounded corners and a soft shadow around each image.
- All images use descriptive `alt` text — keep that in mind if you swap.
- The captures were ~25–45 KB each and ship as-is. If you swap with larger
  files, consider re-exporting at ~1290×2796 to keep the page light.
