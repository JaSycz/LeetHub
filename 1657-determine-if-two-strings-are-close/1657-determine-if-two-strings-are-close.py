class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq_dict1,freq_dict2 = {},{}
        if set(word1) != set(word2):
            return False
        for i in range(len(word1)):
            freq_dict1[word1[i]] = freq_dict1.get(word1[i],0)+1
            freq_dict2[word2[i]] = freq_dict2.get(word2[i],0)+1
        val1,val2 = sorted(freq_dict1.values()),sorted(freq_dict2.values())

        return  val1 == val2
        