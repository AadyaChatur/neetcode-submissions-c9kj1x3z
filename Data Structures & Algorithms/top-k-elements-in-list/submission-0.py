class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        result = [[] for i in range(len(nums)+1)]
        res = []

        freq = {}
        for x in nums:
            freq[x] = freq.get(x,0) + 1
        
        for keys , values in freq.items():
            result[values].append(keys)

        for i in range(len(result)-1, 0 ,-1):
            for n in result[i]:
                res.append(n)

            if len(res) == k:
                return res     