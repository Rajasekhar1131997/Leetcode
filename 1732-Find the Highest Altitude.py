# Leetcode Problem 1732: Find the Highest Altitude
# https://leetcode.com/problems/find-the-highest-altitude/description/
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # intialize the altitude and max altitude to 0
        max_alt = 0
        alt = 0
        # loop through each altitude/change in gain list
        for change in gain:
            # find the change in altitude
            alt += change
            # we need to keep track of max_altitude for every change
            max_alt = max(max_alt, alt)
        # finally, return the maximum altitude
        return max_alt

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")