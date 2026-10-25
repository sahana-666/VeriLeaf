# VeriLeaf Benchmark Results



## 1. Objective



The objective of this benchmark is to compare naive verification, which rebuilds the Merkle tree, with Merkle proof verification. The benchmark measures execution time for different dataset sizes.



## 2. Implementation



- `datasets.py` generates sample records.

- `benchmark.py` measures verification runtimes.

- `results.csv` stores the measured results.

- `plot_results.py` generates a graph from the CSV data.

- `results.png` contains the generated benchmark visualization.



## 3. Methodology



The benchmark uses datasets of different sizes and measures average execution time over repeated runs. The timings are recorded in milliseconds.



## 4. Results



The actual measurements are available in `results.csv` and visualized in `results.png`.



The results should be interpreted based on the measured timings. Runtime can vary with hardware, Python version, and implementation details.



## 5. Limitations



The measurements reflect the local test environment and do not establish theoretical time complexity by themselves. The benchmark compares rebuilding a tree with verifying a proof, so the two operations have different workloads.



## 6. Reproduction



Install dependencies:



`python -m pip install -r requirements.txt`



Generate benchmark results:



`python benchmark.py`



Generate the graph:



`python plot_results.py`



Run tests:



`python -m pytest -v`



