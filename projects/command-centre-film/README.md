# Command Centre film

A 56-second launch-style video (1920×1080, 30fps, no sound) for the Business
Command Centre idea: a live dashboard plus a WhatsApp agent. It's made to help
bring small business owners onto Claude. Made 17 October 2026 at Charlie's request.

- Video: `command-centre-film.mp4`
- Source: `index.html` (every scene is drawn by `render(t)`, so any frame can be reproduced)
- Renderer: `render.js` (Playwright screenshots each frame and pipes it to ffmpeg)
- Fonts: Source Serif 4 (SIL Open Font License) in `fonts/`; Inter is a system font
- Related decks: the original [Business Command Centre](https://claude.ai/artifact/4qjwwGNWD6FLfW15qhiqg3)
  and the keynote restyle [Command Centre Launch](https://claude.ai/artifact/CZBGf96hM1GLMjdepPtNij)

## Scenes
1. 0–6s: "Your numbers live in five places." Scattered app cards and an hour timer.
2. 6–10s: "Connect once." The cards fly into one data hub.
3. 10–24s: the dashboard builds itself: counting KPIs, a sales line that draws, lead bars, a "Needs you today" list.
4. 24–38s: a WhatsApp chat ("Who still owes us money?"). The answer lights up the same Unpaid tile, then the agent drafts a reminder for approval.
5. 38–44s: the 8am morning summary.
6. 44–50s: "You stay in control of your data." Four checks and a shield.
7. 50–56s: end card with placeholders `[Your company name] · [Booking link]`.

## Re-render
```
cd projects/command-centre-film
NODE_PATH=$(npm root -g) node render.js preview 17.5 31   # stills into frames/
NODE_PATH=$(npm root -g) node render.js video             # writes out.mp4
```

## Honest limits
- Every figure is **sample data**, and the video says so on screen. Before showing it to a
  prospect, swap in their own numbers or keep the label.
- There's no music or voiceover yet.
- Design rules come from Impeccable and Taste (taste-skill), read from their published
  instructions. Those skills and Higgsfield were not installed: this session's
  safety check blocks installing third-party code without a permission rule.
- "Built with Claude" is a plain statement of how it is made. There's no Anthropic logo or branding.
