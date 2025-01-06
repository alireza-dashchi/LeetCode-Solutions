class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
         # Sort both strings and compare their sorted versions
        # If they are the same, it means `t` is an anagram of `s`
        return sorted(s) == sorted(t)

        