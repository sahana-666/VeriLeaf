# VeriLeaf Benchmark Results

## Objective

Compare straightforward Merkle-tree operations with implementations that use
Merkle-tree structure to reduce work.

## What was measured

The benchmark uses datasets of 1,000, 10,000, and 100,000 records.

- **Verify one record:** rebuild the tree and compare its root versus verify a Merkle proof.
- **Update one record:** rebuild the tree after changing one record versus update a leaf and recalculate its path to the root.
- **Locate a tampered record:** compare leaf hashes versus use `find_changed` to locate the changed record.

## Results

The measured timings are stored in `results.csv` and visualized in `results.png`.
Timings can vary with hardware, operating system, Python version, and system load.

The benchmark compares operations with different amounts of work, so results
should be interpreted in the context of each operation. Tree construction is
outside the timed update operation.

## Implementation

- `datasets.py` generates sample records.
- `benchmark.py` runs the timing experiments and writes `results.csv`.
- `plot_results.py` generates the graph from the CSV data.
- `results.png` contains the generated benchmark visualization.

## Limitations

These measurements reflect one local environment. They do not, by themselves,
prove theoretical time complexity or guarantee the same performance on other
machines.

## Reproduction

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Generate benchmark results:

```bash
python benchmark.py
```

Generate the graph:

```bash
python plot_results.py
```

Run tests:

```bash
python -m pytest -v
```
