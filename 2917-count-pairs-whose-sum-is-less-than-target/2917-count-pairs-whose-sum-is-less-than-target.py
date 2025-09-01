class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # initialize the count to 0
        count = 0
        # loop through each value in nums
        for i in range(len(nums)):
            # loop through each value in nums
            for j in range(len(nums)):
                # need to satisfy the condition 0<=i<j<n
                if i < j:
                    # need to satisfy this condition as well
                    if nums[i] + nums[j] < target:
                        # we increment the count by 1
                        count += 1
        # return count
        return count