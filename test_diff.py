
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
