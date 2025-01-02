class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Method 1:
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

        # Method 2:
        # Optimised Solution (Two-Pointer Approach)
        # Step 1: Initialise two pointers, one at the start and one at the end
        left, right = 0, len(s) - 1

        while left < right:  # Process until the two pointers meet
            # Move the left pointer to the next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            # Move the right pointer to the previous alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare the characters (case insensitive)
            if s[left].lower() != s[right].lower():
                return False  # If mismatch, it's not a palindrome

            # Move both pointers inward
            left += 1
            right -= 1

        return True  # If no mismatch, it's a palindrome