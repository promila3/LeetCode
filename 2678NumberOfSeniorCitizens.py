# https://leetcode.com/problems/number-of-senior-citizens/
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        person_more_than_60 = 0
        for name in details:
            if int(name[11]) > 6:
                person_more_than_60 +=1 
                continue
            if int(name[11]) == 6:
                if int(name[12]) > 0:
                    person_more_than_60 +=1 
                    continue
        return person_more_than_60
