# Leetcode Problem 347: Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create an empty hash map (dictionary) to store each number and its frequency
        hash_map = {}
        # Iterate through each number in nums
        # Count how many times each number appears using the dictionary
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        # Create a list of empty lists to act as frequency buckets
        # Index represents the frequency, and each bucket holds numbers with that frequency
        freq = [[] for i in range(len(nums) + 1)]
        # Place each number into its corresponding frequency bucket
        for num, count in hash_map.items():
            freq[count].append(num)
        # Initialize a result list to hold the k most frequent elements
        result = []
        # Traverse the frequency buckets in reverse order (highest frequency first)
        for i in range(len(freq) - 1, 0, -1):
            # For each number in the current frequency bucket
            for n in freq[i]:
                # Add the number to the result list
                result.append(n)
                # Once we have collected k elements, return the result
                if len(result) == k:
                    return result

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")