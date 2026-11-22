class Solution:
    def secondLargestElement(self, nums):
        largest=float('-inf')
        second=float('-inf')
        for i in nums:
            if i>largest:
                second=largest
                largest=i
            elif i<largest and i>second:
                second=i
        return second if second!=float('-inf') else -1

#This function takes an array of integers as input and returns second largest number 
