class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dict = {}
        op = 0

        for num in nums:
            result = k - num

            if result in dict.keys():
                op+=1
                if dict.get(result) == 1:
                    dict.pop(result)
                else:
                    dict[result] -= 1
            else:
                dict.update({num : dict.get(num,0)+1})

        return op
