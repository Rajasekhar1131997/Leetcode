# Leetcode Problem 1046: Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # looping until we process all the elements from the list or until it has only one element
        while len(stones) > 1:
            # sort the list in ascending order
            stones.sort()
            # pop the largest value from the list
            largest = stones.pop()
            # pop the second largest value from the list
            second_largest = stones.pop()

            # if the popped values are not equal, we delete the smallest weight and add difference weight to the list
            if largest != second_largest:
                stones.append(largest - second_largest)
        # finally, we return the single value from the list, else we return 0
        return stones[0] if stones else 0

print("Time Complexity: O(N^2 log N)")
print("Space Complexity: O(1)")

# Solving this problem using Heapq and Heapify
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # changing the all the values from positive to negative values
        for i in range(len(stones)):
            stones[i] = -stones[i]
        # sorting the list using heapify
        heapq.heapify(stones)
        # looping until the stones has 1 elements
        while len(stones) > 1:
            # popping off the largest value from the list/queue
            largest = heapq.heappop(stones)
            # popping off the second largest value from the list/queue
            second_largest = heapq.heappop(stones)

            # if the largest value is not equal to the second largest value, we difference the value and push that value to list/queue
            if largest != second_largest:
                heapq.heappush(stones, largest - second_largest)
        
        # if the length of the list/queue is 1, we return that value, else 0
        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0

print("Time Complexity: O(N log N)")
print("Space Complexity: O(1)")