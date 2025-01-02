class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Method 1:
        # Use Python's built-in string find method
        return(haystack.find(needle))

        # Method 2:
        # Get lengths of both strings
        haystack_len = len(haystack)
        needle_len = len(needle)

        # If needle is empty, return 0
        if needle_len == 0:
            return 0

        # Iterate through haystack
        for i in range(haystack_len - needle_len + 1):
            # Compare substring of haystack with needle
            if haystack[i:i + needle_len] == needle:
                return i

        # If no match is found
        return -1