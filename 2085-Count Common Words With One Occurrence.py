# Leetcode Problem 2085: Count Common Words With One Occurrence
# https://leetcode.com/problems/count-common-words-with-one-occurrence/description/
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        # initialize two hashmaps to get frequencies from words1 and words2
        hash_map1 = {}
        hash_map2 = {}
        # get frequency of each word in words1
        for word in words1:
            hash_map1[word] = hash_map1.get(word, 0) + 1
        # get frequency of each word in words2
        for word in words2:
            hash_map2[word] = hash_map2.get(word, 0) + 1
        # initialize the count to 0
        count = 0
        # check for every word in hashmap1 and it's frequency is 1 and also need to check if that word is present in hashmap2 and it's frequency is also equal to 1, increment the count by 1
        for word in hash_map1:
            if hash_map1[word] == 1 and word in hash_map2 and hash_map2[word] == 1:
                count += 1
        # return the count at the end
        return count

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")