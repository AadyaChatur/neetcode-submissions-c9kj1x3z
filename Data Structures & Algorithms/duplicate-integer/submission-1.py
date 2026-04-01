class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        freq = {}
        for x in nums:
            freq[x] = freq.get(x,0) + 1

        for k , v in freq.items():
            if v>1:
                return True
        return False
        