# Leetcode Problem 49: Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/
# solving the problem using defaultdict
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initializing the default dictionary
        dic = defaultdict(list)
        # for word in strs:
        #     dic["".join(sorted(word))].append(word)
        # return list(dic.values())
        # loop through each word in given list
        for word in strs:
            # initialize an empty list with 0's of 26 characters.
            lst = [0] * 26
            # loop through each character in word
            for char in word:
                # for every char we come across, we change/increment the value by 1
                lst[ord(char) - ord('a')] += 1
            # we then convert the list into tuple
            lst = tuple(lst)
            # after converting into tuple, we append that word to dict
            dic[lst].append(word)
        # in the end, we have to return the list of dic values, which stores the grouped anagrams
        return list(dic.values())

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")