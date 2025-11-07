# Leetcode Problem 1470: Shuffle the Array
# https://leetcode.com/problems/shuffle-the-array/description/
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # intialize the left and right pointers to start and n
        left = 0
        right = n
        # initialize the result list
        result = []
        # loop until left value is < n and right value is < 2n
        while left < n and right < 2 * n:
            # append the first value and right value
            result.append(nums[left])
            result.append(nums[right])
            # increment the left and right pointers
            left += 1
            right += 1
        # return the result list
        return result

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")