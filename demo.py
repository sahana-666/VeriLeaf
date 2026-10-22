
"""CLI walkthrough: seal certificates, prove one, then catch tampering.
Run: python demo.py
"""

from diff import find_changed
from merkle import MerkleTree
from proofs import get_proof, verify_proof

certificates = [
    "Cert 101 - Asha",
    "Cert 102 - Ravi",
    "Cert 103 - Meera",
    "Cert 104 - John",
    "Cert 105 - Priya",
    "Cert 106 - Arun",
    "Cert 107 - Divya",
    "Cert 108 - Karan"
]

sealed = MerkleTree(certificates)

print("Trusted root:", sealed.root.hex()[:16], "...")

proof = get_proof(sealed, 2)

print(
    f"\nProof for '{certificates[2]}' needs only "
    f"{len(proof)} hashes (of {len(certificates)} records):",
    verify_proof(certificates[2], proof, sealed.root)
)
