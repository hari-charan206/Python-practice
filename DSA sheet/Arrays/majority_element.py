class Solution:
    def majorityElement(self, nums):
        dic={}
        maxi=0
        for i in nums:
            dict[i]+=1
            if dict[i]>maxi:
                maxi=i

#Given an integer array nums of size n, return the majority element of the array.
