# Leetcode Problem 1387: Sort Integers by The Power Value
# https://leetcode.com/problems/sort-integers-by-the-power-value/description/
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # initialize an empty hashmap powers to store power of each integer
        powers = {}
        # loop through the given range inclusively
        for x in range(lo, hi+1):
            # assign the x value to power and the count to 0
            power = x
            count = 0
            # loop until we reach 1 by doing the following steps
            while x != 1:
                # increment the count by 1
                count += 1
                # as per given condition if x is even, we divide else we we compute x
                if x % 2 == 0:
                    x = x // 2
                else:
                    x = (3 * x) + 1
            # once, we found that power of each integer, record that in hashmap
            powers[power] = count
        # sorting the values based on their power
        sorted_values = sorted(powers.items(), key=lambda x:x[1])
        # looping through each pair and returning the integer value
        for index, tuple in enumerate(sorted_values):
            if index == k - 1:
                value, i = tuple
                break
        return value

print("Time Complexity: O(N logN)")
print("Space Complexity: O(N)")