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

ax.text(0.55, 7.85, "Three preconditions for running AI in house", fontsize=24, fontweight="bold", color=INK, family="DejaVu Sans")
ax.text(0.55, 7.42, "Independent of each other. One is enough to decide it. Checked against 2026 figures.", fontsize=13, color=GRAY, family="DejaVu Sans")

card_w = 4.2
card_h = 6.15
gap = 0.35
x0 = 0.55
y0 = 0.55

cards = [
    {
        "title": "1. Obligation",
        "accent": GREEN_DARK,
        "q": "Does a contract or a\nregulation already fix\nwhere data may go?",
        "detail": "EU: whose law reaches it.\nSchrems II plus the CLOUD\nAct. Residency is not\ncontrol of the stack.\nUS: who may see it. ITAR,\nCUI under 32 CFR 2002.\nChina: whether it may\nleave. PIPL, three routes.",
        "verdict": "If yes, this one is\nsettled. Nothing\nbelow it matters.",
    },
    {
        "title": "2. Volume",
        "accent": GREEN,
        "q": "Is throughput past the\ncrossover where owned\nhardware pays off?",
        "detail": "Break-even sits near\n2M tokens a day. Below\n1M, hosted is cheaper.\nOne deployment serving\nseveral applications\npulls that forward.",
        "verdict": "Staffing to run the\nstack routinely costs\nmore than the GPUs.",
    },
    {
        "title": "3. Capability",
        "accent": STONE,
        "q": "Is the open-weight model\ngood enough for the\nspecific task?",
        "detail": "Leading open-weight models\nreached 85% to 95% of\nfrontier composite scores\nin a July 2026 comparison.\nGaps persist on hard\nmulti-step reasoning.",
        "verdict": "Rarely the binding\nconstraint now for\ndocument work.",
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

    ax.text(tx, ty - 0.62, c["q"], fontsize=11.2, color=INK, va="top", linespacing=1.5,
            fontstyle="italic", family="DejaVu Sans")

    ax.text(tx, ty - 1.95, "WHAT DECIDES IT", fontsize=9, fontweight="bold", color=GRAY, family="DejaVu Sans")
    ax.text(tx, ty - 2.25, c["detail"], fontsize=10.0, color=INK, va="top", linespacing=1.45, family="DejaVu Sans")

    ax.plot([tx, x + card_w - 0.4], [y0 + 1.35, y0 + 1.35], color=BORDER, linewidth=1.0)
    ax.text(tx, y0 + 1.1, "THE CATCH", fontsize=9, fontweight="bold", color=c["accent"], family="DejaVu Sans")
    ax.text(tx, y0 + 0.8, c["verdict"], fontsize=10.4, color=INK, va="top", linespacing=1.5, family="DejaVu Sans")

ax.text(0.55, 0.15,
        "Sources: Schrems II and the US CLOUD Act; 32 CFR Part 2002 and ITAR; China's PIPL; Alpacked self-hosted LLM guide (Aug 2026); Fastino open-weight comparison (Jul 2026). Cost figures are practitioner estimates, not audited.",
        fontsize=8.7, color=GRAY, family="DejaVu Sans")

plt.tight_layout()
plt.savefig("/Users/lorelamarku/Desktop/AI Projects/AI-Researcher/assets/local-ai-gates.png",
            facecolor=BG, bbox_inches="tight")
print("saved")
