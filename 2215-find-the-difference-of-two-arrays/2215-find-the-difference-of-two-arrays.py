class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1,set2 = set(nums1),set(nums2)
        lst1,lst2 = [],[]
        for num in set1:
            if num not in set2:
                lst1.append(num)
        for num in set2:
            if num not in set1:
                lst2.append(num)        

        
        
        return [lst1,lst2]