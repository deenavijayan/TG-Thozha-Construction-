# TG THOZHA CONSTRUCTION — website (static HTML/CSS/JS)

## Run locally
Open `index.html` in a browser, or for best results (video seeking) run a local server:
    python3 -m http.server 8000     # then open http://localhost:8000
## Put it on GitHub Pages
Upload this whole folder to a GitHub repo -> Settings > Pages -> Deploy from branch (main, / root).
After deploying, change the `og:image` meta tag in index.html to the full https URL of images/hero/hero-poster.jpg.

## Where to change things
- **All text, project list, services, testimonials, media paths:** `content.js` (only file you need for content).
- **Media:** overwrite the files below with your real ones — SAME NAME. Keep the same aspect ratio; larger is fine.

| File | Size (px) | Notes |
|---|---|---|
| images/brand/logo.png | ~800x340 | Transparent PNG of the supplied logo. Replace with your original transparent file when you have it. |
| images/brand/favicon.png | 128x128 | Browser tab icon |
| images/hero/hero.mp4 | 1920x1080 | Silent looping hero video, under 6 MB |
| images/hero/hero-poster.jpg | 1920x1080 | Shown before video loads |
| images/hero/blueprint.jpg | 1920x1080 | Real blueprint/plan photo or scan (shown behind hero on mobile, and in final CTA) |
| images/about/about.jpg | 1600x1200 | Featured residential construction |
| images/services/service-01..08.jpg | 1400x980 | One per service, order as in content.js |
| images/projects/project-01..10.jpg | 1600x1000 | Add more: copy a line in `projects` in content.js |
| images/primary/plan-blueprint.jpg / plan-building.jpg | 1400x980 | Plans & Approvals section (blueprint wipes into building) |
| images/construction/stage-1..5-*.jpg | 1600x900 | Foundation, Structure, Walls, Finishing, Completion — same camera angle |
| images/construction/process.mp4 | 1280x720 | Scroll-scrubbed process video (see below) |
| images/construction/process-poster.jpg | 1280x720 | Poster frame |
| images/cta/cta.jpg | 2400x1350 | Final call-to-action background |
| images/about/praveen.jpg | 1000x1300 | Founder portrait — used in the animated Legacy section |
| images/about/gokulraj.jpg | 1000x1300 | Engineer portrait — used in the animated Legacy section |
| images/about/chinnasamy.jpg | 1000x1300 | JK Construction founder portrait — used in the animated Partnership section |
| images/brand/jk-logo.png | ~900x420 | JK Construction logo, transparent PNG |
| images/testimonials/ | any | Put customer photos here; reference them in content.js |

## Process video (scroll-scrubbed)
Put 7 frames in `stages/` (0-blueprint, 1-plot, 2-foundation, 3-structure, 4-walls, 5-finishing, 6-complete; 1920x1080, same angle),
then: `pip install pillow` (ffmpeg must be installed) and `python3 build_video.py 1280 26` -> writes images/construction/process.mp4.
Or supply your own mp4 encoded with all keyframes: `ffmpeg -i in.mp4 -vf scale=1280:-2 -g 1 -crf 26 -an process.mp4`.

## Notes
- Nothing invented: project names/locations show "to be added"; testimonials are marked PLACEHOLDER.
- Contact form opens WhatsApp with the message pre-filled (no server needed).
- Images provided now are generated placeholders, not real photos.

## Removed in this revision
- "Our Process" section (kept "Construction Journey" instead — they told the same story).
- "Why TG Thozha Construction" section.
- The boxed founder/engineer text block in About (replaced by the animated Legacy section).

## Mobile data saving
On screens ≤780px (or when the browser reports Data Saver / a 2G connection), the hero video is not downloaded — a static image is shown instead. Edit the `780` in the `lightMode` line near the top of the `<script>` in index.html to change this threshold.

## Locations
Now 5 project locations: Dharmapuri, Hosur, Yercaud, Salem, Krishnagiri. Edit the `locations` array in content.js to change these.

## Google Reviews
Edit `googleReviews` in content.js: set `rating` (e.g. 4.8) and `count` once you have real numbers from your Google Business Profile, set `link` to your review page, and replace each review's `q`/`who`/`when` with real reviews. Nothing shown now is a real review — it's all marked PLACEHOLDER.

## Legacy & Partnership section size
Both are shorter/smaller now (Legacy 200vh, Partnership 180vh in index.html — search `id="legacy"` / `id="partnership"`). Increase the vh value to make the scroll animation last longer again.
