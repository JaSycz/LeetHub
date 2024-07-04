class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        i = 0
        j = len(s) - 1
        
        lst = list(s)
        
        while i < j:
            i_vowel = s[i] in vowels
            j_vowel = s[j] in vowels
            if i_vowel and j_vowel:
                lst[i] = s[j]
                lst[j] = s[i]
                i+=1
                j-=1
            elif i_vowel:
                j-=1
            elif j_vowel:
                i+=1
            else:
                i+=1
                j-=1
                
                
        return ''.join(lst)
                
                