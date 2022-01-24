# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, cur , arr) :
            if not node : return 
            elif node.left == None and node.right == None and  cur+ node.val  == targetSum:
                res.append(arr + [node.val])
            dfs(node.left , cur+ node.val , arr + [node.val])
            dfs(node.right , cur+ node.val , arr + [node.val])
            return res
            
        return dfs(root,0,[])
        
