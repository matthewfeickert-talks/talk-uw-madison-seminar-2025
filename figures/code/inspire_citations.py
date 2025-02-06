from pathlib import Path

import matplotlib.pyplot as plt

dates = [2020, 2021, 2022, 2023, 2024]
citations = [1, 15, 37, 47, 9]

fig, ax = plt.subplots()

ax.plot(dates[:-1], citations[:-1], marker="o", color="blue")
ax.plot(dates[-2:], citations[-2:], linestyle="dashed", marker="o", color="blue")

ax.text(
    2020.25,
    max(citations) - 5,
    f"Total: {sum(citations)}",
    fontsize=20,
    fontweight="bold",
)

ax.set_xlabel("Year", size=20)
ax.set_ylabel("Citations", size=20)

ax.set_xticks(dates)
ax.xaxis.set_tick_params(labelsize=20)
ax.yaxis.set_tick_params(labelsize=20)

figure_dir_path = Path(__file__).parents[1]
fig.savefig(
    figure_dir_path / "inspire-citations.png",
    transparent=True,
    bbox_inches="tight",
    dpi=300,
)
