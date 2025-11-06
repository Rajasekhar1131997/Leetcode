# Leetcode Problem 3285: Find Indices of Stable Mountains
# https://leetcode.com/problems/find-indices-of-stable-mountains/description/
class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        # initialize an empty result list
        result = []
        # loop through the given list starting from index 1
        for i in range(1, len(height)):
            # check if the previous element is strictly greater than threshold
            if height[i-1] > threshold:
                # if yes, we append the index to the result list
                result.append(i)
        # return the result list
        return result

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")