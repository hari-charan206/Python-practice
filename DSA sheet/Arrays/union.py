class Solution:
    def unionArray(self, nums1, nums2):
        l=[]
        for i in nums1:
            if i not in l:
                l.append(i)
        for j in nums2:
            if j not in l:
                l.append(j)
        l.sort()
        return l

#Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.
