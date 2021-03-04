#https://leetcode.com/problems/word-ladder/
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def getStepWord(word:str,j:int)->str:
            return word[:j]+"*"+word[j+1:]
        def checkBoundary():
            if endWord not in wordList or not endWord or not beginWord or not wordList:
                return 0
            return 1
        
        if not checkBoundary(): return 0
        
        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        
        for word in wordList:
            for i in range(L):
                all_combo_dict[getStepWord(word,i)].append(word)
                
        queue = collections.deque([(beginWord,1)])
        visited  = {beginWord:True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                intermediate_word = getStepWord(current_word,i)
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level+1))
        return 0
