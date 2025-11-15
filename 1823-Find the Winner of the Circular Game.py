# Leetcode Problem 1823: Find the Winner of the Circular Game
# https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # initialize the players list
        players = []
        # add the players into the list from the given range
        for i in range(1, n+1):
            players.append(i)
        # let the index be 0
        index = 0
        # we need to eliminate each value from the list, until there is only player
        while len(players) > 1:
            # compute the index, we need to delete from the list for every loop
            index = (index + k-1) % len(players)
            # pop the player from the list
            players.pop(index)
        # at the end, there will be only one player in the list, we need to return the winner
        return players[0]

print("Time Complexity: O(N^2), since popping from the list takes O(N) time")
print("Space Complexity: O(N)")