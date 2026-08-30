class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        m_count = 0
        nums = set(nums)
        for x in nums:

            if x -1 in nums:
                continue
            
            count = 1
            while x+1 in nums:
                count += 1
                x = x +1

            m_count = max(m_count , count)

        return m_count