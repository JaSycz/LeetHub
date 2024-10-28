# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def dfs_min(node):
            while node.left:
                node = node.left
            return node.val


        def dfs(node,key):
            if node:
                if node.val == key:
                    if not node.left and not node.right:
                        return None
                    elif not node.left:
                        return node.right
                    elif not node.right:
                        return node.left
                    else:
                        
                        node.val = dfs_min(node.right)
                        node.right = dfs(node.right,node.val)


                elif node.val > key:
                    node.left = dfs(node.left,key)
                else:
                    node.right = dfs(node.right,key)


                return node

                
                
            

        


        

        return dfs(root,key)
            
