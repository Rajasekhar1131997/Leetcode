# Leetcode Problem 3184: Count Pairs That Form a Complete Day I
# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/description/
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        # initialize the count to 0
        count = 0
        # loop through hours list starting from index 0
        for i in range(len(hours)):
            # loop through hours list starting from index 1
            for j in range(1, len(hours)):
                # check the condition where i < j and hours[i] + hours[j] should be an exact multiple of 24
                if i < j and (hours[i] + hours[j]) % 24 == 0:
                    # if yes, we increment the count by 1
                    count += 1
        # finally, return the count of such pairs
        return count

print("Time Complexity: O(N^2)")
print("Space Complexity: O(1)")