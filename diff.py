"""Find records that differ between two Merkle trees."""


def find_changed(tree_a, tree_b):
    """Return indices of changed records. Walks down from the root and skips every
    subtree whose hash matches, so it takes O(k log n) for k changed records."""
    if len(tree_a) != len(tree_b):
        raise ValueError("trees must have the same number of records")
    top = len(tree_a.levels) - 1
    stack, changed = [(top, 0)], []
    while stack:
        level, j = stack.pop()
        if tree_a.levels[level][j] == tree_b.levels[level][j]:
            continue
        if level == 0:
            changed.append(j)
            continue
        for child in (2 * j, 2 * j + 1):
            if child < len(tree_a.levels[level - 1]):
                stack.append((level - 1, child))
    return sorted(changed)
