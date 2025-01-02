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