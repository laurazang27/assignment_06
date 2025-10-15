# data_analysis

This directory contains simple demo utilities for data analysis.

Files
- `analysis.py` — Python script with a validated `factorial(n)` function and a small CLI example.
- `calculate_factorial.R` — R equivalent of the recursive factorial function.

Usage

Run the Python example from the repository root or from this directory:

```bash
python3 data_analysis/analysis.py
```

Or in R:

```r
source("data_analysis/calculate_factorial.R")
print(calculate_factorial(5))
```

Notes
- `analysis.py` includes input validation and is safe for demonstration; for production code prefer an iterative implementation for large `n` or use math libraries.
