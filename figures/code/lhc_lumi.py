import itertools
from pathlib import Path

import matplotlib.pyplot as plt

# XKCD style
# Vary parameters to avoid sharp edges and clipping
# Thanks to Thomas Caswell for the suggestion
# plt.xkcd(scale=0.2)
# plt.xkcd(scale=0.2, length=200)
plt.xkcd(length=500)

# Total integrated Luminosity marks
# Run 1: 30 fb^-1 (Run: 30 fb^-1)
# Run 2: 190 fb^-1 (160 fb^-1) ~ 5 squares
# Run 3: 500 fb^-1 (310 fb^-1) ~ 10 squares
# Run 4: 4000 fb^-1 (3500 fb^-1) ~117 squares
# https://atlas.web.cern.ch/Atlas/GROUPS/DATAPREPARATION/PublicPlots/2024/DataSummary/figs/intlumivstimeRun3.png
# Total collected in Run 3 so far: 183 fb^-1

# Specify the number of rows and columns
# would get 3600 fb^-1
# n_rows = 24
# n_cols = 5

# would get 3960 fb^-1
# n_rows = 22
# n_cols = 6

# would get 4050 fb^-1, but choosing to have n_cols be 5
# for aesthetic reasons of being able to easily calculate
# in numbers of 10 per 2 rows.
n_rows = 27
n_cols = 5

fig, ax = plt.subplots()
ax.axis("off")

# Set the aspect ratio to be equal, so squares look like squares
ax.set_aspect("equal", adjustable="box")

# Plot the grid of squares
run_one_color = "red"
run_two_color = "orange"
run_three_color = "gold"
run_four_color = "grey"

# Fix to be index based
for row, col in itertools.product(range(n_rows), range(n_cols)):
    if row == 0 and col == 0:
        facecolor = run_one_color
    elif row == 0 and col > 0:
        facecolor = run_two_color
    elif row == 1 and col == 0:
        facecolor = run_two_color
    elif row == 1 and col > 0:
        facecolor = run_three_color
    elif row == 2:
        facecolor = run_three_color
    elif row == 3 and col == 0:
        facecolor = run_three_color
    else:
        facecolor = run_four_color
    square = plt.Rectangle(
        (col, n_rows - row - 1),
        1,
        1,
        fill=True,
        facecolor=facecolor,
        edgecolor="black",
    )
    ax.add_patch(square)

ax.add_patch(
    plt.Rectangle(
        (7, 18),
        3,
        3,
        fill=True,
        facecolor=run_one_color,
        linewidth=2,
    )
)
ax.text(11, 19, "Run 1 (Higgs)", fontsize=14, fontweight="bold")

ax.add_patch(
    plt.Rectangle(
        (7, 14),
        3,
        3,
        fill=True,
        facecolor=run_two_color,
        linewidth=2,
    )
)
ax.text(11, 15, "Run 2", fontsize=14, fontweight="bold")

ax.add_patch(
    plt.Rectangle(
        (7, 10),
        3,
        3,
        fill=True,
        facecolor=run_three_color,
        linewidth=2,
    )
)
ax.text(11, 11, "Run 3", fontsize=14, fontweight="bold")

ax.add_patch(
    plt.Rectangle(
        (7, 6),
        3,
        3,
        fill=True,
        facecolor=run_four_color,
        linewidth=2,
    )
)
ax.text(11, 7, "Run 4+", fontsize=14, fontweight="bold")

ax.add_patch(
    plt.Rectangle(
        (8, 4),
        1,
        1,
        fill=True,
        facecolor=run_four_color,
        edgecolor="black",
    )
)
# ax.text(11, 4, r"~ $30 \mathrm{fb}^{-1}$", fontsize=14, fontweight="bold")
ax.text(11, 4, r"$\sim 30\,\mathrm{fb}^{-1}$", fontsize=14, fontweight="bold")

ax.add_patch(plt.Circle((1.4, 24.6), 0.1, color="black", fill=True))

ax.add_patch(plt.Circle((8.5, 2.5), 0.2, color="black", fill=True))
ax.text(11, 2, r"Now (2025)", fontsize=14, fontweight="bold")

# Set the limits of the plot
# ax.set_xlim(0, n_cols)
ax.set_xlim(0, 20)
ax.set_ylim(0, n_rows)

# Remove axis labels and ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])

figure_dir_path = Path(__file__).parents[1]
fig.savefig(
    figure_dir_path / "lhc_lumi.png", transparent=True, bbox_inches="tight", dpi=300
)
