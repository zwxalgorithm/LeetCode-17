class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            elif nums[low] < nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid
                else:
                    low = mid + 1
            elif nums[mid] < nums[high - 1]:
                if nums[mid] < target <= nums[high - 1]:
                    low = mid + 1
                else:
                    high = mid
            elif nums[low] == nums[mid]:
                low += 1
            else:
                high -= 1
        return False
