# Weekly workflow

The goal is a finished issue in about thirty minutes of your time. Run it on the same day and
hour every week. Consistency is the whole game.

## Before you start

- Aim to stay two issues ahead. A backlog buffer means a busy week never breaks the streak.
- Pick your publish slot and protect it. Tuesday or Wednesday morning tends to perform well
  for a professional audience.

## Step 1: Gather (5 minutes, mostly the machine)

```bash
source .venv/bin/activate
python scripts/gather.py
```

This writes `sources/briefs/<today>-brief.md`: candidate stories from the last seven days,
grouped by content pillar, ranked, each with a link and a one-line stub. Skim it. Delete
anything that bores you. Star two or three that feel alive.

## Step 2: Drive Claude through the chain (15 minutes)

Open Claude in this repo. Say "go" and point it at the brief. Claude runs the five prompts
in `prompts/` in order. You make one decision in the middle.

1. **Research** (`prompts/01-research-brief.md`): Claude reads the candidates, fetches the
   strongest few, and returns a sourced digest with the key facts and primary links.
2. **Angle** (`prompts/02-angle-selection.md`): Claude proposes three angles and recommends
   one. **You choose.** This is the one decision that decides whether the issue is sharp.
3. **Draft** (`prompts/03-draft.md`): Claude writes the full piece in your voice against
   `templates/article-template.md`.
4. **Edit and fact check** (`prompts/04-edit-and-factcheck.md`): Claude runs the style bans
   and verifies every claim against a source. Unsourced claims get cut or flagged.
5. **Headline and social** (`prompts/05-headline-and-social.md`): title, subtitle, email
   subject line, and two LinkedIn posts.

The finished draft is saved to `articles/<date>-<slug>.md`.

## Step 3: Make it yours (10 minutes)

Claude drafts. You are the author. Read the whole thing aloud once. Where it sounds like a
machine, change it. Add one specific thing only you would know: a number from a project, a
phrase a client used, a mistake you watched a firm make. That single human detail is what
separates you from every other AI newsletter.

Then run the pre-publish checklist at the bottom of `docs/style-guide.md`. It takes two
minutes and it is not optional.

## Step 4: Publish and distribute (5 minutes)

1. Paste the article into Substack. Use the title, subtitle, and email subject from step 5.
2. Publish.
3. Post the two LinkedIn variants. One goes out now, one two days later. Your buyers live on
   LinkedIn, so this step matters as much as the article itself. See
   [docs/distribution.md](docs/distribution.md).

## Step 5: Log the call

If the issue made a prediction, add it to `templates/predictions-ledger.md` with today's
date. Every quarter you grade the open calls in public. That track record is your moat.

## Monthly and quarterly

- **Monthly**: open `docs/metrics-and-feedback.md`, log the numbers, and note which pillars
  pulled. Reweight the calendar toward what works.
- **Quarterly**: grade the predictions ledger in a public issue. Prune dead feeds from
  `sources/sources.yaml` (gather.py logs which ones returned nothing).
