# Arrays, Two pointers, In place

from typing import List

class Solution:
    def movezeroes(self, nums: List[int]) -> None:
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
if __name__ == "__main__":
    nums = [0, 1, 3, 0, 5, 0]
    sol = Solution()
    sol.movezeroes(nums) 
    print(nums)    
