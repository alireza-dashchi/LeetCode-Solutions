class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_dict = {}
        
        # Count occurrences of each number
        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1

        # Find the key with the maximum value
        majority_number = None
        max_count = 0

        for key, value in my_dict.items():
            if value > max_count:
                max_count = value
                majority_number = key

        return majority_number