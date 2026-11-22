class Solution:
    def linearSearch(self, nums, target):
        for i in range(0,len(nums)):
            if nums[i]==target:
                return i 
        return -1

#This function takes two inputs array of integers and a target , it runs a linear search and returns the index if number is in the array else returns -1
