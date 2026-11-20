class Solution:
    def missingNumber(self, nums):
        nums.sort()
        if nums[0]!=0:
            return 0
        for i in range(1,len(nums)+1):
            if i not in nums:
                return i

#Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), return the only number missing from the array within this range.
