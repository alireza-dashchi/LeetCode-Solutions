class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Step 1: Create a list to store alphanumeric characters in lowercase
        s_alphanum_list = []
        for i in s:
            if i.isalnum(): 
                s_alphanum_list.append(i.lower())  

        # Step 2: Compare characters from the beginning and the end of the list
        for i in range(len(s_alphanum_list) // 2):
            if s_alphanum_list[i] != s_alphanum_list[-i-1]:  
                print(s_alphanum_list[i], s_alphanum_list[-i-1])  
                return False  # If mismatch, it's not a palindrome

        return True  # If no mismatch, it's a palindrome