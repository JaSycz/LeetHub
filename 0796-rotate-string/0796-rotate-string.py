class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        all_str = set()

        for i in range(0,len(s)):
            i_str = []
            for n in range(i,len(s)+i):
                index = n % (len(s))
                i_str.append(s[index])
            all_str.add("".join(i_str))


        print(all_str)
        return goal in all_str