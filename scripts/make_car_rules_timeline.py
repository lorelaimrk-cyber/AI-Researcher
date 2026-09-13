"""Road deaths in Great Britain, 1926 to 2024, with the rule layers marked.

Source: Department for Transport, table RAS0101 (reported road collisions, casualties and
vehicles involved, Great Britain, from 1926), killed column. Rule dates from GOV.UK's history of
road safety and the driving test, and the UN road traffic conventions of 1949 and 1968.
"""
import re
import zipfile
import urllib.request
import os

import matplotlib.pyplot as plt

BG = "#F2EFE7"
INK = "#1F2A24"
GRAY = "#6B6F66"
GREEN = "#2F6B47"
GREEN_DARK = "#1F4E33"
RED = "#B23A2E"
STONE = "#8C8272"
BORDER = "#D9D4C6"

ODS_URL = "https://assets.publishing.service.gov.uk/media/6a6398df9a419980593b2bdf/ras0101.ods"
CACHE = os.path.join(os.path.dirname(__file__), "..", "sources", "ras0101.ods")


def load_deaths():
    if not os.path.exists(CACHE):
        urllib.request.urlretrieve(ODS_URL, CACHE)
    x = zipfile.ZipFile(CACHE).read("content.xml").decode()
    rows = re.findall(r"<table:table-row[^>]*>(.*?)</table:table-row>", x, flags=re.S)
    deaths = {}
    for r in rows:
        cells = re.findall(r"<table:table-cell([^>]*)>(.*?)</table:table-cell>|<table:table-cell([^>]*)/>", r, flags=re.S)
        vals = []
        for a, body, b in cells:
            attrs = a or b
            rep = re.search(r'number-columns-repeated="(\d+)"', attrs)
            n = int(rep.group(1)) if rep else 1
            t = re.sub("<[^>]+>", "", body or "").strip()
            vals.extend([t] * min(n, 3))
        # the casualties table: year, pedestrians, pedal cyclists, motorcyclists, car, other, killed, all
        if len(vals) >= 8 and re.fullmatch(r"\d{4}", vals[0]) and vals[6].replace(",", "").isdigit() and vals[7].replace(",", "").endswith("000") or (
            len(vals) >= 8 and re.fullmatch(r"\d{4}", vals[0]) and vals[6].replace(",", "").isdigit() and vals[8:9] == [vals[0]]):
            deaths[int(vals[0])] = int(vals[6].replace(",", ""))
    return deaths


deaths = load_deaths()
years = sorted(y for y in deaths if 1926 <= y <= 2024)
vals = [deaths[y] for y in years]
assert deaths[1934] == 7343 and deaths[1966] == 7985 and deaths[2024] == 1602, deaths

fig, ax = plt.subplots(figsize=(14.4, 6.8), dpi=150)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
for s in ax.spines.values():
    s.set_visible(False)

ax.fill_between(years, vals, color=GREEN, alpha=0.12, zorder=1)
ax.plot(years, vals, color=GREEN_DARK, linewidth=2.2, zorder=3)

ax.set_xlim(1900, 2026)
ax.set_ylim(0, 10400)
ax.set_yticks([0, 2000, 4000, 6000, 8000, 10000])
ax.set_yticklabels(["0", "2,000", "4,000", "6,000", "8,000", "10,000"], color=GRAY, fontsize=10, family="DejaVu Sans")
ax.set_xticks([1903, 1920, 1940, 1960, 1980, 2000, 2024])
ax.set_xticklabels(["1903", "1920", "1940", "1960", "1980", "2000", "2024"], color=GRAY, fontsize=10, family="DejaVu Sans")
ax.tick_params(length=0)
ax.grid(axis="y", color=BORDER, linewidth=0.9, zorder=0)

ax.text(1900, 10250, "Nobody banned the car", fontsize=24, fontweight="bold", color=INK, family="DejaVu Sans", va="top")
ax.text(1900, 9450, "Road deaths in Great Britain each year, 1926 to 2024, and the rules that arrived on the driver, the plate and the border.",
        fontsize=12, color=GRAY, family="DejaVu Sans", va="top")

rules = [
    (1903, "1903", "Licence, no test.\nA number on every car.", 5600, RED),
    (1909, "1909", "Paris, 16 countries: an exam\nand a plate buy the right\nto drive abroad.", 3300, STONE),
    (1935, "1935", "Compulsory driving test.\n63 percent pass.", 8900, RED),
    (1949, "1949", "Geneva: a licence from one\ncountry counts in another.", 3200, STONE),
    (1967, "1967", "Breathalyser.", 9250, RED),
    (1968, "1968", "Vienna: theory and practical\nexams, same signs everywhere.", 2100, STONE),
]
for x, title, body, y_text, color in rules:
    ax.plot([x, x], [0, y_text - 150], color=color, linewidth=1.2, linestyle=(0, (4, 3)), zorder=2)
    ax.text(x + 0.8, y_text, title, fontsize=12.5, fontweight="bold", color=color, family="DejaVu Sans", va="top")
    ax.text(x + 0.8, y_text - 420, body, fontsize=9.6, color=INK, family="DejaVu Sans", va="top", linespacing=1.45)

for yr, label, dy in [(1934, "7,343", 300), (1966, "7,985", 300), (2024, "1,602", 350)]:
    ax.plot(yr, deaths[yr], marker="o", markersize=7, color=GREEN_DARK, markeredgecolor=BG, markeredgewidth=1.5, zorder=4)
    ax.text(yr + (0.8 if yr != 2024 else -0.8), deaths[yr] + dy, label, fontsize=10.5, fontweight="bold", color=GREEN_DARK,
            family="DejaVu Sans", ha="left" if yr != 2024 else "right")

ax.text(1948, 6400, "Vehicles on the road:\n2.3 million in 1931,\n41.7 million in 2024.", fontsize=10, color=INK, family="DejaVu Sans",
        va="top", linespacing=1.45, bbox=dict(boxstyle="round,pad=0.5", facecolor=BG, edgecolor=BORDER))

ax.text(1900, -1500,
        "Deaths: Department for Transport, RAS0101 (Great Britain). Vehicles: GOV.UK history of the driving test (1931) and DfT vehicle licensing "
        "statistics 2024 (UK).\nRule dates: Motor Car Act 1903, Road Traffic Act 1934, GOV.UK; Paris (1909), Geneva (1949) and Vienna (1968) Conventions on Road Traffic. "
        "The 1939 to 1941 rise is the wartime years.",
        fontsize=8.6, color=GRAY, family="DejaVu Sans", va="top", linespacing=1.4)

plt.tight_layout()
out = os.path.join(os.path.dirname(__file__), "..", "assets", "car-rules-timeline.png")
plt.savefig(out, facecolor=BG, bbox_inches="tight")
print("saved", out, "years:", len(years))
