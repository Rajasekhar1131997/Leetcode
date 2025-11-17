# Leetcode Problem 1161: Maximum Level Sum of a Binary Tree
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # convert the given tree into a queue to perform BFS
        queue = deque([root])
        
        # track the maximum level sum found so far
        max_sum = float('-inf')
        
        # track which level holds that max sum
        max_level = 1
        
        # start from level 1 (root level)
        level = 1
        
        # loop until we process all nodes
        while queue:
            # initialize the sum for the current level
            level_sum = 0
            
            # number of nodes present in this level
            level_size = len(queue)
            
            # process all nodes in this level
            for i in range(level_size):
                # pop the current node
                node = queue.popleft()
                
                # add its value to the level sum
                level_sum += node.val

                # push left child into queue if it exists
                if node.left:
                    queue.append(node.left)
                
                # push right child into queue if it exists
                if node.right:
                    queue.append(node.right)
            
            # update max sum and level if current level sum is greater
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            
            # move to the next level
            level += 1
        
        # return the level number that had the maximum sum
        return max_level

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")