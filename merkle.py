"""
Leaves hold hashes of records; every internal node holds the hash of its two children.
Leaves are hashed with a 0x00 prefix and nodes with 0x01, so a leaf can never be passed
off as an internal node. An unpaired node at the end of a level is promoted unchanged,
so no record is ever duplicated.
"""
import hashlib
import json


def hash_leaf(record) -> bytes:
    data = record if isinstance(record, bytes) else str(record).encode()
    return hashlib.sha256(b"\x00" + data).digest()


def hash_node(left: bytes, right: bytes) -> bytes:
    return hashlib.sha256(b"\x01" + left + right).digest()


class MerkleTree:
    def __init__(self, records):
        if not records:
            raise ValueError("need at least one record")
        self.levels = [[hash_leaf(r) for r in records]]
        self._build_upper()

    def _build_upper(self):
        del self.levels[1:]
        while len(self.levels[-1]) > 1:
            cur = self.levels[-1]
            self.levels.append([
                hash_node(cur[i], cur[i + 1]) if i + 1 < len(cur) else cur[i]
                for i in range(0, len(cur), 2)
            ])

    @property
    def root(self) -> bytes:
        return self.levels[-1][0]

    def __len__(self):
        return len(self.levels[0])
    
    def update(self, index: int, record) -> None:
        """Replace one record and refresh only its path to the root: O(log n)."""
        self._check_index(index)
        self.levels[0][index] = hash_leaf(record)
        for k in range(1, len(self.levels)):
            index //= 2
            below = self.levels[k - 1]
            left = 2 * index
            self.levels[k][index] = (
                hash_node(below[left], below[left + 1])
                if left + 1 < len(below) else below[left]
            )

    def _check_index(self, index: int) -> None:
        if not 0 <= index < len(self):
            raise IndexError(f"record index {index} out of range (0 to {len(self) - 1})")

    
    def append(self, record) -> None:
        """Add a record at the end (rebuilds the upper levels: O(n))."""
        self.levels[0].append(hash_leaf(record))
        self._build_upper()
    
    def print_tree(self) -> None:
        """Print the tree from the root down, with hashes shortened to 6 characters."""
        top = len(self.levels) - 1
        for k in range(top, -1, -1):
            label = "root" if k == top else ("leaves" if k == 0 else f"level {k}")
            print(f"{label:>8}: " + " ".join(h.hex()[:6] for h in self.levels[k]))
    
    @classmethod
    def from_leaf_hashes(cls, hashes):
        """Rebuild a tree from stored leaf hashes (no original records needed)."""
        if not hashes:
            raise ValueError("need at least one leaf hash")
        tree = cls.__new__(cls)
        tree.levels = [list(hashes)]
        tree._build_upper()
        return tree

    def save(self, path: str) -> None:
        with open(path, "w") as f:
            json.dump({"leaves": [h.hex() for h in self.levels[0]], "root": self.root.hex()}, f)

    @classmethod
    def load(cls, path: str) -> "MerkleTree":
        with open(path) as f:
            data = json.load(f)
        tree = cls.from_leaf_hashes([bytes.fromhex(h) for h in data["leaves"]])
        if tree.root.hex() != data["root"]:
            raise ValueError("file is corrupted or has been tampered with")
        return tree