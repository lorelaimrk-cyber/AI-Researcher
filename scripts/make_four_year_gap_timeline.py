import matplotlib.pyplot as plt

BG = "#F2EFE7"
INK = "#1F2A24"
GRAY = "#6B6F66"
GREEN = "#2F6B47"
GREEN_DARK = "#1F4E33"
RED = "#B23A2E"
STONE = "#8C8272"
BORDER = "#D9D4C6"

fig, ax = plt.subplots(figsize=(14.4, 6.6), dpi=150)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis("off")

YEAR_MIN, YEAR_MAX = 2017.3, 2030.2
ax.set_xlim(YEAR_MIN, YEAR_MAX)
ax.set_ylim(0, 6.6)

ax.text(YEAR_MIN + 0.15, 6.15, "The four year gap", fontsize=25, fontweight="bold", color=INK, family="DejaVu Sans")
ax.text(YEAR_MIN + 0.15, 5.68,
        "How long it took artificial intelligence to go from a conference session to ChatGPT,\nand where quantum computing sits on the same clock.",
        fontsize=13, color=GRAY, family="DejaVu Sans", linespacing=1.5)

LINE_Y = 3.15
ax.plot([YEAR_MIN + 0.1, YEAR_MAX - 0.1], [LINE_Y, LINE_Y], color=BORDER, linewidth=2.5, zorder=1, solid_capstyle="round")

TODAY = 2026.4
ax.plot([TODAY, TODAY], [0.4, 5.35], color=STONE, linewidth=1.3, linestyle=(0, (5, 4)), zorder=1)
ax.text(TODAY, 5.5, "TODAY", fontsize=10.5, fontweight="bold", color=STONE, ha="center", family="DejaVu Sans")

events = [
    {"year": 2018.7, "y_label": "above", "color": STONE, "solid": True,
     "title": "Sept 2018", "body": "A session on AI at the\nBled Strategic Forum\nsounds like science fiction."},
    {"year": 2022.9, "y_label": "below", "color": GREEN_DARK, "solid": True,
     "title": "Nov 2022", "body": "The whole world gets\nChatGPT. Four years,\nstart to finish."},
    {"year": 2026.4, "y_label": "above", "color": INK, "solid": True,
     "title": "2026", "body": "A podcast raises the same\nfeeling about quantum\ncomputing and cryptography."},
    {"year": 2027.95, "y_label": "below", "color": GREEN, "solid": False,
     "title": "End of 2027", "body": "Prediction: a top 20 AEC\nfirm discloses a post quantum\nmigration plan. Confidence: medium."},
    {"year": 2029.0, "y_label": "above", "color": RED, "solid": True,
     "title": "2029", "body": "Google's own deadline to\nprotect its systems from a\ncapable quantum computer."},
]

for e in events:
    x = e["year"]
    marker_style = dict(marker="o", markersize=11, color=e["color"], zorder=5)
    if e["solid"]:
        ax.plot(x, LINE_Y, markerfacecolor=e["color"], markeredgecolor=BG, markeredgewidth=2, **marker_style)
    else:
        ax.plot(x, LINE_Y, markerfacecolor=BG, markeredgecolor=e["color"], markeredgewidth=2.4, **marker_style)

    if e["y_label"] == "above":
        stem_top = LINE_Y + 0.55
        text_y = LINE_Y + 0.75
        va = "bottom"
    else:
        stem_top = LINE_Y - 0.55
        text_y = LINE_Y - 0.75
        va = "top"

    ax.plot([x, x], [LINE_Y, stem_top], color=e["color"], linewidth=1.4, zorder=2)
    ax.text(x, text_y, e["title"], fontsize=13.5, fontweight="bold", color=e["color"],
            ha="center", va=va, family="DejaVu Sans")
    body_y = text_y + (0.42 if va == "bottom" else -0.42)
    ax.text(x, body_y, e["body"], fontsize=9.8, color=INK, ha="center", va=va,
            linespacing=1.5, family="DejaVu Sans")

ax.text(YEAR_MIN + 0.15, 0.35,
        "Bled Strategic Forum (Wikipedia); OpenAI; Google (blog.google, Mar 2026). The 2027 marker is the author's own dated prediction.",
        fontsize=8.7, color=GRAY, family="DejaVu Sans")

plt.tight_layout()
plt.savefig("/Users/lorelamarku/Desktop/AI Projects/AI-Researcher/assets/four-year-gap-timeline.png",
            facecolor=BG, bbox_inches="tight")
print("saved")
