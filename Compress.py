# https://leetcode.com/problems/string-compression/submissions/
class Solution:
    def compress(self, chars: List[str]) -> int:
        pointer = 0
        iPos = 0
        ctr = 0
        lenChars = len(chars)
        if lenChars == 0:
            return 0
        if lenChars == 1:
            return 1
        prev = chars[pointer]
        pointer +=1
        ctr = 1
        iPos = 1
        totalCtr = 1
        while pointer < lenChars:
            if prev == chars[pointer]:
                ctr+=1
            if prev != chars[pointer]:
                #reset counter to zero, move positon to next point 
                #chars[iPos] = prev
                #iPos +=1
                #prev = chars[pointer]
                #totalCtr += 1
                # Now write the number of characters as characters
                if ctr > 1 :
                    temp = [x for x in str(ctr)]                    
                    totalCtr += len(temp)
                    for j in temp:
                        chars[iPos] = j
                        iPos +=1
                chars[iPos] = chars[pointer]
                prev = chars[pointer]
                totalCtr +=1
                iPos +=1  
                ctr = 1
                    
                
            # In all cases move the pointer
            pointer +=1
        # pointer has come to the end and the very last character needs to be written out.
        # totl ctr gets incremented by number of writes. 
    
        # Now write the number of characters as characters
        if ctr > 1 :
            temp = [x for x in str(ctr)]                    
            totalCtr += len(temp)
            for j in temp:
                chars[iPos] = j
                iPos +=1
        # return the sum of the elements now. 
        return totalCtr
