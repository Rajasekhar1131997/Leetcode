# Leetcode Problem 1114: Print in Order
# https://leetcode.com/problems/print-in-order/description/
# import the Event from threading library
from threading import Event
class Foo:
    def __init__(self):
        # initialize the first and second thread events
        self.first_done = Event()
        self.second_done = Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        # signals that first thread event is done executing the code
        self.first_done.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # wait untils the first thread event completes
        self.first_done.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        # signals that second thread event is done executing the code
        self.second_done.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # waits until the second thread event is done executing the code
        self.second_done.wait()        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")