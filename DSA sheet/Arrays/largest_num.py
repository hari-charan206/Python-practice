class Solution:
    def largestElement(self, nums):
        largest=nums[0]
        for i in nums:
            if i>largest:
                largest=i
        return largest

#The function takes a array of integers as input and returns the largest number
