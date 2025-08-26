# Leetcode Problem 706: Design HashMap
# https://leetcode.com/problems/design-hashmap/
class MyHashMap:

    # definition of hashmap
    def __init__(self):
        self.hashmap = {}

    # inserts a key value pair/ if there is a key already, it updates with the current value
    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value

    # get returns the value of the specified key, otherwise it returns -1
    def get(self, key: int) -> int:
        return self.hashmap.get(key, -1)

    # we can use del keyword to delete key from the hashmap or we can use pop function to remove the key, if it doesn't exist it returns None
    def remove(self, key: int) -> None:
        #del self.hashmap[key]
        self.hashmap.pop(key, None)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

print("Time Complexity: O(1) average, it can O(N) in worst case")
print("Space Complexity: O(N)")