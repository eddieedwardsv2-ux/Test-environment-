# Nate's "Upgrade 2" landing-page prompt (with verification loop)

- **Source:** Nate Herk, "I asked Claude Code to make me as much money as possible",
  https://www.youtube.com/watch?v=iTY8Q449YNQ (transcript in this folder).
  Nate shares his prompts and skills through the Google Drive folder linked in the video.
- **On screen as:** `upgrade2-landing-page-prompt.txt`
- **Captured:** 2026-10-09, typed up from Charlie's five phone photos of the screen.
- `[cut off in photo]` = the line ran off screen or sat behind the webcam bubble.
  The missing words are not guessed. Get the full text from Nate's Drive folder if needed.
- **Why it matters for us:** it's five experts in one prompt (product strategist,
  conversion copywriter, designer, engineer, QA) plus a written definition of done.
  It's the worked example in `brainstorms/2026-10-09-elder-councils-plan.md`.

---

## The prompt as shown

```text
Build me a complete, modern landing page for a SaaS product, then verify it visually with Playwright u… [cut off in photo]

## The product
Name: Cadence
What it does: Cadence turns one piece of long-form content — a YouTube video, podcast, or transcript — … [cut off in photo]
Who it's for: e-commerce business owners who want to build a personal brand on LinkedIn to drive trust … [cut off in photo]
Tone: clean, confident, premium. This should feel like a real, fundable SaaS company, not a gimmick.

## Page goal
This is a WAITLIST landing page. I'm going to DM 20 to 30 e-commerce founders and send them here to jo… [cut off in photo]

## Sections to build (single page, top to bottom)
1. Nav bar — wordmark "Cadence", links (Features, How it works, Pricing), and a solid "Join the waitli… [cut off in photo]

2. Hero
   - Headline: "Turn one video into a week of LinkedIn posts. In your voice."
   - Subheadline: "Cadence repurposes your content into 7 days of scroll-stopping LinkedIn posts that … [cut off in photo]
   - Primary CTA button: "Join the waitlist"
   - A clean product mockup / visual placeholder next to or under the copy.

3. Social proof strip — a short trust line plus a row of placeholder "trusted by" lo… [cut off in photo]

4. Features — 6 feature cards, each a short title + one-sentence description:
   - Voice Match — trains on your past posts so every draft sounds like you, not a … [cut off in photo]
   - One video, a week of posts — drop in a transcript, get 5 to 7 polished posts in minutes.
   - Built-in scheduler — queue a full week in one sitting and let it auto-post.
   - Proven hooks — every post is structured with hooks built to stop the scroll.
   - Idea multiplier — turn a single video into multiple angles so you never repeat yourself.
   - Performance view — see which posts drove profile views and clicks.

5. How it works — 3 simple steps:
   1) Paste your transcript.
   2) Cadence writes a week of posts in your voice.
   3) Approve and schedule.

6. Pricing — a clean 3-tier section, middle tier highlighted as "Most popular":
   - Starter — $19/mo — 1 brand, 4 videos per month, ~30 posts per month, scheduler included.
   - Pro — $39/mo — 1 brand, unlimited videos, unlimited posts, analytics, priority generation. (Most p… [cut off in photo]
   - Scale — $79/mo — up to 3 brands, team access, everything in Pro.
   - Add a line under the tiers: "Waitlist members lock in founding-member pricing for life."

7. Waitlist form — the key conversion section. Fields:
   - Full name (text)
   - Email (email)
   - Company name (text)
   - Annual revenue (dropdown: Under $100k / $100k-$500k / $500k-$1M / $1M-$5M / $5M+)
   - LinkedIn followers (dropdown: Under 500 / 500-2k / 2k-10k / 10k-50k / 50k+)
   - Submit button: "Join the waitlist"
   - On submit: validate every field, then show a clean success confirmation state ("You're on the list… [cut off in photo]

8. Footer — wordmark, minimal links, copyright line.

## Design direction
- Modern, premium SaaS look. Lots of white space, clear visual hierarchy, generous padding.
- Color: deep indigo/navy as the primary (around #1E1B4B / #312E81) with a vibrant violet/electric … [cut off in photo]
- Typography: clean geometric sans-serif (Inter or similar). Large, strong headlines. Comfortable, rea… [cut off in photo]
- Buttons: solid accent fill with a clear hover state.
- Must be fully responsive and look right on both desktop and mobile.

## Tech
- Keep it simple and runnable locally. Plain HTML/CSS/JS (Tailwind via CDN is fine) or a lightweight V… [cut off in photo]
- Serve it on localhost and tell me the exact URL.

## Verification — DO NOT SKIP. This is the part that matters.
After you build it, do not trust that it looks right. Verify it yourself with Playwright before report… [cut off in photo]
1. Start the local server. Use the Playwright CLI / a Playwright script to open the localhost URL in a … [cut off in photo]
2. Screenshot every section individually: nav, hero, social proof, features, how it works, pricing, wa… [cut off in photo]
3. Do all of the above at BOTH a desktop viewport (1440px wide) and a mobile viewport (390px wide).
4. Actually look at every screenshot and check for visual errors:
   - Text that overflows or runs out of bounds / off screen
   - Text that's unreadable (too small, low contrast, clipped, or overlapping)
   - Overlapping or misaligned elements, broken spacing, cut-off content
   - Images or sections that don't render
   - Anything that breaks at mobile width
5. Stress-test the waitlist form: use Playwright to fill in every field and submit it, confirm validat… [cut off in photo]
6. If you find ANY issue, fix it, then re-screenshot and re-check that section. Repeat the loop.
7. Only stop once every section has been screenshotted at both viewports, there are zero vi… [cut off in photo]

## Definition of done
A localhost landing page I can pull up and look at that:
- Looks like a clean, modern, professional SaaS product
- Has every section above, with the waitlist form actually working
- Has zero visible aesthetic errors — no out-of-bounds text, nothing unreadable, n… [cut off in photo]

When you're finished, show me the screenshots you took and give me the localhost URL… [cut off in photo]
```

20 lines are cut off.

---

## How we'd reuse it (our template, not Nate's)

The shape works for any build. Fill in the brackets:

```text
Build [what], then prove it works before you report back.

## The thing
Name / what it does / who it's for / tone: [...]

## Goal
[the one outcome it must drive, e.g. waitlist sign-ups from 20-30 DMs]

## Parts to build (in order)
1. [part] — [what it must contain]
...

## Design / style direction
[look, colours, type, must work on phone and desktop]

## Tech
[simplest stack that runs; where it runs; tell me the exact link]

## Verification — do not skip
1. Run it for real ([tool: Playwright for pages, render-and-watch for video, run-on-real-data for pipelines]).
2. Check each part on its own, in every setting that matters ([e.g. 1440px and 390px]).
3. Look at the evidence and list every fault: [checklist for this kind of build].
4. Stress-test the riskiest bit: [form, edge cases, odd inputs].
5. Fix → re-check that part → repeat (at most [2] rounds, then report NOT READY).

## Definition of done
[3-5 checkable lines]. Then show me the evidence and say what these checks would NOT catch.
```

Note from the video: passing these checks proves the thing **works**, not that
it's **good**. The page Nate built passed and still looked generic. So add a
taste check, and let Charlie judge taste last.
