# O(|E|+|V|) CX


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        vis = set()
        colors = [set(),set()]
        
        for i in range(n):
            if i not in vis :
                st = [(i,0)]
                while st :
                    node,col = st.pop()
                    vis.add(node)
                    colors[col].add(node)
                    
                    for nei in graph[node]:
                        if nei in colors[col]:
                            return 0
                        if nei not in vis :
                            st.append((nei, 1 if col == 0 else 0))
        return 1
        
