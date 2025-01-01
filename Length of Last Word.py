class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Split the string into words and return the length of the last word
        s_list = s.split()
        return(len(s_list[-1]))

    