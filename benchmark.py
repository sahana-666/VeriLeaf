
"""Benchmark Merkle operations against straightforward alternatives."""

import csv
import hashlib
import time

from datasets import generate_records
from diff import find_changed
from merkle import MerkleTree
from proofs import get_proof, verify_proof


def timeit(fn, reps=10):
    """Return the average runtime in milliseconds."""
    start = time.perf_counter()
    for _ in range(reps):
        fn()
    return (time.perf_counter() - start) / reps * 1000


def naive_verify(records, index, trusted_root):
    """Rebuild the Merkle tree from every record and compare roots."""
    return MerkleTree(records).root == trusted_root


def bench_verify(n):
    data = generate_records(n)
    tree = MerkleTree(data)
    index = n // 2
    proof = get_proof(tree, index)

    naive = timeit(lambda: naive_verify(data, index, tree.root), reps=3)
    fast = timeit(lambda: verify_proof(data[index], proof, tree.root))

    return naive, fast


def bench_update(n):
    data = generate_records(n)
    index = n // 2

    def rebuild():
        changed = list(data)
        changed[index] = "changed"
        return MerkleTree(changed).root

    def update_one():
        tree = MerkleTree(data)
        tree.update(index, "changed")
        return tree.root

    naive = timeit(rebuild, reps=3)
    fast = timeit(update_one, reps=3)

    return naive, fast


def bench_locate(n):
    data = generate_records(n)
    forged = list(data)
    forged[n // 3] = "forged"

    tree_a = MerkleTree(data)
    tree_b = MerkleTree(forged)

    def compare_leaves():
        return [
            i for i in range(n)
            if tree_a.levels[0][i] != tree_b.levels[0][i]
        ]

    naive = timeit(compare_leaves)
    fast = timeit(lambda: find_changed(tree_a, tree_b))

    return naive, fast


TASKS = [
    ("verify one record", bench_verify),
    ("update one record", bench_update),
    ("locate tampered record", bench_locate),
]


def main():
    rows = []

    for n in (1_000, 10_000, 100_000):
        for task, fn in TASKS:
            naive, fast = fn(n)
            rows.append((n, task, naive, fast))

    print(
        f"{'n':>8}  {'task':<24}"
        f"{'naive (ms)':>12}{'tree (ms)':>12}"
    )

    for n, task, naive, fast in rows:
        print(f"{n:>8}  {task:<24}{naive:>12.4f}{fast:>12.4f}")

    with open("results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "task", "naive_ms", "tree_ms"])
        writer.writerows(rows)

    print("\nSaved results.csv")


if __name__ == "__main__":
    main()
