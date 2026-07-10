class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Pair each value with its original index and sort by value
        nodes = sorted((val, i) for i, val in enumerate(nums))
        
        # Map original index to its sorted position
        pos = {idx: i for i, (val, idx) in enumerate(nodes)}
        
        # Binary lifting table initialization
        # LOG = 18 is sufficient since N <= 10^5 (2^17 = 131072)
        LOG = 18
        up = [[-1] * LOG for _ in range(n)]
        
        # Build the greedy parent pointer for each node in the sorted array
        right = 0
        for left in range(n):
            while right < n and nodes[right][0] - nodes[left][0] <= maxDiff:
                right += 1
            # The furthest valid reachable node to the right
            parent_pos = right - 1
            if parent_pos > left:
                up[left][0] = parent_pos
            else:
                up[left][0] = -1
                
        # Populate the sparse table for binary lifting
        for j in range(1, LOG):
            for i in range(n):
                if up[i][j-1] != -1:
                    up[i][j] = up[up[i][j-1]][j-1]
                    
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            # Ensure we always jump from the smaller value to the larger value
            p1, p2 = pos[u], pos[v]
            if p1 > p2:
                p1, p2 = p2, p1
                
            # If the target is directly reachable in 1 jump
            if nodes[p2][0] - nodes[p1][0] <= maxDiff:
                ans.append(1)
                continue
                
            # Count the total minimum jumps needed using binary lifting
            jumps = 0
            curr = p1
            for j in range(LOG - 1, -1, -1):
                if up[curr][j] != -1 and nodes[up[curr][j]][0] < nodes[p2][0]:
                    curr = up[curr][j]
                    jumps += (1 << j)
            
            # Take one final jump to see if we can reach or overshoot p2 properly
            final_hop = up[curr][0]
            if final_hop != -1 and nodes[final_hop][0] >= nodes[p2][0] and nodes[final_hop][0] - nodes[curr][0] <= maxDiff:
                ans.append(jumps + 1)
            else:
                ans.append(-1)
                
        return ans