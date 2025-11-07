# Leetcode Problem 2164: Sort Even and Odd Indices Independently
# https://leetcode.com/problems/sort-even-and-odd-indices-independently/description/
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # initialize an empty list for even and odd and also a new list for merging
        even = []
        odd = []
        result = []
        # loop through each number in nums list and separating even and odd numbers
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        # sort the even numbers in increasing order
        even.sort()
        # sort the odd numbers in decreasing order
        odd.sort(reverse=True)
        # loop through each number in nums and append to result list alternatively
        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(even[i // 2])
            else:
                result.append(odd[i // 2])
        # return the result
        return result

print("Time Complexity: O(N log N)")
print("Space Complexity: O(N)")