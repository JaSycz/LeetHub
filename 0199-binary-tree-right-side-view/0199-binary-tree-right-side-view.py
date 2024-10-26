# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        current_node = root
        visited = []
        while current_node:
            visited.append(current_node.val)
            if  current_node.right:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return visited
            
                
