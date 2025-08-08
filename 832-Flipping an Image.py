# Leetcode Problem 832: Flipping an Image
# https://leetcode.com/problems/flipping-an-image/description/
from typing import List
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # for each row in list matrix, flip the list using two pointers approach
        for row in image:
            left = 0
            right = len(row) - 1
            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1
        # check for each value in the list matrix and change value
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == 1:
                    image[i][j] = 0
                elif image[i][j] == 0:
                    image[i][j] = 1
        # return final flipped and inverted matrix
        return image

print("Time Complexity: O(N^2)")
print("Space Complexity: O(1)")

# Solving this problem using Bit Manipulation (XOR)
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # looping through each row in the list matrix
        for row in image:
            # initializing two pointers left and right
            left, right = 0, len(row) - 1
            # looping until left matches right
            while left <= right:
                # if left == right (middle element in the odd row length), just invert the value
                if left == right:
                    row[left] ^= 1
                # flip and invert the value using XOR
                else:
                    row[left], row[right] = row[right] ^1, row[left] ^1
                # increment and decrement left and right pointers respectively
                left += 1
                right -= 1
        # return the output matrix
        return image

print("Time Complexity: O(N^2)")
print("Space Complexity: O(1)")