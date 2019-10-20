'''
https://leetcode.com/problems/print-in-order/
Runtime: 2464 ms, faster than 5.21% of Python3 online submissions for Print in Order.
Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Print in Order.
'''
class Foo:
    def __init__(self):
        self.threads = [0,0,0]


    def first(self, printFirst: 'Callable[[], None]') -> None:
       
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.threads[0] = 1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.threads[0] == 0:
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.threads[1] = 1


    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.threads[1] == 0:
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.threads[2] = 1
