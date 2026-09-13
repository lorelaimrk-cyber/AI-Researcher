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

---

## 2026-09-19, Nobody Banned the Car

Subject: the car kept running while the rules landed on the driver, the plate and the border.

Set the generator's aspect ratio to 1.91:1 or 16:9, then run the result
through `scripts/make_cover.py`. No frame or border around the image; the
illustration runs to the edges.

```
Editorial cover illustration for a business article, in the style of a
modern magazine cover graphic. Wide landscape banner, aspect ratio 1.91:1.
The illustration fills the whole canvas edge to edge, with no border, frame,
margin or vignette.

One dominant subject, large and placed in the right two thirds: a single
early 1900s motor car, boxy and upright with large spoked wheels, as a bold
simplified geometric form in deep green, with just enough shading on its
side faces to read as solid. It sits on an open road drawn as a wide flat
band in warm stone tone that runs from the bottom edge toward a low
horizon. On the front of the car, one small blank rectangular plate in
off-white, empty, no marks on it. Beside the road, a short row of three or
four small round and triangular sign shapes on thin posts, in mid green,
blank faces, receding with the road.

Background: a broad low sky in paper tones with large soft overlapping
shapes, blurred and very low contrast, suggesting distant hills and a few
cloud forms, working as texture and depth only. Subtle paper grain across
the whole image. Warm, calm, confident, with a sense of open distance
ahead of the car.

Style: bold flat editorial illustration with soft depth. Simple shapes at
large scale, few distinct elements, but rich and warm rather than sparse.
Must read clearly as a thumbnail.

Colour, use only these: warm off-white #F2EFE7, panel tone #EAE6DB, soft
rules #D9D4C6, dark ink #1F2A24, grey #6B6F66, deep green #1F4E33 for the
car, mid green #2F6B47 for the sign shapes, warm stone #8C8272 for the
road, alert red #B23A2E only as one small accent on a single sign face.

Left third kept calm and uncluttered for a headline overlay.
```

Note: the plate has to stay blank. If a generation puts lettering on it or
on the signs, regenerate. The road running off the edge is what says the
factories never stopped; keep it open, no barrier, no gate.

### Variants

- **Closer and warmer.** Three quarter view of the car from the front, the
  blank plate large and central, the signs reduced to one round shape at the
  roadside.
- **Quieter.** Car small on the horizon, the road band and the row of blank
  signs carry the frame.
