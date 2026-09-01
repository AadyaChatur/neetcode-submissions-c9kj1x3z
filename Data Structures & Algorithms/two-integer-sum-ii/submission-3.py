class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i , j = 0 , len(numbers)-1

        while i <= j :
            some = numbers[i] + numbers[j]

            if some > target:
                j -= 1
            elif some < target:
                i +=1
            else:
                return [i+1 , j+1]