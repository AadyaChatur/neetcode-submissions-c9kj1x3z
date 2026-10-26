class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}

        for x in strs:
            count= [0] * 26
            for s in x:
                count[ord(s)-ord('a')] += 1
            res.setdefault(tuple(count) , []).append(x)


        return list(res.values())