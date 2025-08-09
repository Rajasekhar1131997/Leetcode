# Leetcode problem 2465: Number of Distinct Averages
# https://leetcode.com/problems/number-of-distinct-averages/description/
# Solving this problem using queue
from typing import List
from collections import deque
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        seen = set()
        nums.sort()
        queue = deque(nums)
        while len(queue) >=2:
            min_value = queue.popleft()
            max_value = queue.pop()
            seen.add(min_value + max_value)
            
        return len(seen)
    
print("Time Complexity: O(N logN)")
print("Space Complexity: O(K)")

# We can also solve this problem using Two-Pointers Method
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        seen = set()
        left, right = 0, len(nums) - 1
        while left < right:
            min_value = nums[left]
            max_value = nums[right]
            seen.add(min_value + max_value)
            left += 1
            right -= 1
        return len(seen)

print("Time Complexity: O(N logN)")
print("Space Complexity: O(K)")