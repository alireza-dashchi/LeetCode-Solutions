class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
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
