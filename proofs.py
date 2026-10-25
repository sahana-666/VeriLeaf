"""Merkle proofs: prove one record belongs to a tree without revealing the others."""
from merkle import hash_leaf, hash_node


def get_proof(tree, index):
    """Sibling hashes from leaf to root, as (hash, side) pairs: O(log n) items."""
    if not 0 <= index < len(tree):
        raise IndexError(f"record index {index} out of range")
    proof = []
    for level in tree.levels[:-1]:
        sibling = index ^ 1
        if sibling < len(level):
            proof.append((level[sibling], "L" if sibling < index else "R"))
        index //= 2
    return proof

def verify_proof(record, proof, root):
    """Return True if the record and proof produce the expected Merkle root."""
    current = hash_leaf(record)

    for sibling_hash, side in proof:
        if side == "L":
            current = hash_node(sibling_hash, current)
        elif side == "R":
            current = hash_node(current, sibling_hash)
        else:
            return False

    return current == root
