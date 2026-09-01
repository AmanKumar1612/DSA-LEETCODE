from collections import deque
from typing import List


class Solution:

  def minMoves(self, classroom: List[str], energy: int) -> int:
    m, n = len(classroom), len(classroom[0])

    # 1. Locate start 'S' and assign bit indices to each litter 'L'
    start = None
    litter_map = {}
    litter_count = 0

    for r in range(m):
      for c in range(n):
        cell = classroom[r][c]
        if cell == "S":
          start = (r, c)
        elif cell == "L":
          litter_map[(r, c)] = litter_count
          litter_count += 1

    # Edge case: No litter to collect
    if litter_count == 0:
      return 0

    target_mask = (1 << litter_count) - 1
    sr, sc = start

    # best_energy[r][c][mask] stores the maximum remaining energy seen so far
    # Initialize with -1
    best_energy = [
        [[-1] * (1 << litter_count) for _ in range(n)] for _ in range(m)
    ]
    best_energy[sr][sc][0] = energy

    # Queue stores tuples of: (row, col, mask, current_energy, moves)
    queue = deque([(sr, sc, 0, energy, 0)])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
      r, c, mask, e, moves = queue.popleft()

      # If we already found a path to this state with more energy, skip
      if e < best_energy[r][c][mask]:
        continue

      for dr, dc in directions:
        nr, nc = r + dr, c + dc

        # Check grid boundaries and obstacles
        if not (0 <= nr < m and 0 <= nc < n):
          continue
        cell = classroom[nr][nc]
        if cell == "X":
          continue

        # Moving takes 1 unit of energy
        ne = e - 1
        if ne < 0:
          continue

        nmask = mask

        # Update state based on cell type
        if cell == "R":
          ne = energy
        elif cell == "L":
          if (nr, nc) in litter_map:
            nmask |= 1 << litter_map[(nr, nc)]

        # Check if all litter items are collected
        if nmask == target_mask:
          return moves + 1

        # Pruning: Only proceed if this path offers strictly more energy for the same state
        if ne > best_energy[nr][nc][nmask]:
          best_energy[nr][nc][nmask] = ne
          queue.append((nr, nc, nmask, ne, moves + 1))

    return -1