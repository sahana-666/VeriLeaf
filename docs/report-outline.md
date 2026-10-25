# VeriLeaf Report Outline

## 1. Problem

Digital records such as certificates can be changed without permission. Checking every record individually can take time. VeriLeaf uses a Merkle tree to detect changes and identify the records that were modified.

## 2. Data Structure

A Merkle tree is a tree in which leaf nodes contain hashes of records and parent nodes contain hashes calculated from their children. VeriLeaf uses SHA-256 to generate hashes. The final hash at the top is called the Merkle root.

## 3. How It Works

VeriLeaf builds a Merkle tree from the certificate records. A Merkle proof helps verify an individual record without rechecking every record. By comparing the original and modified trees, VeriLeaf can identify which records have been tampered with.

## 4. Complexity

Building the tree takes O(n) time for n records. Verifying one record using a Merkle proof takes O(log n) time. Updating one record takes O(log n) time, while appending a record takes O(n) time in this implementation.

## 5. Benchmark Results

Benchmarks were run for n = 1,000, 10,000, and 100,000 records across three tasks: verify one record, update one record, and locate a tampered record. In every case the naive approach (rebuilding the full tree) scaled roughly in proportion to n, reaching about 213 ms for verify and 218 ms for update at n = 100,000, while the tree-based operations stayed below 0.05 ms regardless of n. The locate task showed a similar gap: the naive leaf-scan took 10.75 ms at n = 100,000 while `find_changed` took 0.047 ms, a ratio of roughly 230×. These results confirm that the Merkle-tree operations achieve the expected O(log n) scaling in practice, compared with O(n) for the naive alternatives.

## 6. Demonstration

The command-line demo creates a trusted tree, verifies a certificate using a proof, and then changes one certificate name. The changed tree produces a different root, and the comparison identifies the modified record. Dashboard screenshots will show the original and tampered states.

## 7. Limitations

VeriLeaf identifies that records have changed and helps locate the changes, but it does not identify who made them. The original trusted Merkle root must be stored securely so that an attacker cannot replace both the records and the trusted root.

## 8. Real-World Applications

Merkle trees are useful in systems that need to verify data integrity. Examples include Git, Bitcoin, certificate transparency systems, and file synchronization. They help verify data efficiently using hashes and proofs.