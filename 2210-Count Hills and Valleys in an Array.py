# Leetcode Problem 2210: Count Hills and Valleys in an Array
# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # initialize the count to 0
        count = 0
        # initialize a new list to first element from nums to check the previous element
        nums_list = [nums[0]]
        # loop through number starting from index 1 to end of list
        for i in range(1, len(nums)):
            # check if there are any equal neighbors and eliminate them and add the rest of the numbers to nums_list
            if nums[i] != nums[i-1]:
                nums_list.append(nums[i])
        # loop through numbers ranging from 1 to n-1 numbers
        for i in range(1, len(nums_list)-1):
            # check whether the current number is either a valley or hill and count it
            if (nums_list[i] > nums_list[i-1] and nums_list[i] > nums_list[i+1]) or (nums_list[i] < nums_list[i-1] and nums_list[i] < nums_list[i+1]):
                    count += 1
        # return the count at the end
        return count

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")