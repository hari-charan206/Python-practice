class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count=0
        current=0
        for i in nums:
            if i==1:
                current+=1
                count=max(count,current)
                continue
            current=0
        return count

#The function takes an array of integers an input and returns the maximum consecutive ones in the array
