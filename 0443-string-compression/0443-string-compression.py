class Solution:
    def compress(self, chars: List[str]) -> int:
        if(len(chars) == 1):
            return len(chars)
        s = ""

        prev = chars[0]
        group_len = 1
        for i in range(1,len(chars)):
            if  prev == chars[i]:
                group_len += 1
            else:
                if group_len == 1: 
                    s = s + prev
                else:
                    s = s + prev + str(group_len)
                group_len = 1

            if i+1 == len(chars):
                if prev != chars[i]:
                    s = s + chars[i]
                else:
                    s = s + chars[i] + str(group_len)
                
            
            prev = chars[i]
        chars[:] = list(s)   
        
        return len(s)
