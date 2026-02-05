"""Validate a maze output file for consistent wall encoding.

This utility checks neighboring cells in the compact maze output
format to ensure that shared walls are encoded consistently.

Usage:
    python3 output_validator.py <output_file>
"""

import sys


def _load_grid(path: str):
    """Load the hexadecimal grid from the output file."""
    g = []
    with open(path, 'r') as fh:
        for line in fh:
            if line.strip() == '':
                break
            g.append([int(c, 16) for c in line.strip(' \t\n\r')])
    return g


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <output_file>")
        sys.exit(1)

    g = _load_grid(sys.argv[1])

    for r in range(len(g)):
        for c in range(len(g[0])):
            v = g[r][c]
            if not all([
                (r < 1 or v & 1 == (g[r-1][c] >> 2) & 1),
                (c >= len(g[0]) - 1 or (v >> 1) & 1 == (g[r][c+1] >> 3) & 1),
                (r >= len(g) - 1 or (v >> 2) & 1 == g[r+1][c] & 1),
                (c < 1 or (v >> 3) & 1 == (g[r][c-1] >> 1) & 1)
            ]):
                print(f'Wrong encoding for ({c},{r})')
