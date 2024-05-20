class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Determine the length of the input list
        length = len(nums)
        
        # Initialize the answer list with 1s to store the final results.
        ans = length * [1]
        
        # Populate the answer list with products of elements to the right of each index
        # Start from the second last element and move backwards to the first element
        for i in range(length-2, -1, -1):
            # Each element at index i is updated to be the product of the element
            # to its right and the product stored at the index right of i
            ans[i] = ans[i+1] * nums[i+1]
        
        # Initialize a variable to keep track of the cumulative product of elements
        # to the left of the current index
        prefexProduct = 1
        
        # Update the answer list by multiplying each element by the cumulative product
        # of all elements to the left of the current index
        for i in range(0, length):
            # Multiply the current element in ans by the cumulative left product
            ans[i] *= prefexProduct
            
            # Update the cumulative left product by multiplying it with the current element in nums
            prefexProduct *= nums[i]
        
        # Return the final answer list, which contains the product of all elements
        # except the one at each index
        return ans