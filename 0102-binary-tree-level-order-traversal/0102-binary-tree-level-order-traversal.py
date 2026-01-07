# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            visited=[root]
        else:
            visited=[]

        ans=[]
        h=1
        count=0
        lst=[]
        while visited:
            node=visited[0]
            visited.pop(0)

            if node:
              visited.append(node.left)
              visited.append(node.right)
              lst.append(node.val)
            count+=1
            
            if count==2**(h-1):
                if lst:
                  ans.append(lst)
                lst=[]
                h+=1
                count=0

        return ans