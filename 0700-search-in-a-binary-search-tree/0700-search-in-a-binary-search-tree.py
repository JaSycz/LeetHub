# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node,val):
            if node: 
              if node.val == val:
                return node
              
              search = dfs(node.left,val)
              if search:
                return search
              else:
                return dfs(node.right,val)
              
            return None
            

        return dfs(root , val)