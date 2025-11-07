# Leetcode Problem 1694: Reformat Phone Number
# https://leetcode.com/problems/reformat-phone-number/description/
class Solution:
    def reformatNumber(self, number: str) -> str:
        # initialize an empty list to store only the digits from given string
        new_number = []
        # logic to remove spaces and dashes from string
        for char in number:
            if char == ' ' or char == "-":
                continue
            new_number.append(char)
        # initialize an empty result list
        result = []
        # initialize i = 0 and also find the length of new_number list
        i = 0
        n = len(new_number)
        # loop until we process the length of new number list
        while n > 0:
            # if the length of the digits is > 4, we group digits into 3 numbers each
            if n > 4:
                result.append(''.join(new_number[i:i+3]))
                i += 3
                n -= 3
            # if the length of the digits is 4, we group into length of 2 each and exit the loop
            elif n == 4:
                result.append(''.join(new_number[i:i+2]))
                result.append(''.join(new_number[i+2:i+4]))
                break
            # else, we group into rest of them
            else:
                result.append(''.join(new_number[i:]))
                break
        # finally, return the result list by concatenating with dashes
        return '-'.join(result)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")