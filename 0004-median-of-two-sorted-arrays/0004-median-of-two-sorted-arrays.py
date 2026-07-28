class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        l=len(nums1)
        mid=l/2
        if mid==float(l//2):
            return float((nums1[l//2]+nums1[(l//2)-1])/2)
        return nums1[l//2]