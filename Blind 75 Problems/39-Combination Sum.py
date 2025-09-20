# Leetcode Problem 39: Combination Sum
# https://leetcode.com/problems/combination-sum/description/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort the candidates list
        candidates.sort()
        # create an empty list to hold the result
        result = []
        # caller/helper function backtrack
        def combination(current, start, target):
            # base case, if the target value is 0, we append the current combination to result and exit and continue with other values
            if target == 0:
                result.append(current)
                return
            # loop through the list of values
            for i in range(start, len(candidates)):
                # check if the current value is greater than our target value, we exit the loop
                if candidates[i] > target:
                    break
                # call the helper function with current value and existing combination values, current value, and every time we call the helper function, we decrease the target value with the value
                combination(current + [candidates[i]], i, target - candidates[i])
            return
        # call the recursive helper function from base, with empty list, 0 and target value
        combination([], 0, target)
        # we return the combinations list at the end
        return result

print("Time Complexity: 2^T, where T is target")
print("Space Complexity: O(T)")