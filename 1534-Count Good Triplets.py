# Leetcode Problem 1534: Count Good Triplets
# https://leetcode.com/problems/count-good-triplets/description/
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # initialize the count to 0
        count = 0
        # loop through the list of number
        for i in range(len(arr)):
            # start the j loop
            for j in range(i+1, len(arr)):
                # start the k loop
                for k in range(j+1, len(arr)):
                    # check the conditions listed
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        # if they satisfy, count it as a good triplet
                        count += 1
        # return the count
        return count

print("Time Complexity: O(N^3)")
print("Space Complexity: O(1)")