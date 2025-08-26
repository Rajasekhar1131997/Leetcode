# Leetcode Problem 705: Design Hashset
# https://leetcode.com/problems/design-hashset/description/
class MyHashSet:

    # defintion of hashset
    def __init__(self):
        self.hashset = set()

    # we use add built-in library to add value to a hashset
    def add(self, key: int) -> None:
        self.hashset.add(key)

    # we use discard built-in library to safe delete from hashset, we can also use remove
    def remove(self, key: int) -> None:
        self.hashset.discard(key)    

    # if the key exists in hashset, we return true else false
    def contains(self, key: int) -> bool:
        if key in self.hashset:
            return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

print("Time Complexity: O(1) average, O(N) in worst case")
print("Space Complexity: O(N)")