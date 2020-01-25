#https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/submissions/
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #arr.sort()
        cpyArr = arr[:]
        cpyArr.sort()
        lenA = len(arr)
        if lenA == 0:
            return arr
        if lenA == 1:
            return [-1]
        result = [ -1 for x in range(lenA)]
        #cpyArr.remove(arr[0])
        #arr[0] = cpyArr[-1]
        #print(cpyArr, arr)
        '''
        for i in range(1, lenA -1):
            #cpyArr.remove(arr[i])
            idx = cpyArr.index(arr[i])
            cpyArr[idx] = -1
            cpyArr.sort()
            arr[i] = cpyArr[-1]
        arr[-1] = -1
        '''
        i, j = lenA-1, lenA -1
        maxCurrent = -1
        while (i >= 0 and j >=0):
            result[j] = maxCurrent
            if arr[i] > maxCurrent:
                maxCurrent = arr[i]
            j-=1
            i-=1
            
        return result
        
        #return arr
        
