import itertools
from pathlib import Path

import matplotlib.pyplot as plt

# XKCD style
plt.xkcd()

# Specify the number of rows and columns
n_rows = 24
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

ax.add_patch(plt.Circle((3.5, 22.5), 0.1, color="black", fill=True))

ax.add_patch(plt.Circle((8.5, 2.5), 0.2, color="black", fill=True))
ax.text(11, 2, r"Now (2024)", fontsize=14, fontweight="bold")

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
