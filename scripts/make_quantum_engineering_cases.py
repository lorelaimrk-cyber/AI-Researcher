import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

BG = "#F2EFE7"
CARD = "#EAE6DB"
INK = "#1F2A24"
GRAY = "#6B6F66"
GREEN = "#2F6B47"
GREEN_DARK = "#1F4E33"
STONE = "#8C8272"
BORDER = "#D9D4C6"

fig, ax = plt.subplots(figsize=(14.4, 8.0), dpi=150)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 14.4)
ax.set_ylim(0, 8.3)
ax.axis("off")

ax.text(0.55, 7.85, "Three engineering problems, already being tested", fontsize=24, fontweight="bold", color=INK, family="DejaVu Sans")
ax.text(0.55, 7.42, "Real pilots and papers, not hypotheticals. All three are still small scale.", fontsize=13, color=GRAY, family="DejaVu Sans")

card_w = 4.2
card_h = 6.15
gap = 0.35
x0 = 0.55
y0 = 0.55

cards = [
    {
        "title": "Routing traffic",
        "accent": GREEN_DARK,
        "problem": "Routing many vehicles\nthrough a city in\nnear real time.",
        "tried": "Volkswagen and D-Wave,\nLisbon, Nov 2019.\nNine public buses.",
        "status": "Live pilot.\nNot a lab demo.",
    },
    {
        "title": "Designing structures",
        "accent": GREEN,
        "problem": "Finding where material\ngoes in a beam to\nminimize flex under load.",
        "tried": "Ye, Qian, and Pan,\n2023. Classical computer\nplus quantum annealer.",
        "status": "Matched classical\nmethods on small\ntest problems.",
    },
    {
        "title": "Capturing carbon",
        "accent": STONE,
        "problem": "Designing a material\nthat binds CO2 cheaply.\nCement alone is ~8% of\nglobal emissions.",
        "tried": "Quantinuum, quantum\nsimulation of how MOFs\nbind CO2 molecules.",
        "status": "Simulation stage.\nNot yet a built\nmaterial.",
    },
]

for i, c in enumerate(cards):
    x = x0 + i * (card_w + gap)
    box = FancyBboxPatch((x, y0), card_w, card_h, boxstyle="round,pad=0,rounding_size=0.14",
                          linewidth=1.2, edgecolor=BORDER, facecolor=CARD)
    ax.add_patch(box)

    bar = FancyBboxPatch((x, y0), 0.09, card_h, boxstyle="round,pad=0,rounding_size=0.03",
                          linewidth=0, facecolor=c["accent"])
    ax.add_patch(bar)

    tx = x + 0.4
    ty = y0 + card_h - 0.55
    ax.text(tx, ty, c["title"], fontsize=15.5, fontweight="bold", color=c["accent"], family="DejaVu Sans")

    ax.text(tx, ty - 0.55, "THE PROBLEM", fontsize=9, fontweight="bold", color=GRAY, family="DejaVu Sans")
    ax.text(tx, ty - 0.85, c["problem"], fontsize=10.6, color=INK, va="top", linespacing=1.55, family="DejaVu Sans")

    ax.text(tx, ty - 2.55, "TRIED IN", fontsize=9, fontweight="bold", color=GRAY, family="DejaVu Sans")
    ax.text(tx, ty - 2.85, c["tried"], fontsize=10.6, color=INK, va="top", linespacing=1.55, family="DejaVu Sans")

    ax.plot([tx, x + card_w - 0.4], [y0 + 1.35, y0 + 1.35], color=BORDER, linewidth=1.0)
    ax.text(tx, y0 + 1.1, "STATUS TODAY", fontsize=9, fontweight="bold", color=c["accent"], family="DejaVu Sans")
    ax.text(tx, y0 + 0.8, c["status"], fontsize=10.6, color=INK, va="top", linespacing=1.55, family="DejaVu Sans")

ax.text(0.55, 0.15,
        "Volkswagen Group; arXiv 2301.11531 (Ye, Qian, Pan); Quantinuum. None of these beat classical software at real project scale yet.",
        fontsize=8.7, color=GRAY, family="DejaVu Sans")

plt.tight_layout()
plt.savefig("/Users/lorelamarku/Desktop/AI Projects/AI-Researcher/assets/quantum-engineering-cases.png",
            facecolor=BG, bbox_inches="tight")
print("saved")
