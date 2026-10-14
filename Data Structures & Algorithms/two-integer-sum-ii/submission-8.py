class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l , r = 0 , len(numbers)-1

        while l < r:

            some = numbers[l] + numbers[r]

            if some == target:
                return [l+1 , r+1]
            if some > target:
                r -=1      
            if some < target:
                l += 1
        return False