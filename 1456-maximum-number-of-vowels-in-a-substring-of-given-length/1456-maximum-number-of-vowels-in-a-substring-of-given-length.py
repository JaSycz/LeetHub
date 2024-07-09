class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count+=1
            
        m_vowels = count
        i = 0

        for j in range(k,len(s)):
            if s[j] in vowels:
                count+=1
            if s[i] in vowels and k>1:
                count-=1
            i+= 1 
            m_vowels =  max(count,m_vowels)

        return min(m_vowels,k)


