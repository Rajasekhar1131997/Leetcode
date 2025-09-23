# Leetcode Problem 1360: Number of Days Between Two Dates
# https://leetcode.com/problems/number-of-days-between-two-dates/description/
from datetime import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # helper function to determine the number of days from base date which 1900-01-01
        def f(date):
            # initializing the base date
            base_date = datetime(1900, 1, 1)
            # assigning the target date
            target_date = datetime.strptime(date, "%Y-%m-%d")
            # find the difference of days from target date to base date
            delta = target_date - base_date
            # return only the dates
            return delta.days
        # we need to calculate the number of days b/w two dates
        return (abs(f(date1) - f(date2)))

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")