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
glowing neon, blue cyberspace, circuit board patterns, holograms, robots,
humanoid AI, brain imagery, binary digits, lens flare, photorealism,
3D render, dark background, purple, cyan, text, lettering, watermark
```

---

## 2026-09-05, The Boundary You Can Point To

Subject: local AI, data governance, the boundary data does not cross.

```
Rich editorial illustration for an engineering business publication, in the
style of a detailed technical drawing rendered as flat vector art.

Scene: a server rack, drawn in careful detail with individual units, vents,
patch panels and neatly routed cabling, stands inside a boundary drawn like
a surveyed property line on an architect's site plan, a precise closed
rectangle with tick marks, corner markers and small dimension arrows along
its edges. Around and beneath it, a dense architectural underlay fills the
frame: overlapping floor plans, elevation drawings, grid lines, section
marks, hatching, contour lines and small annotation blocks, layered like
several drawings stacked on a light table. Outside the boundary, a network
of thin routing lines and connection nodes travels across the sheet from
the edges of the frame, converging on the boundary and terminating cleanly
at it, none crossing over.

Style: flat vector, precise draughtsman linework, layered and detailed
rather than sparse, subtle paper grain, gentle tonal panels behind sections
of the drawing to create depth. No gradients on objects, no glow, no 3D
lighting. Dense but organised, the density of a real engineering drawing
sheet, not clutter.

Composition: landscape 1200 x 630. Detail runs edge to edge, with one
calmer tonal panel in the left third where a headline can sit.

Colour, use only these: warm off-white paper #F2EFE7, panel tone #EAE6DB,
drawing underlay and rules #D9D4C6, dark linework #1F2A24, grey annotation
detail #6B6F66, deep green #1F4E33 for the server rack, mid green #2F6B47
for the boundary line, warm stone #8C8272 for the external routing lines
that stop at the boundary.

No text, no lettering, no numbers, no logos.
```

Note: the routing lines stopping at the boundary carry the whole argument.
If a generation loses that, regenerate rather than accept it.

### Variants

- **Warmer, less diagrammatic.** Overhead view of a drafting table: rolled
  drawings, a scale rule, a coffee cup, weighted-down plan sheets, and a
  single compact server unit sitting on the sheet inside a drawn boundary.
  Same palette, same flat vector treatment, more physical objects.
- **Fuller architectural.** Drop the rack to a small solid green form and
  let the layered site plan carry the frame, with the boundary and the
  terminating routing lines as the only accented elements.
