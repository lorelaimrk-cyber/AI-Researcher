import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib import font_manager

BG = "#F2EFE7"
CARD = "#EAE6DB"
INK = "#1F2A24"
GRAY = "#6B6F66"
GREEN = "#2F6B47"
GREEN_DARK = "#1F4E33"
BORDER = "#D9D4C6"

fig, ax = plt.subplots(figsize=(14.4, 8.8), dpi=150)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 14.4)
ax.set_ylim(0.6, 9.2)
ax.axis("off")

ax.text(0.55, 8.65, "Where does your IP actually sit?", fontsize=27, fontweight="bold", color=INK, family="DejaVu Sans")
ax.text(0.55, 8.2, "Two questions. Cross them and four boxes fall out.", fontsize=13.5, color=GRAY, family="DejaVu Sans")

col_x = [0.55, 3.55, 11.4]
row_y = [1.0, 4.55]
cell_w = 5.1
cell_h = 3.15
gap = 0.15

def card(x, y, w, h, fc=CARD, ec=BORDER, lw=1.2, accent=None):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.14",
                          linewidth=lw, edgecolor=ec, facecolor=fc, mutation_aspect=1)
    ax.add_patch(box)
    if accent:
        bar = FancyBboxPatch((x, y), 0.08, h, boxstyle="round,pad=0,rounding_size=0.03",
                              linewidth=0, facecolor=accent)
        ax.add_patch(bar)

label_x = 3.55
grid_x = 4.05
grid_w = 9.7
grid_top = 7.7
header_gap = 0.55
card_top = grid_top - header_gap
row_h = 3.0
row_gap = 0.35
col_gap = 0.35
col_w = (grid_w - col_gap) / 2

# axis labels
ax.text(0.55, card_top - row_h / 2, "Tool trains\non input", fontsize=13, fontweight="bold", color=INK, ha="left", va="center", family="DejaVu Sans")
ax.text(0.55, card_top - row_h / 2 - 0.42, "(consumer, fine-tuned)", fontsize=9.5, color=GRAY, ha="left", va="center", family="DejaVu Sans")

ax.text(0.55, card_top - row_h - row_gap - row_h / 2, "Tool does not\ntrain on input", fontsize=13, fontweight="bold", color=INK, ha="left", va="center", family="DejaVu Sans")
ax.text(0.55, card_top - row_h - row_gap - row_h / 2 - 0.42, "(enterprise, RAG, self-hosted)", fontsize=9.5, color=GRAY, ha="left", va="center", family="DejaVu Sans")

ax.text(grid_x + col_w / 2, grid_top + 0.32, "Content is common", fontsize=12.5, fontweight="bold", color=INK, ha="center", family="DejaVu Sans")
ax.text(grid_x + col_w / 2, grid_top - 0.05, "boilerplate, templates, standard notes", fontsize=9.5, color=GRAY, ha="center", family="DejaVu Sans")

ax.text(grid_x + col_w + col_gap + col_w / 2, grid_top + 0.32, "Content is distinctive", fontsize=12.5, fontweight="bold", color=INK, ha="center", family="DejaVu Sans")
ax.text(grid_x + col_w + col_gap + col_w / 2, grid_top - 0.05, "a firm's own judgment, a rare call", fontsize=9.5, color=GRAY, ha="center", family="DejaVu Sans")

cells = [
    {
        "x": grid_x, "y": card_top - row_h, "title": "The quiet leak",
        "body": "Easy to miss. Staff are\nquietly helping train the\nnext model version on the\nindustry's baseline work.",
        "accent": "#B23A2E", "titlecolor": "#B23A2E",
    },
    {
        "x": grid_x + col_w + col_gap, "y": card_top - row_h, "title": "Keep this box empty",
        "body": "Unlikely to be memorized\nword for word. Keep it out\nanyway. This is what makes\na firm distinctive.",
        "accent": "#B23A2E", "titlecolor": "#B23A2E",
    },
    {
        "x": grid_x, "y": card_top - 2 * row_h - row_gap, "title": "Nothing to fix",
        "body": "Low value data, no lasting\nexposure. Not where\nattention needs to go.",
        "accent": GRAY, "titlecolor": GRAY,
    },
    {
        "x": grid_x + col_w + col_gap, "y": card_top - 2 * row_h - row_gap, "title": "Where the edge should live",
        "body": "The one box where real\njudgment belongs near AI.\nConfirm the no-training\npromise is enforced.",
        "accent": GREEN_DARK, "titlecolor": GREEN_DARK,
    },
]

for c in cells:
    card(c["x"], c["y"], col_w, row_h, accent=c["accent"])
    ax.text(c["x"] + 0.35, c["y"] + row_h - 0.5, c["title"], fontsize=14, fontweight="bold", color=c["titlecolor"], family="DejaVu Sans")
    ax.text(c["x"] + 0.35, c["y"] + row_h - 0.95, c["body"], fontsize=10.8, color=INK, va="top", linespacing=1.55, family="DejaVu Sans")

plt.tight_layout()
plt.savefig("/Users/lorelamarku/Desktop/AI Projects/AI-Researcher/assets/ip-exposure-matrix.png", facecolor=BG, bbox_inches="tight")
print("saved")
