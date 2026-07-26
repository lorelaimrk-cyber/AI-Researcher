import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

BG = "#F2EFE7"
CARD = "#EAE6DB"
INK = "#1F2A24"
GRAY = "#6B6F66"
GREEN = "#2F6B47"
GREEN_DARK = "#1F4E33"
BORDER = "#D9D4C6"

fig, ax = plt.subplots(figsize=(14.4, 6.6), dpi=150)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 14.4)
ax.set_ylim(0, 6.9)
ax.axis("off")

ax.text(0.55, 6.4, "The speed premium: two tests", fontsize=25, fontweight="bold", color=INK, family="DejaVu Sans")
ax.text(0.55, 5.98, "Both have to pass before a firm can charge for time instead of hours.", fontsize=13, color=GRAY, family="DejaVu Sans")

col_w = 6.65
col_h = 4.6
gap = 0.4
x0 = 0.55
y0 = 0.55

def card(x, y, w, h, accent):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.16",
                          linewidth=1.2, edgecolor=BORDER, facecolor=CARD)
    ax.add_patch(box)
    bar = FancyBboxPatch((x, y), 0.1, h, boxstyle="round,pad=0,rounding_size=0.03",
                          linewidth=0, facecolor=accent)
    ax.add_patch(bar)

card(x0, y0, col_w, col_h, GREEN_DARK)
ax.text(x0 + 0.4, y0 + col_h - 0.55, "1. The value test", fontsize=17, fontweight="bold", color=GREEN_DARK, family="DejaVu Sans")
ax.text(x0 + 0.4, y0 + col_h - 1.05, "Is the client's value of a week saved,\nin revenue booked early plus cost avoided,\nlarge next to the fee premium being asked?",
        fontsize=11.5, color=INK, va="top", linespacing=1.6, family="DejaVu Sans")
ax.text(x0 + 0.4, y0 + col_h - 2.75, "Port project: 15% acceleration created\n£75m in client value. A fee that moved by\na few percent of that pool is still a rounding\nerror to the client and real money to the firm.",
        fontsize=10.5, color=GRAY, va="top", linespacing=1.55, family="DejaVu Sans")
ax.text(x0 + 0.4, y0 + 0.35, "Fails when: the asset makes little money per\nday, or the schedule was never the constraint.",
        fontsize=10, color=GRAY, va="bottom", linespacing=1.5, family="DejaVu Sans")

x1 = x0 + col_w + gap
card(x1, y0, col_w, col_h, GREEN)
ax.text(x1 + 0.4, y0 + col_h - 0.55, "2. The proof test", fontsize=17, fontweight="bold", color=GREEN, family="DejaVu Sans")
ax.text(x1 + 0.4, y0 + col_h - 1.05, "Can the firm name the number of weeks or\nmonths it will pull forward, and stand behind\nit, rather than promise a general improvement?",
        fontsize=11.5, color=INK, va="top", linespacing=1.6, family="DejaVu Sans")
ax.text(x1 + 0.4, y0 + col_h - 2.75, "Generative scheduling tools that model\nthousands of paths through the work, not one\nbaseline plan, are what make a specific number\ndefensible instead of a sales line.",
        fontsize=10.5, color=GRAY, va="top", linespacing=1.55, family="DejaVu Sans")
ax.text(x1 + 0.4, y0 + 0.35, "Fails when: the case for speed is a story,\nnot a modelled, checkable number.",
        fontsize=10, color=GRAY, va="bottom", linespacing=1.5, family="DejaVu Sans")

plt.tight_layout()
plt.savefig("/Users/lorelamarku/Desktop/AI Projects/AI-Researcher/assets/speed-premium-framework.png", facecolor=BG, bbox_inches="tight")
print("saved")
