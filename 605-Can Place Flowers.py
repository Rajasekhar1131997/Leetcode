# Leetcode Problem 605: Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/description/
from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # iterate over each plot in the flowerbed
        for i in range(len(flowerbed)):
            # if there's already a flower, skip
            if flowerbed[i] == 1:
                continue
            # if it's empty, check neighbors
            elif flowerbed[i] == 0:
                # left is free if we're at the first plot OR left neighbor is 0
                left = (i == 0) or (flowerbed[i-1] == 0)
                # right is free if we're at the last plot OR right neighbor is 0
                right = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)

                # if both sides are free, we can plant a flower
                if left and right:
                    flowerbed[i] = 1   # mark as planted
                    n -= 1             # reduce flowers left to plant
        # valid if we managed to plant all n flowers
        return n <= 0

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")