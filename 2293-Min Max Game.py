# Leetcode Problem 2293: Min Max Game
# https://leetcode.com/problems/min-max-game/
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        # if the length of the given nums list is 1, we return that number
        if len(nums) == 1:
            return nums[0]
        # else, we have to follow the steps provided
        else:
            # find the length of given list
            n = len(nums)
            # initialize an empty list with half the size of given list
            new_nums = [0] * (n//2)
            # loop through each number
            for i in range(n//2):
                # if the number is even, we perform the below operation
                if i % 2 == 0:
                    new_nums[i] = min(nums[2*i], nums[2*i+1])
                # if the number is odd, we perform the below operation
                else:
                    new_nums[i] = max(nums[2*i], nums[2*i+1])
        # call our main function with new list until we process all the values in the list
        return self.minMaxGame(new_nums)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")