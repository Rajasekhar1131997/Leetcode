# Leetcode Problem 2154: Keep Multiplying Found Values by Two
# https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # check if the original number is present in the nums list or not
        if original in nums:
            # recursive call to the function
            return self.findFinalValue(nums,original*2)
        # finally, we return the original value
        return original

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")