# Prompt 06: Final review (independent Sonnet pass)

Run this last, on the finalized article, after you have made it yours and added your one human
detail. A reviewer that was not in the room while the issue was built catches what the writer
stopped seeing.

---

Launch a new subagent to review the finished issue. Use the Agent tool with `model: sonnet` and
a general-purpose agent, so the review is independent of this session's context.

Give the agent:

- the path to the finished article (`articles/<date>-<slug>.md`),
- `docs/style-guide.md`,
- `docs/positioning.md`.

Ask the agent to read the issue cold and report, in order:

1. **Does it hold together.** One claim, argued from the lead through the throughline, with no
   section that contradicts another. Flag any inconsistency between the benefit case, the risk
   case, and the throughline.
2. **Is it on thesis.** Does the issue serve the positioning, that AI is repricing engineering
   judgment, or has it drifted into generic AI commentary?
3. **Sourcing and fact-check.** Every number, quote, and firm action traces to a named source
   with a working link. Flag any claim that is unsourced, or that the linked source does not
   actually support.
4. **Bans and tells.** A clean pass against the hard bans and the machine vocabulary. Report any
   survivor by line. Confirm the word "principle" appears nowhere and the keeper idea sits under
   "The throughline."
5. **The pre-publish checklist.** Run the checklist at the bottom of `docs/style-guide.md` and
   report every box as ticked or flagged.
6. **Verdict.** One of: ship as is; ship after the listed fixes; or hold, with the reasons.

The agent reviews and reports only. It does not edit the file. Bring its report back so you can
decide what to change before publishing.
