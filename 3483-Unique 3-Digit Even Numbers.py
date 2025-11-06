# Leetcode Problem 3483: Unique 3-Digit Even Numbers
# https://leetcode.com/problems/unique-3-digit-even-numbers/description/
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # find the length of the given array
        n = len(digits)
        # initialize the set to store each unique 3 digit even numbers
        s = set()
        # brute force approach, looping to each digit in given list
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    # check the condition and form the 3-digit number
                    if i != j and j != k and i != k:
                        num = digits[i] * 100 + digits[j] * 10 + digits[k]
                        # check if the formed number is even and lies in the 3-digit range
                        if num % 2 == 0 and 100 <= num <= 999:
                            # if yes, add that number to set
                            s.add(num)
        # finally, return the length of the set which contains only 3-digit even numbers
        return len(s)

print("Time Complexity: O(N^3)")
print("Space Complexity: O(1)")