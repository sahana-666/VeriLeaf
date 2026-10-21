import unittest
from merkle import MerkleTree


def records(n):
    return [f"record-{i}" for i in range(n)]


class TestBuild(unittest.TestCase):
    def test_same_records_same_root(self):
        self.assertEqual(MerkleTree(records(8)).root, MerkleTree(records(8)).root)

    def test_changing_one_record_changes_root(self):
        changed = records(8)
        changed[3] = "forged"
        self.assertNotEqual(MerkleTree(records(8)).root, MerkleTree(changed).root)

    def test_order_matters(self):
        self.assertNotEqual(MerkleTree(["a", "b"]).root, MerkleTree(["b", "a"]).root)

    def test_odd_counts_build(self):
        for n in (1, 3, 5, 7, 13):
            self.assertEqual(len(MerkleTree(records(n))), n)

    def test_empty_rejected(self):
        with self.assertRaises(ValueError):
            MerkleTree([])