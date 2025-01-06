class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store numbers we've seen and their indices
        seen = {}
        
        # Iterate over the list with both index and value
        for i, num in enumerate(nums):
            # Calculate the complement that would sum to the target
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in seen:
                # If found, return the indices of the complement and current number
                return [seen[complement], i]
            
            # Otherwise, store the current number and its index in the dictionary
            seen[num] = i