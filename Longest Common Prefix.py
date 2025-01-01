class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:  # Check if the array is empty
            return ""

        # Sort the strings so that the first and last strings are the most different;
        # this ensures that their common prefix is the longest common prefix for all strings.
        strs.sort()
        common_prefix = ""
        for i in range(len(strs[0])):
            # Compare characters of the first and last strings
            if strs[0][i] == strs[-1][i]:
                common_prefix += strs[0][i]
            else:
                break  # Exit the loop when characters don't match
        return common_prefix