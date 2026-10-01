class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            elif nums[mid] > target:

                # Left half is sorted
                if nums[l] <= nums[mid]:

                    if nums[l] <= target:
                        r = mid - 1
                    else:
                        l = mid + 1

                # Right half is sorted
                else:
                    r = mid - 1

            elif nums[mid] < target:

                # Left half is sorted
                if nums[l] <= nums[mid]:
                    l = mid + 1

                # Right half is sorted
                else:

                    if target <= nums[r]:
                        l = mid + 1
                    else:
                        r = mid - 1

        return -1