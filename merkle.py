"""
Leaves hold hashes of records; every internal node holds the hash of its two children.
Leaves are hashed with a 0x00 prefix and nodes with 0x01, so a leaf can never be passed
off as an internal node. An unpaired node at the end of a level is promoted unchanged,
so no record is ever duplicated.
"""
import hashlib


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