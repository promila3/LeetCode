# https://leetcode.com/problems/unique-email-addresses/
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def process(email:str)->str:
            i = 0
            
            first, second = email.split('@')
            length = len(first)
            result = ""
            while i < length:
                if first[i] == '.':
                    i +=1
                    continue
                if first[i] == '+':
                    break
                result += first[i]
                i +=1
            return result+'@'+second
        result = set()
        for email in emails:
            result.add(process(email))
        
        return len(result)
