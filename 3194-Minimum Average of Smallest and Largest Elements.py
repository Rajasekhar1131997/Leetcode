# Leetcode Problem 3194: Minimum Average of Smallest and Largest Elements
# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/
from typing import List
from collections import deque
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        # initialize an empty list
        averages = []
        # sort the nums list in ascending order
        nums.sort()
        # convert the given nums list into queue
        queue = deque(nums)
        # loop until we process all the values from the queue
        while queue:
            # using popleft, we get the minimum value
            min_value = queue.popleft()
            # using pop, we get the maximum value
            max_value = queue.pop()
            # find the average of the min and max values
            average = (min_value + max_value) / 2
            # add that average to the averages list
            averages.append(average)
        # finally, return the min value from averages list
        return min(averages)

print("Time Complexity: O(N logN)")
print("Space Complexity: O(N)")

# instead of storing all the averages values in list, we can use running min average which takes O(1) space
from collections import deque
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        queue = deque(nums)
        min_average = float('inf')

        while queue:
            min_value = queue.popleft()
            max_value = queue.pop()
            average = (min_value + max_value) / 2
            min_average = min(min_average, average)

        return min_average

print("Time Complexity: O(N logN)")
print("Space Complexity: O(1)")