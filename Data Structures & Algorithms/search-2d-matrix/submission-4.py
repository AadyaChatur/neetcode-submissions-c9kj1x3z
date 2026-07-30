class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        outer_l , outer_r = 0,len(matrix)-1


        while outer_l <= outer_r:

            mid = (outer_l + outer_r) //2

            if matrix[mid][-1] < target:
                outer_l = mid + 1

            elif matrix[mid][0] > target:
                outer_r = mid - 1

            else:

                inner_l , inner_r = 0 , len(matrix[mid])-1
                
                
                while inner_l <= inner_r :

                    inner_mid = (inner_l + inner_r)//2

                    if matrix[mid][inner_mid] == target:
                        return True
                    elif matrix[mid][inner_mid] > target:
                        inner_r = inner_mid - 1
                    
                    else:
                        inner_l = inner_mid + 1
                return False
        return False                        