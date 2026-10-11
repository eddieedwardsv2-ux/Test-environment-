# Nate Herk — AI video-editing workflow (segmented notes)

Source: [Opus 5.5 Just Changed Video Editing Forever (free skills)](opus-5-5-just-changed-video-editing-forever-free-skills--7jHXoPGnA4c-transcript.md)  
YouTube ID: `7jHXoPGnA4c`  
Published: 2026-09-25  
Full source status: the complete timestamped transcript and raw source are already saved in this folder. This file is derived routing/segmentation, not a replacement for the transcript.

## Why this source matters

This video contains a durable production method, not merely a model demo. Nate's examples use Opus 5.5 and HyperFrames, but the lasting system idea is a five-stage media loop:

`transcribe → cut → plan beats → reuse/refine a skill → verify the rendered output`

The workflow belongs in both Nate's architecture brain and the Quartermaster because it separates the stable production method from whichever editing/generation tool happens to be current.

## Semantic segments

| Time | Segment | Durable information |
|---|---|---|
| 0:01–1:31 | What the agent can assemble | Motion design, sound design, B-roll, screenshots and generated assets can be coordinated from natural-language direction. The result still needs verification. |
| 1:32–4:34 | Transcript-driven timing and explicit beats | Transcribe first so visual elements can align with speech. Give concrete timing/placement expectations and define what “good” looks like. |
| 4:35–6:37 | Reference → analysis → reusable skill | A reference video can be analysed for why it works, then distilled into a reusable motion/reel skill rather than re-prompted from scratch each time. |
| 6:38–10:50 | Brand and story assembly | Use real brand assets, typography, colours, design language and source footage. The agent should tell a story from the material rather than merely decorate clips. |
| 10:51–13:51 | Same footage, different production briefs | The same raw clip can become whiteboard, course-style or short-form output when the beat plan and visual language change. This demonstrates that style is a brief/skill layer, not the raw footage itself. |
| 13:52–15:58 | Product/brand look and feel | Brand identity can be expressed through chosen assets, pacing, music, motion and emotional direction. “Professional” is not one generic style; it is alignment to a defined visual language. |
| 15:59–19:21 | Five-stage method | 1) transcribe; 2) remove mistakes/dead space; 3) plan beats; 4) build/refine reusable skills; 5) let the agent inspect renders/screenshots and iterate before handoff. |

## Stable principles vs dated implementation

### Stable
- Timing starts from transcript or another explicit time-aligned source.
- Remove obvious mistakes/dead space before expensive creative work.
- Plan visual beats against the story and state what good looks like.
- Repeated preferences belong in a reusable skill, not repeated prompts.
- Improve the skill from specific feedback on real outputs.
- Brand assets, typography, colour, pacing and emotional intent are input constraints.
- The worker should inspect the rendered artifact, not only its own code/prompt.
- A first render is a draft; iteration continues until an explicit quality gate is met.
- The method should be tested on our own real work before we promote a tool or skill.

### Dated / tool-specific
- Opus 5.5 performance claims.
- HyperFrames as the implementation used in the examples.
- ElevenLabs vs Whisper speed/cost comparison.
- Kling/Kie.ai asset-generation examples.
- ScrollCraft promotion.
- Student-kit/community promotion.

These may still be useful tools, but Quartermaster must evaluate them as current products rather than treating this video as permanent proof that they are best.

## Relation to our system

### Nate brain
This strengthens the existing themes around skills, “prove it”, smaller repeatable procedures, and verification. It adds a media-specific execution contract: verification must inspect the rendered artifact, not just the instructions that produced it.

### Quartermaster
Quartermaster should choose tools **inside** this production method rather than choosing a tool first and letting the workflow bend around it. A candidate must improve a named stage: transcribe, cut, beat planning, reusable skill execution, asset generation/assembly, or verification.

### Guardian / verification
For media, “tests passed” cannot mean only that a render command succeeded. The verification evidence should include the produced video plus visual/audio inspection at representative frames or scenes. Problems found should cause another render before handoff.

### Journey video / Shorts
The first strong proof case should be Charlie's AI-OS journey Short. It already has a story thesis and a chosen visual direction (“Mix”: Terminal typing + Kinetic boldness/colour + early Glass scenes). The Nate loop gives us the production discipline to turn that draft into a professional artifact instead of another concept page.

### Creative Claw and HyperFrames
- HyperFrames has already produced a draft-quality 10-second title card and its checker caught a layout fault, but Charlie could not review the video in-app; its verdict remains **later** until a real Short is reviewable.
- Creative Claw is routed for YouTube media but is not yet connected/tested.
- Neither should be promoted merely because this Nate video looks strong. The journey Short is the real comparison/proof task.

## Journey Short proof plan

1. **Transcribe / timing source** — use Charlie's final voice-over or script as the timed source.
2. **Cut** — remove mistakes, dead air and redundant phrasing before motion work.
3. **Plan beats** — map each story beat to exact moments and define the “Mix” brand constraints.
4. **Skill / assembly** — reuse the smallest suitable motion/Short capability; update it only from concrete feedback.
5. **Verification loop** — render → inspect video/audio/framing/branding → record defects → rerender until the quality gate passes.

### Quality gate
The Short is not “verified” until:
- the story is understandable to a newcomer without repo knowledge;
- the router/Elders/Chief relationship is not confused;
- typography, colour and motion feel consistent rather than template-random;
- important visuals enter on the intended spoken beats;
- no text is unreadable on a phone;
- there are no obvious dead-air, cut, audio or framing faults;
- the final render has been watched end to end after the last change;
- Charlie can preview it before any publishing action.

## Status

**VERIFIED:** full timestamped transcript exists in the repo; the five-stage method and brand/verification sections are present in the source.

**NOT VERIFIED:** the method has not yet been proven end to end on Charlie's journey Short. Do not promote a specific editor/toolchain as the default until that real render is produced, inspected and compared.
