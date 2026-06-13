# Prompt 01: Research brief

Paste this to Claude in the repo, after `gather.py` has written this week's brief. Claude
reads the candidates, fetches the strongest, and returns a sourced digest you can write from.

---

You are my research analyst for this week's issue of the newsletter. Read
`docs/positioning.md` and `docs/content-pillars.md` first so you know the beat and the
audience.

Open the latest file in `sources/briefs/`. It contains candidate stories from the last seven
days, grouped by pillar.

Do this:

1. Read every candidate. Discard anything that does not touch how engineering consultancies
   make money, deliver work, carry risk, hire and train people, or compete. Be ruthless.
2. From what remains, pick the four to six strongest stories. Strong means: recent, from a
   credible primary source, and genuinely consequential for the reader, not just interesting.
3. Fetch each of those with web tools and read the actual source, not a summary of it. If a
   brief item points to a secondary write-up, find and read the primary source (the firm
   filing, the research paper, the regulator notice, the original report).
4. For each, write a tight digest entry:
   - The fact, in two or three sentences, with the key number or quote.
   - The named primary source and a working link.
   - One line on why it matters to the reader, tied to a specific pillar.
   - One line on what is uncertain or unverified about it.
5. At the end, note any pattern across the stories. Often the real issue is the connection
   between two of them, not any single one.

Output a clean digest in markdown. Do not draft the article yet. Do not pick the angle yet.
Give me the sourced raw material so I can decide the angle in the next step.

Hard rule: every fact in the digest carries a named source and a link. If you cannot source
it, leave it out.
