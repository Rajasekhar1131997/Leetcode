# Leetcode Problem 551: Student Attendance Record I
# https://leetcode.com/problems/student-attendance-record-i/description/
class Solution:
    def checkRecord(self, s: str) -> bool:
        # initialize the absent and late counts variables
        absent_count = late_count = 0
        # loop through each character in string s
        for ch in s:
            # if the character is A, increment the absent count by 1
            if ch == 'A':
                absent_count += 1
                # check absent condition is satisfied or not
                if absent_count >= 2:
                    return False
                # reset the late count to 0
                late_count = 0
            # if the character is L, increment the late count by 1
            elif ch == 'L':
                late_count += 1
                # checking the late count condition
                if late_count >= 3:
                    return False
            # while traversing, if we found "P" character, we reset the late count to 0
            else:
                late_count = 0
        # we return True if the above conditions failed.
        return True

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")