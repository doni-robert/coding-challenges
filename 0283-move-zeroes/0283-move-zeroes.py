# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         length = len(nums)

#         for i in range(length):
#             if nums[i] == 0:
#                 nums.append(0)
#                 nums[i] = None
#         while None in nums:
#             nums.remove(None)

# 2 Pointer solution
class Solution:
    def moveZeroes(self, nums):
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        
        return nums