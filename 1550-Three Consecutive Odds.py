# Leetcode Problem 1550: Three Consecutive Odds
# https://leetcode.com/problems/three-consecutive-odds/description/
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # loop through all the elements in the array
        for i in range(len(arr)-2):
            # check if there are any three consecutive off numbers in the array and return true
            if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                return True
        # else, we return false
        return False

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")