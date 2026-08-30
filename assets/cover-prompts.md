# Cover image prompts

House recipe for AI-Researcher cover images. Keep the palette fixed so covers read as one
family with the charts in `assets/`. Always generate text-free: image models mangle lettering,
and the title gets overlaid on Substack anyway.

Palette (same constants used by every `scripts/make_*.py`):

| Role | Hex |
|---|---|
| Paper background | `#F2EFE7` |
| Panel / card tone | `#EAE6DB` |
| Rules, underlay, borders | `#D9D4C6` |
| Ink linework | `#1F2A24` |
| Muted grey detail | `#6B6F66` |
| Primary accent green | `#1F4E33` |
| Secondary accent green | `#2F6B47` |
| Warm stone counterpoint | `#8C8272` |
| Alert red, sparingly | `#B23A2E` |

Standard negative prompt:

```
title block, drawing sheet, blueprint sheet, legend, key, callouts,
annotations, labels, dimension lines, specifications, technical diagram,
schematic, isometric drawing, tables, panels of text, text, lettering,
numbers, watermark, glowing neon, blue cyberspace, circuit patterns,
holograms, robots, humanoid AI, brain imagery, binary digits, lens flare,
3D render, photorealism, dark background, purple, cyan
```

## Size

LinkedIn article cover is **1200 x 644** (about 1.86:1). Substack post cover
is **1200 x 630**. Near enough that one generation serves both.

Image generators respect aspect ratio but almost never the pixel size you
type, so set the tool's own ratio control to **1.91:1** or **16:9**, whichever
it offers, then fix the exact pixels afterwards:

```
python scripts/make_cover.py raw-generation.png assets/2026-09-05-cover.png
python scripts/make_cover.py raw-generation.png --substack
python scripts/make_cover.py raw-generation.png --anchor top
```

It centre-crops to the right ratio then resizes, so nothing gets squashed.
Use `--anchor` when the subject sits off centre.

## Two failure modes, both seen

1. **Describing a drawing sheet gets you a drawing sheet.** The first attempt
   asked for "the density of a real engineering drawing sheet" and returned a
   full technical document with a title block and a legend panel. A cover is a
   magazine graphic, not a document. Say so explicitly.
2. **Words implying labels produce fake text.** "Annotation blocks",
   "dimension strings", "specifications" and "callouts" all make a model spray
   garbled lettering across the image, no matter how firmly the prompt says no
   text. Keep them out of the positive prompt entirely.

Density on a cover comes from depth, soft background shapes and paper grain.
It never comes from more information. The image has to survive being seen at
thumbnail size in a feed.

---

## 2026-09-05, The Boundary You Can Point To

Subject: local AI, data governance, the boundary data does not cross.

Set the generator's aspect ratio to 1.91:1 or 16:9, then run the result
through `scripts/make_cover.py`.

```
Editorial cover illustration for a business article, in the style of a
modern magazine cover graphic. Wide landscape banner, aspect ratio 1.91:1.

One dominant subject, large and centred slightly right: a single server
cabinet as a bold simplified geometric form in deep green, with just
enough shading on its side faces to read as solid and three-dimensional.
Around its base, a wide flat plane suggesting a floor, in warm stone tone.
A single confident boundary line encircles the cabinet on that plane,
clearly closed. From the outer edges of the frame, four or five thick soft
lines sweep inward toward the cabinet and stop short at the boundary, none
crossing it.

Background: large soft overlapping geometric shapes in muted paper tones,
suggesting architectural plan forms abstractly, heavily blurred and very
low contrast, working as texture and depth only. Subtle paper grain across
the whole image. Warm, calm, confident.

Style: bold flat editorial illustration with soft depth. Simple shapes at
large scale. Must read clearly as a thumbnail. Rich and warm rather than
sparse, but with few distinct elements.

Colour, use only these: warm off-white #F2EFE7, panel tone #EAE6DB, soft
rules #D9D4C6, dark ink #1F2A24, grey #6B6F66, deep green #1F4E33 for the
cabinet, mid green #2F6B47 for the boundary line, warm stone #8C8272 for
the inward sweeping lines.

Left third kept calm and uncluttered for a headline overlay.
```

Note: the lines stopping at the boundary carry the whole argument. If a
generation loses that, regenerate rather than accept it.

### Variants

- **Warmer, more physical.** Overhead view of a drafting table: rolled
  drawings, a scale rule, weighted-down plan sheets, and one compact server
  unit sitting inside a drawn boundary. Same palette, same flat treatment,
  real objects instead of abstract shapes.
- **Quieter.** Drop the cabinet to a small solid green form and let the soft
  background plan shapes carry the frame, with the boundary and the
  terminating lines as the only accented elements.
