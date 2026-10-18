class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_map = {}

        for i , x in enumerate(nums):
            a = target - x

            if a in my_map:
                return [my_map[a] , i]
            else:
                my_map[x] = i
        return []