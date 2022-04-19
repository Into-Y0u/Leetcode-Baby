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
