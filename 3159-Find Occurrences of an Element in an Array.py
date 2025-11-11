# Leetcode Problem 3159: Find Occurrences of an Element in an Array
# https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/description/
class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        # initialize an empty output array and indices array
        output = []
        indices = []
        # loop and enumerate through nums array
        for i, value in enumerate(nums):
            # find the indices of each x value in nums array and append them to indices list
            if x == value:
                indices.append(i)
        # loop through each query in queries list
        for query in queries:
            # if the query is <= length of indices, we add that index value to output
            if query <= len(indices):
                output.append(indices[query-1])
            # otherwise, we append -1 to the list
            else:
                output.append(-1)
        # return output as result
        return output

print("Time Complexity: O(N + M) where N is for nums list and M is for number of queries")
print("Space Complexity: O(N)")