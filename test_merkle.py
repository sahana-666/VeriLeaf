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
    

class TestUpdate(unittest.TestCase):
    def test_update_matches_rebuild(self):
        for n in (1, 2, 5, 8, 13):
            tree, changed = MerkleTree(records(n)), records(n)
            changed[n // 2] = "changed"
            tree.update(n // 2, "changed")
            self.assertEqual(tree.root, MerkleTree(changed).root)

    def test_bad_index_raises(self):
        tree = MerkleTree(records(3))
        for bad in (3, -1, 10):
            with self.assertRaises(IndexError):
                tree.update(bad, "x")


class TestAppend(unittest.TestCase):
    def test_append_matches_rebuild(self):
        tree = MerkleTree(records(5))
        tree.append("record-5")
        self.assertEqual(tree.root, MerkleTree(records(6)).root)


class TestPrintTree(unittest.TestCase):
    def test_print_tree_shows_root_and_leaves(self):
        import io
        import contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            MerkleTree(records(3)).print_tree()
        out = buf.getvalue()
        self.assertIn("root", out)
        self.assertIn("leaves", out)
        self.assertEqual(len(out.strip().splitlines()), 3)
