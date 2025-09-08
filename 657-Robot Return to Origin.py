# Leetcode Problem 657: Robot Return to Origin
# https://leetcode.com/problems/robot-return-to-origin/
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # robot starts from position (0,0), so initialized two variables a, b to 0
        a = b = 0
        # determine the character and it's movement
        for move in moves:
            # if it moves upwards, we increase the b value by 1
            if move == 'U':
                b += 1
            # if it moves downwards, we decrease the b value by 1
            elif move == 'D':
                b -= 1
            # if it moves left, we decrease the a value by 1
            elif move == 'L':
                a -= 1
            # if it moves right, we increase the a value by 1
            elif move == 'R':
                a += 1
        # we need to check, if the robot is returning to its (0,0) at the end
        return True if a == b == 0 else False

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")