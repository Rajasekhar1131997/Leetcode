# Leetcode Problem 2678: Number of Senior Citizens
# https://leetcode.com/problems/number-of-senior-citizens/description/
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # initialize the count to 0
        count = 0
        # loop through each detail of passenger in details list
        for detail in details:
            # using slicing, find the phone number, age, seat and gender
            phone_number = detail[:10]
            gender = detail[10:11]
            age = detail[11:13]
            seat = detail[13:15]
            # check if their age is strictly more than 60 years old
            if int(age) > 60:
                # if yes, we count that
                count += 1
        # at the end, return the count
        return count

print("Time Complexity: O(N * K) => O(N) since K is fixed and will always be 15 characters")
print("Space Complexity: O(1)")