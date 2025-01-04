class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Create a dictionary to count characters in magazine
        mag_dict = {}
        for i in magazine:
            mag_dict[i] = mag_dict.get(i, 0) + 1
        
        # Check if each character in ransomNote can be used from magazine
        for i in ransomNote:
            if i not in mag_dict or mag_dict[i] == 0:
                return False
            mag_dict[i] -= 1

        return True