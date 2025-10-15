"""Simple test runner to run the tests without pytest installed."""
import importlib
import traceback

from tests import test_count_missing_values as t

failures = 0
for name in dir(t):
    if name.startswith("test_"):
        fn = getattr(t, name)
        try:
            fn()
            print(f"OK: {name}")
        except AssertionError:
            failures += 1
            print(f"FAIL: {name}")
            traceback.print_exc()
        except Exception:
            failures += 1
            print(f"ERROR: {name}")
            traceback.print_exc()

if failures:
    raise SystemExit(1)
