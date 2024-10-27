# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        queue = [root]

        while queue:
            
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.right:
                  queue.append(node.right)
                if node.left:  
                  queue.append(node.left)

                if node.right and node.left:
                      tmp = node.left
                      node.left = node.right
                      node.right = tmp
                elif not node.right and node.left:
                      node.right = node.left
                      node.left = None
                else:
                    node.left = node.right
                    node.right = None
                

        return root