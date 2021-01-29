 #https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
 def getSmallestString(self, n: int, k: int) -> str:
        result = ""
        numToLetter = dict(enumerate(string.ascii_lowercase))
        print(numToLetter)
        while k > 0:
            if k == n:
                result = "a"*n + result
                k = 0
                continue
            largest = k - (n-1)
            quotient = largest // 26
            #print(quotient)
            if quotient > 0:
                largest = 26
                k -= 26 * quotient
                n -= quotient
                result = numToLetter[largest-1] * quotient + result
            else:
                k -= largest 
                n -= 1
                result = numToLetter[largest-1] + result
            
        return result
