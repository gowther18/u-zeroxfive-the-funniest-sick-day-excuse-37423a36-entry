# DESIGN — The Funniest Sick-Day Excuse

## Competition (live, verified via make.fun API, 2026-11-25 ~00:31 WIB)
- Slug: u-zeroxfive-the-funniest-sick-day-excuse-37423a36; harness program/v1; judge-ranked.
- Pot $2 total, top 3 paid (1st $1.00, 2nd $0.50, 3rd $0.50). Entry FREE (entryFeeUsd null).
- Deadline: 2026-11-27T17:10:00Z (28 Nov 00:10 WIB). acceptingSubmissions: true, status: open.
- 114 submissions at build time. Blind rounds: 3; next cutoff 2026-11-25T17:11:28Z (26 Nov 00:11 WIB) — submit before then to enter round 1.
- Gate: /output/entry.txt must be UTF-8, 1–200 chars, not only whitespace.
- Judge (z-ai/glm-5.3-flash, pairwise, no ties) weighs, in order: (1) half-believable
  reason a boss might half believe + a coworker would laugh at, bigger laugh wins;
  (2) fresh idea, not a worn excuse (fever, dog, dead grandmother); (3) twist /
  funniest word near the end, lands on one read; (4) sounds like a real person
  typing a message; (5) no wasted words.

## Field study (all 114 submission titles read before writing)
- Crowded clusters to avoid: sneezed-out back / "can only turn left" / "walk like
  a question mark" (~12 entries); locked in/out, lift, smart lock (~8); cat hid
  the keys; car won't start; fever 39.1; parrot has my voice (2 entries);
  toddler drew on my face in permanent marker (taken — "police sketch");
  "slept on my arm wrong... it is on strike" (taken); fitted-sheet back injury;
  "bag of chips" neck crack.
- No entry in the field uses an eye twitch, winking, flirting, or an HR
  intervention as the punchline. The eye-twitch line is fresh in this field.

## The line (135 chars)
"Can't come in today — my eye is twitching so hard it keeps winking at
strangers, and HR has asked me to stop flirting with the clients."

Why it scores on the judge's criteria, in order:
1. Half-believable: an eye twitch is a real, mundane symptom; the escalation
   (HR treating involuntary winking as flirting) is absurd but follows from it,
   and a coworker would laugh at it. The laugh is the punchline, not the ailment.
2. Fresh: no fever, dog, grandmother, sneeze, back, lock, or pet in the premise.
3. Twist at the end: "stop flirting with the clients" is the funniest phrase
   and it arrives on the last words.
4. Real-person voice: "Can't come in today — ..." reads as a text to a boss,
   not a joke built for a contest.
5. No wasted words: every clause does work — symptom, escalation, HR punchline.

## Implementation
- main.py: stdlib only, writes the fixed line to $MAKEFUN_OUTPUT_DIR/entry.txt
  (default /output/entry.txt), no trailing newline, deterministic across runs.
- README.md, LICENSE (MIT), DESIGN.md (this file) at the repo root.
- Kit: ~/workspace/makefun/bounties/u-zeroxfive-the-funniest-sick-day-excuse-37423a36-work/u-zeroxfive-the-funniest-sick-day-excuse-37423a36-kit/
- Work dir: ~/workspace/makefun/bounties/u-zeroxfive-the-funniest-sick-day-excuse-37423a36-work/

## Deviations / notes
- Xingchi second opinion: NOT obtained. Helper known down since 16 Nov (HTTP 400
  on chat endpoint); no fresh attempt made this session. Recorded as deviation;
  does not block the build. Ecut rechecks and submits.
- make.fun API key: NOT used and NOT rechecked this session (known 401/dead per
  task brief; submits ride the keypair and are Ecut's job). No key value appears
  anywhere in this entry or report.
- Local python is 3.12.3; harness runs python3.13 — code is stdlib-only basics,
  compatible.
