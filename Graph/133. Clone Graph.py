"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node : return None
        old2new = {}
        def helper(node):
            if node in old2new :
                return old2new[node]
            
            copy = Node(node.val)
            old2new[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(helper(nei))
            
            return copy
        return helper(node) 
        
