# Leetcode Problem 3280: Convert Date to Binary
# https://leetcode.com/problems/convert-date-to-binary/description/
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        # split the given string into different words using split method
        date = date.split("-")
        # initialize an empty result list
        result = []
        # loop through each num in date
        for num in date:
            # convert the number into binary format and append that to result list
            binary = format(int(num), "b")
            result.append(binary)
        
        # finally, convert the result list into string using join method
        return "-".join(result)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")