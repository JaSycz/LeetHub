class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        for i in range(min(len1,len2), 0, -1):
            if (len1 % i == 0 and len2 % i == 0):
                l1, l2 = len1 // i, len2 // i
                if str1[:i] * l1 == str1 and str1[:i] * l2 == str2:
                    return str1[:i]
            


        return ""


        