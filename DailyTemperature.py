'''
Runtime: 640 ms, faster than 15.79% of Python3 online submissions for Daily Temperatures.
Memory Usage: 17.4 MB, less than 15.79% of Python3 online submissions for Daily Temperatures.
'''
# https://leetcode.com/problems/daily-temperatures/submissions/
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        lenT = len(T)
        stack = []
        top = 0
        result = []
        for i in range(lenT-1, -1, -1):
            if len(stack) == 0:
                stack.append([(T[i], 0)])
                result.append(0)
                ctr = 0
                continue
            ctr = 1
            while len(stack) > 0 :
                temp2 = stack[len(stack)-1][0]
                #print(temp2[0])
                if temp2[0] > T[i] :
                    break
                #ctr +=1
                temp = stack.pop()
                #print(temp)
                ctr += temp[0][1]
            if len(stack) == 0:
                stack.append([(T[i], 0)])
                result.append(0)
                ctr = 0
                continue
            else :
                result.append(ctr)
                stack.append([(T[i], ctr)])
        result = result[::-1]
        return result
                
    '''
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        diffL = []
        lenT = len(T)
        for i in range(lenT-1):
            diffL.append(T[i+1] - T[i])
        
        diffL.append(0)
        
        result = []
        lenDiff = len(diffL)
        for i in range(lenDiff):
            ctr = 0
            runningSum = 0
            for j in range(i, lenDiff):
                runningSum += diffL[j]
                if runningSum == 0:
                    result.append(0)
                    break
                else:
                    ctr +=1 
                    if runningSum > 0:
                        result.append(ctr)
                        break
                        
        result.append(0)            
        return result
    '''
    # Stack implementation
