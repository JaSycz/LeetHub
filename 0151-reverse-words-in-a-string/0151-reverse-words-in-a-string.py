class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = []
        word = ''
        for i in range(0,len(s)+1):
            if  (i == len(s) or s[i] == ' ') and not word.isspace():
                words.append(word)
                word = ''
                continue
            word+=s[i]

        res = ''
        for j in range(len(words)-1,-1,-1):
            if not words[j].isspace() and words[j]!='':
                res+= words[j]+ ' '

        return res.strip()