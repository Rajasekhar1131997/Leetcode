# Leetcode Problem 1108: Defanging an IP Address
# https://leetcode.com/problems/defanging-an-ip-address/description/
class Solution:
    def defangIPaddr(self, address: str) -> str:
        # initialize an empty string
        new_address = ""
        # loop through each character in address string
        for char in address:
            # if the char is not period . we keep adding that to new string
            if char != ".":
                new_address += char
            # else, we change it to [.] and add it to new string
            else:
                new_address += "[.]"
        # return the new string
        return new_address

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")