# Leetcode Problem 2243:Calculate Digit Sum of a String
# https://leetcode.com/problems/calculate-digit-sum-of-a-string/description/
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # loop until len(s) is greater than k
        while len(s) > k:
            # group into k characters to a list
            groups = [s[i:i+k] for i in range(0, len(s), k)]
            # for every group, we need to find the sum and again join them into a string
            s = ''.join(str(sum(int(d) for d in group)) for group in groups)
        # finally, return s
        return s

print("Time Complexity: O(M * N)")
print("Space Complexity: O(N)")