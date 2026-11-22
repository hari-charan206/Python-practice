class Solution:
    def moveZeroes(self, nums):
        ze=[]
        n=len(nums)
        for i in range(0,n):
            if nums[i]==0:
                ze.append(0)
                nums.pop(i)
        nums.extend(ze)
        return nums

#Take an array of numbers as input , move zeroes to the end and return the array
