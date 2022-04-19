# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(root,targetSum,path):
            if not root :
                return 
            if root.left is None and root.right is None and targetSum - root.val == 0 :
                res.append(path + [root.val])
            dfs(root.left,targetSum - root.val , path + [root.val])
            dfs(root.right,targetSum - root.val , path + [root.val])
        dfs(root,targetSum,[])
        return res
        

        
#java Solve
class Solution {
    List<List<Integer>> paths = new ArrayList<>();
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        if(root == null)
            return paths;
        dfs(root, targetSum, new ArrayList<>());
        return paths;
    }

    void dfs(TreeNode node, int targetSum, ArrayList<Integer> path) {
        if(node == null)
            return;
            path.add(node.val);
            targetSum -= node.val;
        
        if(targetSum == 0 && node.left == null && node.right == null)
            paths.add(path);
        
        dfs(node.left, targetSum, new ArrayList<>(path));
        dfs(node.right, targetSum, new ArrayList<>(path));
    }
}
