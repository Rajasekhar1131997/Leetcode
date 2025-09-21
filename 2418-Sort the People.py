# Leetcode Problem 2418: Sort the People
# https://leetcode.com/problems/sort-the-people/description/
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # using zip command, we can match each name with their respective height
        pairs = list(zip(names, heights))
        # once matched, we sort the pairs using lambda function based on height values in desc order
        sorted_pairs = sorted(pairs, key=lambda x:x[1], reverse=True)
        # once sorted, we need to output only names
        return [name for name, height in sorted_pairs]

print("Time Complexity: O(N logN)")
print("Space Complexity: O(N)")