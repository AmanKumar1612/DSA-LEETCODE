class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        vis = [False] * n
        complete_components = 0
        
        for i in range(n):
            if not vis[i]:
                queue = [i]
                vis[i] = True
                
                component_nodes = []
                head = 0
                
                while head < len(queue):
                    curr = queue[head]
                    head += 1
                    component_nodes.append(curr)
                    
                    for neighbor in adj[curr]:
                        if not vis[neighbor]:
                            vis[neighbor] = True
                            queue.append(neighbor)
                
                num_nodes = len(component_nodes)
                is_complete = True
                
                for node in component_nodes:
                    if len(adj[node]) != num_nodes - 1:
                        is_complete = False
                        break
                        
                if is_complete:
                    complete_components += 1
                    
        return complete_components