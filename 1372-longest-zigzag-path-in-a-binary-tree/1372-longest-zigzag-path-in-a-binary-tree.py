# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.path_length = 0
        def dfs_helper(node,length,direction_right=True):
            if  node:
                self.path_length = max(self.path_length, length)
            
                if  direction_right:
                    dfs_helper(node.left,length+1,False)
                    dfs_helper(node.right,1,True)
                else:
                    dfs_helper(node.right,length+1,True)
                    dfs_helper(node.left,1,False)
            
        dfs_helper(root,0,True)
        dfs_helper(root,0,False)

        return self.path_length



            



