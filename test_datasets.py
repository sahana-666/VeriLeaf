
import unittest
from datasets import generate_records


class TestDatasets(unittest.TestCase):
    def test_count(self):
        self.assertEqual(len(generate_records(50)), 50)

    def test_records_are_unique(self):
        self.assertEqual(len(set(generate_records(1000))), 1000)

    def test_prefix(self):
        self.assertEqual(
            generate_records(2, prefix="cert"),
            ["cert-0", "cert-1"]
        )

    def test_zero_records(self):
        self.assertEqual(generate_records(0), [])

    def test_negative_count_rejected(self):
        with self.assertRaises(ValueError):
            generate_records(-1)


if __name__ == "__main__":
    unittest.main()
