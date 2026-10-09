# Source: "The 6 Phrases That Make Claude Build 10x Faster" (Instagram auto-DM)

Where from: an Instagram auto-DM (the reply to commenting "PHRASES" on a reel), attributed to
Nate Herk by Charlie. Charlie pasted the text on 2026-10-09; date sent unknown, and the author
isn't named in the text itself. **This text is verbatim**, as pasted, so it can be quoted.

---

The 6 Phrases That Make Claude Build 10x Faster
You commented "PHRASES", so here are all six in full.
The reel had the short versions. These are the actual prompts, plus the reason each one works and the way each one goes wrong.

## 1. Launch sub-agents
Instead of Claude grinding through work one item at a time, it splits and runs in parallel.

> Launch sub-agents for this.
>
> Split the work so each agent owns one independent piece and none of them need each other's output. Before you start, tell me: how many agents, what each one owns, and what you'll do if two of them come back with contradictory findings.
>
> When they're done, reconcile the results yourself and give me one answer, not three reports.

When it backfires: work that isn't actually parallel. If step 2 needs step 1's answer, sub-agents make it slower and worse. Use this for search, review across many files, and research. Not for sequential building.

## 2. Write me an implementation spec
> Write me an implementation spec before you touch anything.
>
> Cover: what you're going to build, the files you'll create or change, the order you'll do it in, what could go wrong at each step, and what you're explicitly NOT doing.
>
> End with the three decisions in this plan I'm most likely to disagree with, and why you chose them.
>
> Do not write code until I say go.

Why the last paragraph matters: it surfaces the assumption you'd otherwise find out about forty minutes in.

## 3. Interview me
> Interview me before you start.
>
> Ask one question at a time and wait for my answer. Keep going until you could hand this to someone who has never spoken to me and they'd build the right thing.
>
> Ask about what I actually want, not what I said. Ask about the edge cases I haven't mentioned. Ask what "done" looks like.
>
> When you stop, summarise what you learned and flag anything I was vague about.

The trap: it asks ten questions in one message and you answer three. One question at a time is not optional.

## 4. Verify before you build
> Before you build, tell me how you're going to prove this works.
>
> Pick the strongest option you actually have: a test you write and run, a command whose output I can read, real data you process, or a second pass reading your own diff against the requirement.
>
> Then tell me what that check would NOT catch.
>
> After you build, run it and report:
> VERIFIED: [what you ran, what it returned]
> NOT VERIFIED: [what you couldn't check and why]

Why the format is mandatory: without a required shape, "it should work" slides right in. NOT VERIFIED forces honesty.

## 5. Based on this conversation, build me a skill
> Based on this conversation, build me a skill.
>
> Capture everything we just worked out so I never explain it again. Include: when this skill should fire, the exact steps in order, the prompts that actually worked, the mistakes we hit and how we fixed them, and what to do when it goes wrong.
>
> Write it for someone who has my context but not my memory. Keep it under 300 lines.

The rule: run this the second time you solve something, not the first. The first time you don't yet know which parts mattered.

## 6. Automate this
The most powerful one, and the one to be slowest with.

> Automate this.
>
> Before you set anything up, show me the plan: what will run, when it will run, exactly which files or services it touches, and what happens if a step fails.
>
> I want to review that plan before anything is scheduled.

How to use it well. Keep the scope tight on the first version. Let it read broadly and write to exactly one place. Have it show you anything it would send or publish rather than acting on its own. And keep a log of every run, because the first time an automation surprises you, the log is the only way to work out why.
An automation that runs while you're asleep with one wrong assumption is a very different problem from a prompt with one wrong assumption. Get phrases 2 and 4 reliable before you reach for this one.
Rule of thumb: phrases 1 to 5 make Claude better at one task. Phrase 6 makes it act without you watching. Earn your way to it.

## The order they actually go in
On a real task you use four of them in sequence:
1. Interview me so it understands the job
2. Write me an implementation spec so you can catch bad calls early
3. Verify before you build so "done" means something
4. Build me a skill so next time is free

Launch sub-agents slots into step 1 or 2 when there's research to do. Automate this comes later, once the skill from step 4 has been run enough times that you trust it.

## What breaks and how to fix it
- Sub-agents contradict each other and it picks one at random. The reconciliation line wasn't there. Make it state the conflict before resolving it.
- The spec is vague. Ask for file paths and function names. If it can't name files, it hasn't thought about it yet.
- The interview is generic. Add: Only ask things you don't already know from what I've said. Do not ask me to repeat myself.
- The verifier is "I reviewed the code." That's not a verifier. Reject it and make it run something.
- The skill is a summary, not instructions. Add: Write it as instructions to a future agent, in the imperative. Not a description of what we did.
- The automation did something you didn't expect. Its scope was too wide. Narrow it to one destination and rebuild from there.

## Do this in the next 10 minutes
- [ ] Take the task you're about to start and open with Interview me instead
- [ ] Add the VERIFIED / NOT VERIFIED block to your CLAUDE.md as a permanent rule
- [ ] Pick something you've now explained to Claude twice and turn it into a skill

Six phrases. The one that compounds is number five.
