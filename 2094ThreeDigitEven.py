# https://leetcode.com/problems/finding-3-digit-even-numbers
'''
Let M=min(n 
3
 ,10 
k
 ) be the number of even numbers that meet the requirements, where n is the length of the input array and k is the number of digits in the target even number.

Time complexity: O(n 
3
 +MlogM)

The time complexity for enumerating all combinations of three elements is O(n 
3
 )‘.SortingthevalidevennumbersstoredinthesettakesO(M \log M).−Spacecomplexity:O(M)Thisaccountsforthespaceusedbythehashsetthatstoresallvalidintegers.###Approach2:TraverseAllPossible3−DigitEvenNumbers####IntuitionWecanalsotraverseall3−digitevennumbersfromsmallesttolargest(i.e.,allevennumbersintheclosedinterval[100, 999]),andcheckwhethertheirthreedigitscanbeformedusingdistinctelementsfromtheinputdigitarray.Iftheycan,thenthenumberqualifiesasatargetevennumber;otherwise,itdoesnot.Specifically,wefirstuseahashtable\textit{freq}torecordthefrequencyofeachdigitinthe\textit{digits}array.Whiletraversingevennumbers,weuseanotherhashtable\textit{freq}_1torecordthefrequencyofeachdigitinthecurrentnumber.Atthispoint,a∗∗necessaryandsufficient∗∗conditionforthenumbertobeformedusingthearrayis:Eachdigitin\textit{freq}_1mustappearnomoretimesthanitdoesin\textit{freq}.Wecheckeachevennumberusingthisconditiontodeterminewhetheritqualifies,andcollectallsuchvalidnumbers.Finally,wereturnthesortedarrayoftargetevennumbers.####Implementation<iframesrc="https://leetcode.com/playground/L6bR3gRa/shared"frameBorder="0"width="100kbethenumberofdigitsinthetargetevennumber.−Timecomplexity:O(k \cdot 10^k)Thisrepresentsthetimerequiredtoenumerateallevennumberswithkdigits.−Spacecomplexity:O(1)$
 '''
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        nums = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or i == k:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num >= 100 and num % 2 == 0:
                        nums.add(num)
        res = sorted(list(nums))
        return res
