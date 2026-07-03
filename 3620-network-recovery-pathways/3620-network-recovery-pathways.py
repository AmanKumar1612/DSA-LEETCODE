from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        
        # If the start or end node is offline, no valid path can exist
        if not online[0] or not online[n - 1]:
            return -1
            
        # Collect all unique edge costs to define our binary search bounds
        all_costs = sorted(list(set(cost for _, _, cost in edges)))
        
        # Helper function to check if a valid path exists where every edge has cost >= mid
        def can_reach_with_min_cost(min_edge_threshold: int) -> bool:
            # Build the adjacency list filtering out offline nodes and edges below the threshold
            adj = [[] for _ in range(n)]
            in_degree = [0] * n
            
            for u, v, cost in edges:
                if online[u] and online[v] and cost >= min_edge_threshold:
                    adj[u].append((v, cost))
                    in_degree[v] += 1
            
            # DP array initialized to infinity representing the minimum cost to reach each node
            min_cost_to_node = [float('inf')] * n
            min_cost_to_node[0] = 0
            
            # Standard Kahn's algorithm for Topological Sort
            queue = deque([i for i in range(n) if in_degree[i] == 0])
            
            while queue:
                u = queue.popleft()
                current_cost = min_cost_to_node[u]
                
                for v, cost in adj[u]:
                    if current_cost + cost < min_cost_to_node[v]:
                        min_cost_to_node[v] = current_cost + cost
                    
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)
            
            return min_cost_to_node[n - 1] <= k

        # Binary search over the indices of the unique cost array
        low, high = 0, len(all_costs) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if can_reach_with_min_cost(all_costs[mid]):
                ans = all_costs[mid]  # Found a valid path, try to maximize the score
                low = mid + 1
            else:
                high = mid - 1
                
        return ans