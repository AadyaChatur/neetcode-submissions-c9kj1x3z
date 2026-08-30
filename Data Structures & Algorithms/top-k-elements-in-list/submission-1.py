class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for x in nums:
            freq[x] = freq.get(x , 0) + 1
        res = [] 
        for _ in range(k):
            
            max_key = max(freq, key=freq.get)
            res.append(max_key)
            
            del freq[max_key]
        return res    