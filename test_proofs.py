
from merkle import MerkleTree
from proofs import get_proof, verify_proof


def test_valid_proof():
    records = ["Alice", "Bob", "Charlie", "David"]
    tree = MerkleTree(records)
    proof = get_proof(tree, 1)
    assert verify_proof("Bob", proof, tree.root)


def test_tampered_record():
    records = ["Alice", "Bob", "Charlie", "David"]
    tree = MerkleTree(records)
    proof = get_proof(tree, 1)
    assert not verify_proof("Eve", proof, tree.root)


def test_invalid_index():
    tree = MerkleTree(["Alice", "Bob"])
    try:
        get_proof(tree, 5)
        assert False, "Expected IndexError"
    except IndexError:
        pass
