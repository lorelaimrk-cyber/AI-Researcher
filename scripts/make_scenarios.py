import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

BG = "#F2EFE7"
CARD = "#EAE6DB"
INK = "#1F2A24"
GRAY = "#6B6F66"
GREEN = "#2F6B47"
GREEN_DARK = "#1F4E33"
RED = "#B23A2E"
STONE = "#8C8272"
BORDER = "#D9D4C6"

fig, ax = plt.subplots(figsize=(14.4, 7.4), dpi=150)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 14.4)
ax.set_ylim(0, 7.7)
ax.axis("off")

ax.text(0.55, 7.15, "Three scenarios, one survival trait", fontsize=24, fontweight="bold", color=INK, family="DejaVu Sans")
ax.text(0.55, 6.72, "They differ mainly in timing. Revenue that doesn't depend on the boom wins in all three.", fontsize=13, color=GRAY, family="DejaVu Sans")

card_w = 4.2
card_h = 5.0
gap = 0.35
x0 = 0.55
y0 = 1.0

def curve_rhyme(t):
    rise = 0.55 * t / 0.3
    crash = 0.55 - 0.75 * (t - 0.3) / 0.15
    recover = -0.2 + 1.1 * (t - 0.45) / 0.55
    return np.where(t < 0.3, rise, np.where(t < 0.45, crash, recover))

def curve_holds(t):
    return 0.9 * t ** 1.15

def curve_middle(t):
    base = 0.75 * t
    dip = -0.18 * np.exp(-((t - 0.5) ** 2) / 0.008)
    return base + dip

cards = [
    {
        "title": "The rhyme plays out",
        "accent": RED,
        "curve": curve_rhyme,
        "body": "A correction. AI budgets freeze\nfor a year or two. Firms priced\non endless spending follow the\nFast Five. The technology wins\nanyway, and the survivors\ninherit it cheap.",
    },
    {
        "title": "The difference holds",
        "accent": GREEN,
        "curve": curve_holds,
        "body": "Real earnings keep supporting\nthe spending. No crash, the\nbuildout continues. Returns still\nconcentrate: most of the 2025\nventure cohort won't capture\nthem.",
    },
    {
        "title": "The middle",
        "accent": STONE,
        "curve": curve_middle,
        "body": "A partial correction, uneven by\nsector. Client AI spending slows\nbut doesn't stop. The gap\nbetween diversified firms and\none-story firms widens quietly.",
    },
]

for i, c in enumerate(cards):
    x = x0 + i * (card_w + gap)
    box = FancyBboxPatch((x, y0), card_w, card_h, boxstyle="round,pad=0,rounding_size=0.14",
                          linewidth=1.2, edgecolor=BORDER, facecolor=CARD)
    ax.add_patch(box)

    # sparkline area at the top of the card
    sx0 = x + 0.4
    sx1 = x + card_w - 0.4
    sy0 = y0 + card_h - 1.9
    sy1 = y0 + card_h - 0.55
    t = np.linspace(0, 1, 200)
    v = c["curve"](t)
    v = (v - v.min()) / (v.max() - v.min())
    xs = sx0 + t * (sx1 - sx0)
    ys = sy0 + v * (sy1 - sy0)
    ax.plot(xs, ys, color=c["accent"], linewidth=2.4, solid_capstyle="round", zorder=5)
    ax.plot([sx0, sx1], [sy0 - 0.08, sy0 - 0.08], color=BORDER, linewidth=1.2, zorder=4)
    ax.plot(xs[-1], ys[-1], marker="o", markersize=5.5, color=c["accent"], zorder=6)

    ax.text(x + 0.4, y0 + card_h - 2.35, c["title"], fontsize=14.5, fontweight="bold", color=c["accent"], family="DejaVu Sans")
    ax.text(x + 0.4, y0 + card_h - 2.75, c["body"], fontsize=10.3, color=INK, va="top", linespacing=1.5, family="DejaVu Sans")

ax.text(0.55, 0.45, "Historical pattern: MarchFirst and Scient outcomes 2000–2002 (Computerworld; E-Commerce Times); Amazon fundamentals through the crash (HBS Online).",
        fontsize=9, color=GRAY, family="DejaVu Sans")

plt.tight_layout()
plt.savefig("/Users/lorelamarku/Desktop/AI Projects/AI-Researcher/assets/dotcom-ai-scenarios.png", facecolor=BG, bbox_inches="tight")
print("saved")
