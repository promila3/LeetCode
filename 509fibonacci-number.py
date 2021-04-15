#https://leetcode.com/problems/fibonacci-number/
class Solution:
    def __init__(self):
        self.memo = []
    def fib(self, n: int) -> int:
        self.memo = [0 for i in range(n+1)]
        self.memo[0] = 0
        if n >= 1:
            self.memo[1] = 1
        return self.fib_m(n)

    def fib_m(self, n:int) -> int:
        print(self.memo)
        if n == 0:
            return self.memo[n]
        if n == 1:
            return self.memo[n]
        if self.memo[n] != 0:
            return self.memo[n]
        first_term = self.memo[n-1] if (n > 0 and self.memo[n-1] != 0 ) else self.fib_m(n-1) 
        second_term = self.memo[n-2] if (n > 1 and self.memo[n-2] !=0 ) else self.fib_m(n-2)
        self.memo[n] = first_term + second_term
        print(self.memo)
        return self.memo[n]
