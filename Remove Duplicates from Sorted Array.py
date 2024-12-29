class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        cnt = 1 
        i = 1  # Start from the second element

        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)  # Remove the duplicate element
            else:
                cnt += 1
                i += 1  # Move to the next element only if no pop occurs

        return cnt