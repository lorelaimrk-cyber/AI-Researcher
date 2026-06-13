# AI-Researcher

A weekly publishing engine for a Substack about how AI is reshaping engineering consulting.

This repository is the machine behind the newsletter. It does two jobs:

1. **Gathers** the week's most relevant news, research, and firm moves from a curated source
   list (the light automation: `scripts/gather.py`).
2. **Drafts** a publishable, on-voice article from that material through a fixed prompt chain
   run with Claude (the content system: `prompts/`, `templates/`, `docs/`).

You stay the author and the editor. The machine removes the blank-page problem and the
research grind, then enforces a consistent voice and a consistent structure so the archive
compounds into recognizable intellectual property over time.

## Who this is for

The named expert behind the newsletter (you). The reader is a decision maker at an
engineering consultancy. Two audiences, one beat:

- **AEC engineering consultancies**: Arup, AECOM, Jacobs, WSP, Stantec, and the like.
- **Engineering and digital practices inside management consultancies**: McKinsey, BCG,
  Accenture, Capgemini Engineering, and the like.

The thread that unites them: these are firms that sell engineering judgment by the hour, and
AI is repricing that judgment. See [docs/positioning.md](docs/positioning.md).

## How a week runs

The full checklist lives in [WEEKLY-WORKFLOW.md](WEEKLY-WORKFLOW.md). In short:

1. Run `python scripts/gather.py`. It writes a dated brief into `sources/briefs/`.
2. Open Claude in this repo and say "go". Claude runs the prompt chain in `prompts/`:
   research, angle, draft, edit and fact check, headline and social.
3. You edit the draft, then run a final independent Sonnet review pass over it.
4. You publish on Substack and post the two LinkedIn variants.

About thirty minutes of your time for a finished issue.

## Layout

```
docs/         positioning, voice rules, pillars, calendar, distribution, metrics
prompts/      the chain Claude runs each week, ending in an independent Sonnet review
templates/    the article skeleton, the brief shape, the predictions ledger
sources/      sources.yaml (what to track) and briefs/ (what gather.py produces)
scripts/      gather.py and its requirements
articles/     finished issues, ready to paste into Substack
```

## Setup once

```bash
cd AI-Researcher
python3 -m venv .venv && source .venv/bin/activate
pip install -r scripts/requirements.txt
python scripts/gather.py        # writes sources/briefs/<date>-brief.md
```

## The rules that never bend

The voice borrows the way Ray Dalio reasons, in plain words and cause and effect, while
keeping the vocabulary original. These bans are absolute and are checked before every publish:

- No "not X, but Y" antithesis constructions.
- No dash used as punctuation (no em dash, no en dash).
- No commands to the reader ("you have to," "you must," "you need to").
- No keeper idea labeled a "principle." It sits under "The throughline" in your own words.

The full set is in [docs/style-guide.md](docs/style-guide.md), which ends with a one-screen
pre-publish checklist. Read it before you ship anything.
