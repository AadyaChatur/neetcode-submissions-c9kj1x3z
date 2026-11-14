class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}

        for x in strs:
            key_res = [0]*26
            for i in x:
                key_res[ord(i) - 97] += 1 
            
            res.setdefault(tuple(key_res) , []).append(x)
        return list(res.values())