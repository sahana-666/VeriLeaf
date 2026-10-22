
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


def test_proof_for_a_different_record_fails():
    tree = MerkleTree(["a", "b", "c", "d"])
    assert not verify_proof("c", get_proof(tree, 0), tree.root)


def test_tampered_sibling_hash_fails():
    tree = MerkleTree(["a", "b", "c", "d"])
    proof = get_proof(tree, 1)

    original_hash = proof[0][0]
    bad_hash = bytes([original_hash[0] ^ 1]) + original_hash[1:]
    proof[0] = (bad_hash, proof[0][1])

    assert not verify_proof("b", proof, tree.root)
