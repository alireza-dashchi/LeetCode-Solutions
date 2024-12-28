class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cnt = 0
        length = len(nums)
        val_indices = []

        # Collect indices of elements equal to val
        for i, value in enumerate(nums):
            if value == val:  
                val_indices.append(i)
                cnt += 1

        # Remove elements at collected indices 
        for i in reversed(val_indices):
            nums.pop(i)

        return length - cnt