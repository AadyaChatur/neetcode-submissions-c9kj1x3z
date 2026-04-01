class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq = {}
        for x in s:
            freq[x] = freq.get(x,0) + 1
        
        for k in t:
            if k in freq.keys():
                freq[k] = freq[k] - 1
            
            else:
                return False

        for count in freq.values():
            if count != 0 :
                return False
        return True        