
"""Read benchmark results and save a graph as results.png."""

import csv
from collections import defaultdict

import matplotlib.pyplot as plt

data = defaultdict(lambda: {"n": [], "naive": [], "tree": []})

with open("results.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        task = row["task"]
        data[task]["n"].append(int(row["n"]))
        data[task]["naive"].append(float(row["naive_ms"]))
        data[task]["tree"].append(float(row["tree_ms"]))

if not data:
    raise ValueError("results.csv contains no benchmark results.")

fig, axes = plt.subplots(
    1, len(data), figsize=(5 * len(data), 4), squeeze=False
)

for ax, (task, values) in zip(axes[0], data.items()):
    ax.plot(values["n"], values["naive"], "o-", label="Naive")
    ax.plot(values["n"], values["tree"], "o-", label="Merkle tree")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title(task)
    ax.set_xlabel("Number of records (n)")
    ax.set_ylabel("Time (ms)")
    ax.legend()
    ax.grid(True, alpha=0.3)

fig.tight_layout()
fig.savefig("results.png", dpi=150)
plt.close(fig)

print("Saved results.png")
