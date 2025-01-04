class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Create two dictionaries to store character mappings
        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            # Check if there's a conflict in s -> t mapping
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t

            # Check if there's a conflict in t -> s mapping
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s

        return True