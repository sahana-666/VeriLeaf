## Files

| File | Purpose |
|---|---|
| `merkle.py` | Build and manage the Merkle tree |
| `proofs.py` | Generate and verify Merkle proofs |
| `diff.py` | Compare trees and find changed records |
| `datasets.py` | Generate sample records |
| `benchmark.py`, `plot_results.py` | Benchmark performance and plot results |
| `demo.py`, `proof_demo.py` | Run command-line demonstrations |
| `index.html` | Visual dashboard |
| `test_*.py` | Unit tests |

## Run

Requires Python 3.8 or later.

```bash
python -m unittest -v
python demo.py
python proof_demo.py
python benchmark.py
python plot_results.py
```

Install dependencies using `pip install -r requirements.txt` if needed for the graph.

## Complexity

| Operation | Time Complexity |
|---|---|
| Build the tree | O(n) |
| Verify one record using a proof | O(log n) |
| Update one record | O(log n) |
| Locate k tampered records | O(k log n) |
| Append a record | O(n) |# VeriLeaf: Tamper-Evident Record Verification Using Merkle Trees

VeriLeaf detects tampering in digital records and pinpoints exactly which record was changed,
using a Merkle (hash) tree built in Python.
## Screenshots

![Sealed records](docs/screenshot-sealed.png)

![Tampered record](docs/screenshot-tampered.png)

## Team

| Member | Contribution |
|---|---|
| Replace with actual name | Core Merkle tree, repository setup, reviews |
| Replace with actual name | Proofs and finding changed records |
| Replace with actual name | Sample data, benchmark and graph |
| Replace with actual name | Dashboard, demo and documentation |

## Note on AI assistance

The initial code was AI-assisted. The team reviewed, tested and extended it, and each member can explain the part they worked on.