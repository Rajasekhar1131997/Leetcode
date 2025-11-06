# Leetcode Problem 2042: Check if Numbers Are Ascending in a Sentence
# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/description/
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        # split the given string
        s = s.split()
        # initialize an empty array to store the digits in the string
        nums = []
        # loop through each word in s and if that word is digit, we append that to our nums list
        for word in s:
            if word.isdigit():
                nums.append(word)
        # convert each string into numbers list
        nums_list = [int(d) for d in nums]
        # loop through each number in the list and check if they are strictly increasing or not
        for i in range(len(nums_list)-1):
            if nums_list[i] >= nums_list[i+1]:
                return False
        return True

print("Time Complexity: O(N)")
print("Space Complexity: O(M), where m is the number of digits being stored in the list")