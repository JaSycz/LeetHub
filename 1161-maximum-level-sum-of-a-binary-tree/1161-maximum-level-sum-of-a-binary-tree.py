# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = {1: [root]}
        level_map = {}
        level = 1
        sum = 0
        while queue:
            current_node = queue[level].pop(-1)
            if current_node:
                sum += current_node.val
                if level+1 not in queue.keys():
                    if current_node.left and current_node.right:
                      queue[level+1]=[current_node.left,current_node.right]
                    elif current_node.left:
                        queue[level+1]=[current_node.left]
                    elif current_node.right:
                        queue[level+1]=[current_node.right]
                else:
                  if current_node.left:
                    queue[level+1].append(current_node.left)
                  if current_node.right:
                    queue[level+1].append(current_node.right)
            
            
            if  queue[level] == []:
                del queue[level]
                level_map[level]= sum
                sum = 0
                level+=1
                
        print(level_map)
        max = float(-inf)
        max_key = 0
        for key in level_map.keys():
            if level_map[key] > max:
                max = level_map[key]
                max_key = key
                

        return max_key


