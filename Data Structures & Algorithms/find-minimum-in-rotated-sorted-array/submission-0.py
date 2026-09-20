class Solution:
    def findMin(self, nums: List[int]) -> int:

        i = 0
        if nums[i] < nums[len(nums)-1]:
            return nums[i]
        while i < len(nums)-1:
            if nums[i] > nums[i+1]:
                return nums[i+1]
            i +=1
        
        return nums[0]