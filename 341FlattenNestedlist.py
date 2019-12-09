# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
'''
Runtime: 72 ms, faster than 35.71% of Python3 online submissions for Flatten Nested List Iterator.
Memory Usage: 16.3 MB, less than 100.00% of Python3 online submissions for Flatten Nested List Iterator.
'''
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
# 341. Flatten Nested List Iterator
class NestedIterator:
    
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        for item in nestedList:
            self.pushIn(item)
    
    def pushIn(self, item : NestedInteger) -> bool:
        if item.isInteger():
            intItem = item.getInteger()
            self.stack.append(intItem)
        else :
            tList = item.getList()
            for a in tList:
                self.pushIn(a)
                
    def next(self) -> int:
        return self.stack.pop(0)
    
    def hasNext(self) -> bool:
        if len(self.stack) == 0:
            return False
        else:
            return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
