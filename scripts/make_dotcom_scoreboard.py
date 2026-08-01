import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

BG = "#F2EFE7"
CARD = "#EAE6DB"
INK = "#1F2A24"
GRAY = "#6B6F66"
STONE = "#8C8272"      # dot-com era series
GREEN = "#2F6B47"      # AI era series
GREEN_DARK = "#1F4E33"
RED = "#B23A2E"
BORDER = "#D9D4C6"

fig, ax = plt.subplots(figsize=(14.4, 9.0), dpi=150)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 14.4)
ax.set_ylim(0, 9.4)
ax.axis("off")

ax.text(0.55, 8.9, "Dot-com era vs AI era: the scoreboard", fontsize=25, fontweight="bold", color=INK, family="DejaVu Sans")
ax.text(0.55, 8.45, "Where the numbers rhyme with 1999, and where they don't.", fontsize=13, color=GRAY, family="DejaVu Sans")

# legend
lx = 0.55
ly = 7.95
ax.add_patch(FancyBboxPatch((lx, ly), 0.34, 0.2, boxstyle="round,pad=0,rounding_size=0.06", linewidth=0, facecolor=STONE))
ax.text(lx + 0.46, ly + 0.10, "Dot-com, 1999–2000", fontsize=11, color=INK, va="center", family="DejaVu Sans")
ax.add_patch(FancyBboxPatch((lx + 2.6, ly), 0.34, 0.2, boxstyle="round,pad=0,rounding_size=0.06", linewidth=0, facecolor=GREEN))
ax.text(lx + 3.06, ly + 0.10, "AI, 2024–2026", fontsize=11, color=INK, va="center", family="DejaVu Sans")


def chip(x, y, text, color):
    w = 0.22 + 0.135 * len(text)
    ax.add_patch(FancyBboxPatch((x, y), w, 0.34, boxstyle="round,pad=0,rounding_size=0.12",
                                 linewidth=0, facecolor=color))
    ax.text(x + w / 2, y + 0.17, text, fontsize=9, color="#FFFFFF", ha="center", va="center",
            fontweight="bold", family="DejaVu Sans")


def panel(x, y, w, h, title, rows, chip_text, chip_color, suffix="x"):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.14",
                          linewidth=1.2, edgecolor=BORDER, facecolor=CARD)
    ax.add_patch(box)
    ax.text(x + 0.35, y + h - 0.48, title, fontsize=13, fontweight="bold", color=INK, family="DejaVu Sans")
    chip(x + w - 0.35 - (0.22 + 0.135 * len(chip_text)), y + h - 0.62, chip_text, chip_color)

    max_val = max(v for _, v, _ in rows)
    bar_area_w = w - 2.75
    bar_x = x + 1.85
    bar_h = 0.34
    by = y + h - 1.15
    for name, val, color in rows:
        ax.text(bar_x - 0.12, by + bar_h / 2, name, fontsize=10, color=GRAY, ha="right", va="center", family="DejaVu Sans")
        bw = max(bar_area_w * val / max_val, 0.15)
        ax.add_patch(FancyBboxPatch((bar_x, by), bw, bar_h, boxstyle="round,pad=0,rounding_size=0.07",
                                     linewidth=0, facecolor=color))
        ax.text(bar_x + bw + 0.12, by + bar_h / 2, f"{val:g}{suffix}",
                fontsize=11, fontweight="bold", color=INK, va="center", family="DejaVu Sans")
        by -= bar_h + 0.22


panel_w = 8.6
panel_h = 2.15
panel_gap = 0.3
px = 0.55
py = 7.55 - panel_h

panel(px, py, panel_w, panel_h, "Nasdaq-100, forward P/E",
      [("1999", 60, STONE), ("now", 26, GREEN)], "differs", GREEN_DARK)

py -= panel_h + panel_gap
panel(px, py, panel_w, panel_h, "Flagship stock, P/E at peak",
      [("Cisco", 200, STONE), ("Nvidia", 47, GREEN)], "differs", GREEN_DARK)

py -= panel_h + panel_gap
panel(px, py, panel_w, panel_h, "Shiller CAPE, whole market",
      [("1999", 44, STONE), ("now", 41, GREEN)], "rhymes", RED, suffix="")

# stat tiles on the right
tile_x = px + panel_w + 0.35
tile_w = 14.4 - tile_x - 0.55
tile_h = (3 * panel_h + 2 * panel_gap - 0.3) / 2
ty = 7.55 - tile_h

def tile(y, big, caption, chip_text, chip_color):
    box = FancyBboxPatch((tile_x, y), tile_w, tile_h, boxstyle="round,pad=0,rounding_size=0.14",
                          linewidth=1.2, edgecolor=BORDER, facecolor=CARD)
    ax.add_patch(box)
    chip(tile_x + 0.35, y + tile_h - 0.62, chip_text, chip_color)
    ax.text(tile_x + 0.35, y + tile_h - 1.45, big, fontsize=30, fontweight="bold", color=GREEN_DARK, family="DejaVu Sans")
    ax.text(tile_x + 0.35, y + tile_h - 1.85, caption, fontsize=10, color=INK, va="top", linespacing=1.45, family="DejaVu Sans")

tile(ty, "$320B", "Big-tech capex in 2026 alone,\nmost of it AI. More than the\nwhole telecom buildout.", "rhymes", RED)
ty -= tile_h + 0.3
tile(ty, "61%", "Share of all global venture\nmoney that went to AI\nin 2025.", "rhymes", RED)

ax.text(0.55, 0.18, "Sources: IntuitionLabs comparison of company filings and market data; Nasdaq.com; Yahoo Finance. Figures as reported, 2026.",
        fontsize=9, color=GRAY, family="DejaVu Sans")

plt.tight_layout()
plt.savefig("/Users/lorelamarku/Desktop/AI Projects/AI-Researcher/assets/dotcom-ai-scoreboard.png", facecolor=BG, bbox_inches="tight")
print("saved")
