# Leetcode Problem 3069: Distribute Elements Into Two Arrays I
# https://leetcode.com/problems/distribute-elements-into-two-arrays-i/description/
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        # performing the 1st operation
        arr1 = [nums[0]]
        # performing the 2nd operation
        arr2 = [nums[1]]
        # base case, if there are only 3 values in the list, we perform the 3rd operation
        if arr1[0] > arr2[0]:
            arr1.append(nums[2])
        else:
            arr2.append(nums[2])
        # if there are more than 3 values, we perform the operation until all the values are completed from the list
        for i in range(3, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        # finally, return the concatenation of both arrays
        return arr1 + arr2

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")