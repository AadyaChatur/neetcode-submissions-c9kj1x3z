class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        for num in nums:
            freq[num] = freq.get(num , 0) + 1
        
        res = [[] for i in range(len(nums)+1)]

        for num , frequency in freq.items():
            res[frequency].append(num)

        frequent_nums = []

        for i in range(len(res)-1 , 0 ,-1):
            if not res[i]:
                continue
            
            for x in res[i]:
                frequent_nums.append(x)

                if len(frequent_nums) == k:
                    return frequent_nums