# Leetcode Problem 1491: Average Salary Excluding the Minimum and Maximum Salary
# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/
class Solution:
    def average(self, salary: List[int]) -> float:
        # finc the min and maximum salary
        min_salary = min(salary)
        max_salary = max(salary)
        # initialize the variables summ and count to 0
        summ = 0
        count = 0
        # loop through each salary in salary list
        for sal in salary:
            # make sure we exclude the min and max salary when computing and also find the count
            if sal != min_salary and sal != max_salary:
                summ += sal
                count += 1
        # return the average salary of the employees excluding min and max salaries
        return summ / count

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")