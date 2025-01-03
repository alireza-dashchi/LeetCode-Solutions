class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Method 1:
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

        # Method 2: (Better Time Complexity)
        # Two pointers: one for s and one for t
        s_index, t_index = 0, 0

        while s_index < len(s) and t_index < len(t):
            # If characters match, move the s pointer
            if s[s_index] == t[t_index]:
                s_index += 1
            # Always move the t pointer
            t_index += 1

        # If we've gone through all characters in s, it's a subsequence
        return s_index == len(s) 