
"""Generate sample records for demos and benchmarks."""


def generate_records(n, prefix="deed"):
    """Return n unique, readable records like 'deed-0', 'deed-1', ..."""
    if n < 0:
        raise ValueError("n must be non-negative")
    return [f"{prefix}-{i}" for i in range(n)]
