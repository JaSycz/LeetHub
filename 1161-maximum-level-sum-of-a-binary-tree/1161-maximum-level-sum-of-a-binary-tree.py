# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue =  [root]
        max_sum,level,ans = float(-inf),0,0
        
        while queue:
            level+=1
            sum_at_level=0

            for _ in range(len(queue)):
              node = queue.pop(0)

              sum_at_level += node.val
              if node.left:
                queue.append(node.left)
              if node.right:
                queue.append(node.right)
                
            if sum_at_level > max_sum:
                max_sum = sum_at_level
                ans = level
        
        
        return ans


