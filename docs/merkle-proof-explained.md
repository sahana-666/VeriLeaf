
# Merkle Proofs Explained

## What is a Merkle Proof?

A Merkle proof shows that a particular record belongs to a Merkle tree without needing to reveal every record in the tree.

It uses the record's hash and the hashes of its sibling nodes to reconstruct the Merkle root.

## How Does It Work?

1. The record is converted into a hash using `hash_leaf()`.
2. The proof contains the sibling hash at each level of the tree.
3. Each sibling is marked as either `"L"` (left) or `"R"` (right).
4. Starting from the record's hash, `verify_proof()` combines the hashes in the correct order using `hash_node()`.
5. The reconstructed hash is compared with the trusted Merkle root.

If the hashes match, verification returns `True`. Otherwise, it returns `False`.

## Example

Suppose a Merkle tree contains these records:

- Alice
- Bob
- Charlie
- David

We generate a proof for Bob using `get_proof(tree, 1)`.

The proof allows us to verify Bob's membership using the sibling hashes and the Merkle root, without needing to provide the original records Alice, Charlie, and David.

If Bob is changed to Eve while keeping the original proof and root, verification fails.

## Why Are Merkle Proofs Useful?

- They verify records without sharing the entire dataset.
- They help detect modified or forged records.
- They are useful in systems that need efficient integrity verification.

## Time Complexity

For a balanced Merkle tree with `n` records, a proof contains approximately `O(log n)` sibling hashes, and verification takes `O(log n)` hash operations.
