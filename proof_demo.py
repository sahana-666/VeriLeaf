
"""Demonstrate how Merkle proofs verify records."""
from merkle import MerkleTree
from proofs import get_proof, verify_proof


def main():
    records = ["Alice", "Bob", "Charlie", "David"]
    tree = MerkleTree(records)

    # Prove that Bob belongs to this Merkle tree.
    proof = get_proof(tree, 1)
    print("Original record:", "Bob")
    print("Proof valid:", verify_proof("Bob", proof, tree.root))

    # Show that changing the record makes verification fail.
    print("Tampered record:", "Eve")
    print("Proof valid:", verify_proof("Eve", proof, tree.root))


if __name__ == "__main__":
    main()
