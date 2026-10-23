\# VeriLeaf Benchmark Results



\## Objective



This benchmark compares a naive verification approach with Merkle-tree-based verification and measures the performance of selected VeriLeaf operations as the number of records increases.



\## Methodology



\- Generate sample records using `datasets.py`.

\- Measure operation runtimes using `benchmark.py`.

\- Save the measurements in `results.csv`.

\- Visualize the results using `plot\_results.py`.



\## Results



The benchmark measurements are recorded in `results.csv`, and the corresponding graph is saved as `results.png`.



Actual performance conclusions should be added after reviewing the measured results. Runtime can vary with hardware, Python version, and dataset size.



\## Limitations



The measurements are specific to the test environment. Benchmark timings alone do not establish theoretical time complexity, and comparisons should use equivalent inputs and clearly defined operations.



\## Reproducibility



Install dependencies with:



```powershell

python -m pip install -r requirements.txt

```



Run the benchmark and graph-generation scripts from the project root. Ensure the project dependencies and expected CSV column names match the scripts.



