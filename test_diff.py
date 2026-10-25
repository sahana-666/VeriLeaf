
import random

import pytest
from merkle import MerkleTree
from diff import find_changed


def test_no_records_changed():
    a = MerkleTree(["Alice", "Bob", "Charlie"])
    b = MerkleTree(["Alice", "Bob", "Charlie"])
    assert find_changed(a, b) == []


def test_one_record_changed():
    a = MerkleTree(["Alice", "Bob", "Charlie"])
    b = MerkleTree(["Alice", "Eve", "Charlie"])
    assert find_changed(a, b) == [1]


def test_multiple_records_changed():
    a = MerkleTree(["Alice", "Bob", "Charlie", "David"])
    b = MerkleTree(["Eve", "Bob", "Frank", "David"])
    assert find_changed(a, b) == [0, 2]


def test_different_tree_sizes():
    a = MerkleTree(["Alice", "Bob"])
    b = MerkleTree(["Alice", "Bob", "Charlie"])
    with pytest.raises(ValueError):
        find_changed(a, b)


def test_odd_sizes_and_edges():
    for n in (1, 2, 3, 5, 7, 13, 21):
        base = [f"r{i}" for i in range(n)]
        changed = list(base)
        changed[0] = "x"
        changed[n - 1] = "y"
        expected = sorted({0, n - 1})
        assert find_changed(MerkleTree(base), MerkleTree(changed)) == expected


def test_matches_naive_comparison_on_random_changes():
    random.seed(1)
    for _ in range(50):
        n = random.randint(1, 60)
        base = [f"r{i}" for i in range(n)]
        changed = list(base)
        for i in random.sample(range(n), random.randint(0, n)):
            changed[i] = f"edited-{i}"
        a, b = MerkleTree(base), MerkleTree(changed)
        naive = [i for i in range(n) if a.levels[0][i] != b.levels[0][i]]
        assert find_changed(a, b) == naive
