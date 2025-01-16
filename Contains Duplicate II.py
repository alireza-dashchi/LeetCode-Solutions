class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Method 1:
        my_dict = {}
        for i, value in enumerate(nums):
            # Check if value is already in the dictionary
            if value in my_dict:
                # Return True if the difference of indices is <= k
                if i - my_dict[value] <= k:
                    return True
                else:
                    # Update the index of the value
                    my_dict[value] = i
            else:
                # Add value and its index to the dictionary
                my_dict[value] = i
        return False
        
        # Method 2:
        # Dictionary to store the most recent index of each value
        my_dict = {}
        
        for i, value in enumerate(nums):
            # If the value exists in the dictionary and the index difference is <= k, return True
            if value in my_dict and i - my_dict[value] <= k:
                return True
            # Update the index of the value
            my_dict[value] = i
        
        # If no duplicates with required condition are found, return False
        return False
