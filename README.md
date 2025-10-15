Assignment 06

Author: Laura Zang

Date: 2024-06-10

## Overview

This repository contains code and small utilities for Assignment 06. The focus is on basic data analysis demonstrations in both Python and R. The examples are intentionally small and educational:

- data cleaning and normalization helpers
- counting/missing-value utilities
- small language examples (Python + R)

## Repository structure

- `data_analysis/` — examples and utilities
	- `analysis.py` — Python factorial example
	- `calculate_factorial.R` — R factorial example
	- `count_vowels.py` / `count_vowels.R` — vowel-count utilities and examples
	- `count_missing_values.py` — missing-value counters (pandas + pure-Python fallback)
	- `normalize_data.py` — min-max normalization helper
- `tests/` — simple unit tests
- `run_tests.py` — small test runner for environments without pytest

## Usage

Run example Python scripts with:

```bash
python3 data_analysis/analysis.py
python3 data_analysis/count_vowels.py
```

Run R examples from an R session:

```r
source("data_analysis/calculate_factorial.R")
source("data_analysis/count_vowels.R")
# then call functions, e.g. count_vowels("Résumé")
```

## Testing

If you have pytest installed you can run:

```bash
pytest -q
```

Or use the included minimal runner:

```bash
python3 run_tests.py
```

## Notes

- Some scripts include fallbacks when optional dependencies (pandas, stringi) are not available.
- These utilities are educational; for production or large datasets prefer vectorized/optimized libraries.

## Contributing

PRs and issues are welcome. Suggestions: add more tests, improve type hints, and package examples if desired.