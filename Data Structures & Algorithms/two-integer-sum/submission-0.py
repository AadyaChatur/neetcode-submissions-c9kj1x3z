class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        azz = {}
        for i , num in enumerate(nums):
            com = target - num

            if com in azz:
                return [azz[com] , i]
            
            else:
                azz[num] = i 
