class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        if nums[0]!=0:
            return 0
        for i in range(1,len(nums)+1):
            if i not in nums:
                return i

#This function takes a list of n numbers as input and returns the missing number
