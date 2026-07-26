import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

BG = "#F2EFE7"
CARD = "#EAE6DB"
INK = "#1F2A24"
GRAY = "#6B6F66"
GREEN = "#2F6B47"
GREEN_DARK = "#1F4E33"
BORDER = "#D9D4C6"

fig, ax = plt.subplots(figsize=(14.4, 7.6), dpi=150)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 14.4)
ax.set_ylim(0, 7.9)
ax.axis("off")

ax.text(0.55, 7.35, "One partnership's numbers, in cash terms", fontsize=24, fontweight="bold", color=INK, family="DejaVu Sans")
ax.text(0.55, 6.92, "Three McKinsey and ALICE Technologies case studies. The fee for the work is a rounding error against this.", fontsize=13, color=GRAY, family="DejaVu Sans")

card_w = 4.2
card_h = 4.7
gap = 0.35
x0 = 0.55
y0 = 1.55

cards = [
    {
        "title": "Port expansion",
        "metric": "15%+",
        "metric_label": "schedule acceleration",
        "value": "£75m",
        "value_label": "£60m revenue booked early\n+ £15m lower labour cost",
    },
    {
        "title": "Electronics plant",
        "metric": "6 weeks",
        "metric_label": "pulled forward, from\n3 months behind",
        "value": "£37m+",
        "value_label": "combined cost savings\nand revenue acceleration",
    },
    {
        "title": "Transit guideway",
        "metric": "13 months",
        "metric_label": "delay recovered",
        "value": "£60m",
        "value_label": "in flagged risk,\nworked out of the plan",
    },
]

for i, c in enumerate(cards):
    x = x0 + i * (card_w + gap)
    box = FancyBboxPatch((x, y0), card_w, card_h, boxstyle="round,pad=0,rounding_size=0.14",
                          linewidth=1.2, edgecolor=BORDER, facecolor=CARD)
    ax.add_patch(box)
    bar = FancyBboxPatch((x, y0), 0.08, card_h, boxstyle="round,pad=0,rounding_size=0.03",
                          linewidth=0, facecolor=GREEN_DARK)
    ax.add_patch(bar)

    ax.text(x + 0.35, y0 + card_h - 0.55, c["title"], fontsize=14.5, fontweight="bold", color=INK, family="DejaVu Sans")

    ax.text(x + 0.35, y0 + card_h - 1.35, c["metric"], fontsize=26, fontweight="bold", color=GREEN_DARK, family="DejaVu Sans")
    ax.text(x + 0.35, y0 + card_h - 1.85, c["metric_label"], fontsize=10, color=GRAY, va="top", linespacing=1.4, family="DejaVu Sans")

    ax.text(x + 0.35, y0 + 1.55, c["value"], fontsize=22, fontweight="bold", color=GREEN, family="DejaVu Sans")
    ax.text(x + 0.35, y0 + 1.1, c["value_label"], fontsize=10, color=INK, va="top", linespacing=1.4, family="DejaVu Sans")

ax.text(0.55, 0.9, "Across 35+ clients in infrastructure, data centres, energy, mining, and manufacturing: schedule accelerations of up to 20%.",
        fontsize=11, color=GRAY, family="DejaVu Sans")
ax.text(0.55, 0.5, "Source: McKinsey and ALICE Technologies, generative scheduling case studies, published July 9, 2026 (ALICE Technologies blog).",
        fontsize=9, color=GRAY, family="DejaVu Sans")

plt.tight_layout()
plt.savefig("/Users/lorelamarku/Desktop/AI Projects/AI-Researcher/assets/speed-premium-evidence.png", facecolor=BG, bbox_inches="tight")
print("saved")
