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

fig, ax = plt.subplots(figsize=(14.4, 6.4), dpi=150)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 14.4)
ax.set_ylim(0, 6.7)
ax.axis("off")

ax.text(0.55, 6.15, "Workers 22 to 25, employment change since Nov 2022", fontsize=24, fontweight="bold", color=INK, family="DejaVu Sans")
ax.text(0.55, 5.72, "Real time payroll data, Stanford Digital Economy Lab's Canaries Dashboard, through June 2026.", fontsize=13, color=GRAY, family="DejaVu Sans")

# Diverging bar chart
plot_x0, plot_x1 = 0.9, 8.6
zero_y = 3.05
bar_half_h = 0.7
bar_gap = 1.5

bars = [
    {"label": "Least AI-exposed\noccupations", "value": 10, "color": GREEN_DARK, "y": zero_y + bar_gap / 2},
    {"label": "Most AI-exposed\noccupations", "value": -11, "color": STONE, "y": zero_y - bar_gap / 2},
]

max_abs = 11
scale = 3.1 / max_abs  # inches per percentage point

ax.plot([plot_x0, plot_x0], [1.15, 5.0], color=BORDER, linewidth=1.0)

for b in bars:
    width = abs(b["value"]) * scale
    x = plot_x0 if b["value"] >= 0 else plot_x0 - width
    box = FancyBboxPatch((x, b["y"] - bar_half_h), width, bar_half_h * 2,
                          boxstyle="round,pad=0,rounding_size=0.06",
                          linewidth=0, facecolor=b["color"])
    ax.add_patch(box)
    label_x = plot_x0 + width + 0.25 if b["value"] >= 0 else plot_x0 - width - 0.25
    ha = "left" if b["value"] >= 0 else "right"
    sign = "+" if b["value"] >= 0 else ""
    ax.text(label_x, b["y"] + 0.18, f"{sign}{b['value']}%", fontsize=22, fontweight="bold", color=b["color"], ha=ha, family="DejaVu Sans")
    ax.text(label_x, b["y"] - 0.32, b["label"], fontsize=11, color=INK, ha=ha, va="top", linespacing=1.35, family="DejaVu Sans")

# Callout card: the widening gap
cx, cy, cw, ch = 9.6, 0.8, 4.15, 4.5
box = FancyBboxPatch((cx, cy), cw, ch, boxstyle="round,pad=0,rounding_size=0.14",
                      linewidth=1.2, edgecolor=BORDER, facecolor=CARD)
ax.add_patch(box)
bar = FancyBboxPatch((cx, cy), 0.08, ch, boxstyle="round,pad=0,rounding_size=0.03",
                      linewidth=0, facecolor=GREEN_DARK)
ax.add_patch(bar)

tx = cx + 0.4
ax.text(tx, cy + ch - 0.55, "The gap is widening", fontsize=14.5, fontweight="bold", color=INK, family="DejaVu Sans")

ax.text(tx, cy + ch - 1.5, "19%", fontsize=34, fontweight="bold", color=GREEN_DARK, family="DejaVu Sans")
ax.text(tx, cy + ch - 2.05, "as of June 2026", fontsize=10.5, color=GRAY, family="DejaVu Sans")

ax.text(tx, cy + ch - 2.75, "up from", fontsize=10.5, color=GRAY, family="DejaVu Sans")
ax.text(tx, cy + ch - 3.35, "15%", fontsize=22, fontweight="bold", color=STONE, family="DejaVu Sans")
ax.text(tx, cy + ch - 3.78, "a year earlier (July 2025)", fontsize=10.5, color=GRAY, family="DejaVu Sans")

ax.text(tx, cy + 0.55, "Employment shortfall for 22\nto 25 year olds in the most\nAI-exposed occupations, vs.\nwhere it would sit had it kept\npace with less-exposed peers.",
        fontsize=9.6, color=INK, va="top", linespacing=1.4, family="DejaVu Sans")

ax.text(0.55, 0.35,
        "Source: Stanford Digital Economy Lab, Canaries Dashboard, August 2026 update. The shift shows up mainly as fewer young people hired, not more let go.",
        fontsize=9, color=GRAY, family="DejaVu Sans")

plt.tight_layout()
plt.savefig("/Users/lorelamarku/Desktop/AI Projects/AI-Researcher/assets/ai-exposed-employment-gap.png",
            facecolor=BG, bbox_inches="tight")
print("saved")
