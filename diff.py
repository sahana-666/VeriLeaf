
"""Find records that differ between two Merkle trees."""


def find_changed(tree_a, tree_b):
    """Return indices of changed records, comparing their leaf hashes."""
    if len(tree_a) != len(tree_b):
        raise ValueError("trees must have the same number of records")

    return [
        i
        for i, (hash_a, hash_b) in enumerate(
            zip(tree_a.levels[0], tree_b.levels[0])
        )
        if hash_a != hash_b
    ]
