# Leetcode Problem 1869: Longer Contiguous Segments of Ones than Zeros
# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/description/
# This approach will traverse the string two times --> two pass
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        # get the length of the input binary string
        n = len(s)
        # initialize counters for current streaks of 1s and 0s
        one_count = zero_count = 0
        # initialize variables to keep track of maximum streaks
        max_one_count = max_zero_count = 0
        # -------- First loop: find the longest segment of 1s --------
        for i in range(n):
            if s[i] == '1':
                # if current char is '1', extend the streak
                one_count += 1
                # update maximum streak of 1s if needed
                max_one_count = max(max_one_count, one_count)
            else:
                # if current char is '0', reset the 1s streak
                one_count = 0
        # -------- Second loop: find the longest segment of 0s --------
        for i in range(n):
            if s[i] == '0':
                # if current char is '0', extend the streak
                zero_count += 1
                # update maximum streak of 0s if needed
                max_zero_count = max(max_zero_count, zero_count)
            else:
                # if current char is '1', reset the 0s streak
                zero_count = 0
        # compare the longest segments of 1s and 0s
        if max_one_count > max_zero_count:
            return True   # longest 1s segment is strictly greater
        else:
            return False  # otherwise, 0s segment is equal/greater

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")

# We can solve this problem using single pass/traversing the string in one pass
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        # initialize counters for current streaks of 1s and 0s
        one_count = zero_count = 0
        # initialize variables to keep track of maximum streaks
        max_one_count = max_zero_count = 0
        # loop through each character in string
        for ch in s:
            # if char is 1, we increase the one count by 1 and set zero count to 1
            if ch == "1":
                one_count += 1
                zero_count = 0
            # if char is 0, we increase the zero count by 0 and set one count to 0
            else:
                zero_count += 1
                one_count = 0
            # find the max one count and zero count
            max_one_count = max(max_one_count, one_count)
            max_zero_count = max(max_zero_count, zero_count)
        # return true if max one count is greater else false
        return max_one_count > max_zero_count

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")