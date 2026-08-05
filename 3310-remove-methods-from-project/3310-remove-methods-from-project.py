from collections import defaultdict, deque
from typing import List


class Solution:

  def remainingMethods(
      self, n: int, k: int, invocations: List[List[int]]
  ) -> List[int]:
    graph = defaultdict(list)
    in_degree = [0] * n

    # Build adjacency list and calculate in-degrees
    for u, v in invocations:
      graph[u].append(v)
      in_degree[v] += 1

    suspicious = {k}
    queue = deque([k])

    # Traverse suspicious component and decrement incoming edge count
    while queue:
      curr = queue.popleft()
      for neighbor in graph[curr]:
        in_degree[neighbor] -= 1  # Remove edge from a suspicious method
        if neighbor not in suspicious:
          suspicious.add(neighbor)
          queue.append(neighbor)

    # If any suspicious method still has in_degree > 0,
    # it means a non-suspicious method invokes it.
    for node in suspicious:
      if in_degree[node] > 0:
        return list(range(n))

    # Otherwise, return all non-suspicious methods
    return [i for i in range(n) if i not in suspicious]