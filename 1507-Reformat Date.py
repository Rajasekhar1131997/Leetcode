# Leetcode Problem 1507: Reformat Date
# https://leetcode.com/problems/reformat-date/description/
class Solution:
    def reformatDate(self, date: str) -> str:
        # initialize the dictionary with months with their respective numbers
        Months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov":"11", "Dec":"12"}
        # get the day, month and year from the input using split command
        day, month, year = date.split()
        # convert the day into 2 digit day using zfill 
        day = day[:-2].zfill(2)
        # returning the output
        return f"{year}-{Months[month]}-{day}"

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")