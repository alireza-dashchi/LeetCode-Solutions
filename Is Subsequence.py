class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Create a copy of t to track remaining characters as we check subsequence
        t_copy = t[:]
        
        # Iterate over each character in s
        for i in range(len(s)):
            # Check if the current character of s is in the remaining t_copy
            if s[i] in t_copy:
                # Find the index of the character in t_copy
                t_index = t_copy.index(s[i])
                # Update t_copy to exclude all characters before and including the found index
                t_copy = t_copy[t_index + 1:]
            else:
                # If the character is not found, s is not a subsequence of t
                return False
        
        # If all characters of s are found in order, return True
        return True