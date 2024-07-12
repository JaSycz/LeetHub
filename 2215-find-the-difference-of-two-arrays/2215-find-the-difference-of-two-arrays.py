class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        dict = {}
        nums1,nums2 = set(nums1),set(nums2)
        for num in nums1:
            dict[num] = 1
        for num in nums2:
            if num in dict:
                dict[num] = -1
            else:
                dict[num] = 2

        lst1,lst2 = [],[]
        print(dict.keys())
        for key, val in dict.items():
            if val == 1:
                lst1.append(key)
            elif val == 2:
                lst2.append(key)
    
        return [lst1,lst2]