# Leetcode Problem 1009: Complement of Base 10 Integer
# https://leetcode.com/problems/complement-of-base-10-integer/description/
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # convert the given decimal number into binary number
        binary_num = format(n, "b")
        # convert the binary number into string
        binary_string = str(binary_num)
        # find the complement string
        complement_string = "".join("1" if ch == "0" else "0" for ch in binary_string)
        # change the complement string into complement number
        complement_num = int(complement_string, 2)
        # return the complement number
        return complement_num

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")