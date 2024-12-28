class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Replace the zero placeholders in nums1 with elements from nums2
        nums1[m:] = nums2
        
        # Sort the array
        nums1.sort()
