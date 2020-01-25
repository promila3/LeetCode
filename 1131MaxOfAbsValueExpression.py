#https://leetcode.com/problems/maximum-of-absolute-value-expression/

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        maxVal = float('-inf')
        lenA = len(arr1)
        # N*2 solution
        '''
        for i in range(lenA-1):
            for j in range(i, lenA):
                temp = abs(arr1[i] - arr1[j])+ abs(arr2[i] - arr2[j]) + abs(i - j)
                if temp > maxVal:
                    maxVal = temp
        '''
        case1 = float('-inf')
        case2 = float('-inf')
        case3 = float('-inf')
        case4 = float('-inf')
        case1Min = float('inf')
        case2Min = float('inf')
        case3Min = float('inf')
        case4Min = float('inf')
        for i in range(lenA):
            case1 = max(case1, arr1[i] + arr2[i] -i)
            case1Min =  min(case1Min, arr1[i] + arr2[i] -i)
            case2 =max(case2, arr1[i] - arr2[i] -i)
            case2Min = min(case2Min, arr1[i] - arr2[i] -i)
            case4 =max(case4, arr2[i] - arr1[i] -i)
            case4Min = min(case4Min, arr2[i] - arr1[i] -i)
            case3 = max(case3, arr1[i] + arr2[i] +i)
            case3Min = min(case3Min, arr1[i] + arr2[i] +i)
        return max(case1 - case1Min, case2 - case2Min, case3 - case3Min, case4 - case4Min)
        
        
        return maxVal
        
