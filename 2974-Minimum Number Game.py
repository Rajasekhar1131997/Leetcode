# Leetcode Problem 2974: Minimum Number Game
# https://leetcode.com/problems/minimum-number-game/description/
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # initialize an empty arr to hold the result
        new_arr = []
        # loop through the array half time, since the given array is of even length and everytime 2 elements will be removed
        for i in range(len(nums)//2):
            # alice gets the min element from the nums list
            alice = min(nums)
            # remove that min element from old array
            nums.remove(alice)
            # bob gets the min element from the nums list
            bob = min(nums)
            # remove the min element from old array
            nums.remove(bob)
            # append the new element from bob to new array
            new_arr.append(bob)
            # append the new element from alice to new array
            new_arr.append(alice)
        # return the new array
        return new_arr

print("Time Complexity: O(N^2)")
print("Space Complexity: O(N)")

# we can also solve this problem in O(N logN) time
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # initialize an empty arr to hold the result
        new_arr = []
        # sort the array
        nums.sort()
        # loop through the array
        for i in range(0, len(nums), 2):
            # get the first element
            alice = nums[i]
            # get the second element
            bob = nums[i+1]
            # append the element from bob to new array
            new_arr.append(bob)
            # append the element from alice to new array
            new_arr.append(alice)
        # return the new array
        return new_arr

print("Time Complexity: O(N logN)")
print("Space Complexity: O(N)")