---
name: write-article
description: Run the weekly newsletter chain: read this week's sources brief, research and source a digest, pick an angle with Lorela, draft the issue in her voice, edit and fact-check it, then produce the headline and social packaging. Use when Lorela says "go", points at a brief in sources/briefs/, or asks to write this week's issue.
argument-hint: <path to sources/briefs/<date>-brief.md, or blank to use the newest brief>
---

# Produce one week's issue

Read `CLAUDE.md`, `docs/style-guide.md` (the voice, the hard bans, the pre-publish checklist),
`docs/positioning.md`, and `docs/content-pillars.md` first. Then run the prompts in `prompts/`
in order, exactly as written. They are the specification; this skill only sequences them.

- Input: the argument, a specific brief path, or the newest file in `sources/briefs/`. If none
  exists, tell her to run `python scripts/gather.py` first; never invent sources.
- Run `01-research-brief.md`: read every candidate in the brief, discard anything off-thesis,
  fetch and read the primary source for the four to six strongest, and return a sourced digest.
  Every fact carries a named source and a working link. Do not pick the angle or draft yet.
- Run `02-angle-selection.md`: propose three angles from the digest, each with its claim, its
  pillar, why it's current this week, a benefit case and a risk case, who shares it, and the
  risk in the angle. Recommend one. STOP and wait for her to choose, combine, or redirect.
- Run `03-draft.md` on the chosen angle: the full issue in voice, 800 to 1200 words, leading
  with the claim, one throughline (never labeled a "principle"), a dated falsifiable
  prediction, and closing "what I am watching next." Leave the `[YOUR DETAIL HERE]` placeholder
  for her; never invent that detail. Save to `articles/<date>-<slug>.md` with a frontmatter
  block (date, pillar, working title).
- Run `04-edit-and-factcheck.md`: a style pass against every hard ban (antithesis, dashes,
  machine vocabulary, commands to the reader), then a fact-check pass verifying every claim
  against its source. Report what changed, and the filled-in pre-publish checklist. Save over
  the draft, keeping `[YOUR DETAIL HERE]` in place.
- Run `05-headline-and-social.md`: title (3 options), subtitle (2), email subject line (3,
  recommend one), and the two LinkedIn posts (publish day, and the follow-up two days later).
- Tell her what remains: fill in `[YOUR DETAIL HERE]`, read the piece aloud once and rewrite
  anywhere it sounds like a machine, then `06-final-review.md` (an independent Sonnet subagent
  via the Agent tool, `model: sonnet`) on the version she has already made hers, before she
  publishes.

The bar throughout: lead with the claim, reason from cause and effect rather than fashion,
calibrate confidence explicitly, show a benefit case and a risk case honestly, land exactly one
throughline, source every fact to a primary link, and never let it read like something any
other AI newsletter could have written this week.
