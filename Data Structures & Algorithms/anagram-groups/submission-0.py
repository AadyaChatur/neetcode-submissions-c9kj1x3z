class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = {}

        for x in strs:
            res = [0]*26
            for i in range(len(x)):
                res[ord(x[i]) - 97] += 1

            key = tuple(res)

            if key not in result:
                result[key] = []
            result[key].append(x)
        
        return list(result.values())