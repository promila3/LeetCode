# https://leetcode.com/problems/next-greater-element-i/description/

class Solution:
    def nextGreaterElement1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_uq_map = {}
        len_nums2 = len(nums2)
        for i in range(len_nums2): 
            nums2_uq_map[nums2[i]] = i
        
        nums2_cp = nums2[:] 
        nums2_higher_index = {}
        nums2_cp.sort() # n log n
        for i in range(len_nums2):
            if i < (len_nums2 -1 ):
                if nums2_uq_map[nums2_cp[i+1]] > nums2_uq_map[nums2_cp[i]]:
                    nums2_higher_index[nums2_cp[i]] = nums2_cp[i+1]
                else :
                    nums2_higher_index[nums2_cp[i]] = -1
            else :
                nums2_higher_index[nums2_cp[i]] = -1
        ans = []
        print(nums2_uq_map)
        print(nums2_higher_index)
        for i in range(len(nums1)):
            element = nums2_higher_index[nums1[i]]
            print(element)
            ans.append(element)
        return ans

    def nextGreaterElement(self, nums1, nums2):
        res = [-1] * len(nums1)
        for i, num1 in enumerate(nums1):
            found = False
            for j, num2 in enumerate(nums2):
                if found and num2 > num1:
                    res[i] = num2
                    break

                if num2 == num1:
                    found = True

        return res  
