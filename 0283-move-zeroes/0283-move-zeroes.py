class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        for i in range(length):
            if nums[i] == 0:
                nums.append(0)
                nums[i] = None
        while None in nums:
            nums.remove(None)