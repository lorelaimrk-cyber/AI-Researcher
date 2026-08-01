import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

BG = "#F2EFE7"
CARD = "#EAE6DB"
INK = "#1F2A24"
GRAY = "#6B6F66"
GREEN = "#2F6B47"
GREEN_DARK = "#1F4E33"
BORDER = "#D9D4C6"
RED = "#B23A2E"

fig, ax = plt.subplots(figsize=(14.4, 8.8), dpi=150)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 14.4)
ax.set_ylim(0.6, 9.2)
ax.axis("off")

ax.text(0.55, 8.65, "Are you buying activation, or are you buying value?", fontsize=25, fontweight="bold", color=INK, family="DejaVu Sans")
ax.text(0.55, 8.2, "Two questions. Cross them and four situations fall out.", fontsize=13.5, color=GRAY, family="DejaVu Sans")


def card(x, y, w, h, fc=CARD, ec=BORDER, lw=1.2, accent=None):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.14",
                          linewidth=lw, edgecolor=ec, facecolor=fc, mutation_aspect=1)
    ax.add_patch(box)
    if accent:
        bar = FancyBboxPatch((x, y), 0.08, h, boxstyle="round,pad=0,rounding_size=0.03",
                              linewidth=0, facecolor=accent)
        ax.add_patch(bar)


grid_x = 4.05
grid_w = 9.7
grid_top = 7.7
header_gap = 0.55
card_top = grid_top - header_gap
row_h = 3.0
row_gap = 0.35
col_gap = 0.35
col_w = (grid_w - col_gap) / 2

# row axis labels
ax.text(0.55, card_top - row_h / 2, "Rarely opens\nthe tool", fontsize=13, fontweight="bold", color=INK, ha="left", va="center", family="DejaVu Sans")
ax.text(0.55, card_top - row_h / 2 - 0.5, "(the quiet majority)", fontsize=9.5, color=GRAY, ha="left", va="center", family="DejaVu Sans")

ax.text(0.55, card_top - row_h - row_gap - row_h / 2, "Opens it\nconstantly", fontsize=13, fontweight="bold", color=INK, ha="left", va="center", family="DejaVu Sans")
ax.text(0.55, card_top - row_h - row_gap - row_h / 2 - 0.5, "(the heavy user)", fontsize=9.5, color=GRAY, ha="left", va="center", family="DejaVu Sans")

# column headers
ax.text(grid_x + col_w / 2, grid_top + 0.32, "No proven value", fontsize=12.5, fontweight="bold", color=INK, ha="center", family="DejaVu Sans")
ax.text(grid_x + col_w / 2, grid_top - 0.05, "nobody checked the output against an outcome", fontsize=9.5, color=GRAY, ha="center", family="DejaVu Sans")

ax.text(grid_x + col_w + col_gap + col_w / 2, grid_top + 0.32, "Proven value", fontsize=12.5, fontweight="bold", color=INK, ha="center", family="DejaVu Sans")
ax.text(grid_x + col_w + col_gap + col_w / 2, grid_top - 0.05, "tied to a margin, an error rate, a deadline held", fontsize=9.5, color=GRAY, ha="center", family="DejaVu Sans")

cells = [
    {
        "x": grid_x, "y": card_top - row_h, "title": "Shelfware",
        "body": "The seat nobody checks.\nPaid for either way. The\nlicense fee is the only\nfact anyone has.",
        "accent": GRAY, "titlecolor": GRAY,
    },
    {
        "x": grid_x + col_w + col_gap, "y": card_top - row_h, "title": "The efficient specialist",
        "body": "Uses it for one task, gets\nit right, moves on. What\nan activation dashboard\nmisses entirely.",
        "accent": GREEN_DARK, "titlecolor": GREEN_DARK,
    },
    {
        "x": grid_x, "y": card_top - 2 * row_h - row_gap, "title": "Token theater",
        "body": "Volume with no check on\nthe output. More logins,\nno more value: the\nGoodhart trap in action.",
        "accent": RED, "titlecolor": RED,
    },
    {
        "x": grid_x + col_w + col_gap, "y": card_top - 2 * row_h - row_gap, "title": "The real win",
        "body": "Heavy use tied to a\nmeasured outcome. Rare,\nand the one combination\nworth building toward.",
        "accent": GREEN, "titlecolor": GREEN,
    },
]

for c in cells:
    card(c["x"], c["y"], col_w, row_h, accent=c["accent"])
    ax.text(c["x"] + 0.35, c["y"] + row_h - 0.5, c["title"], fontsize=14, fontweight="bold", color=c["titlecolor"], family="DejaVu Sans")
    ax.text(c["x"] + 0.35, c["y"] + row_h - 0.95, c["body"], fontsize=10.8, color=INK, va="top", linespacing=1.55, family="DejaVu Sans")

plt.tight_layout()
plt.savefig("/Users/lorelamarku/Desktop/AI projects/AI-Researcher/assets/activation-value-matrix.png", facecolor=BG, bbox_inches="tight")
print("saved")
