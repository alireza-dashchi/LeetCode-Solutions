class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Helper to calculate the sum of squares of digits
        def sum_of_squares(num):
            return sum(int(digit) ** 2 for digit in str(num))
        
        seen = set()  # Keep track of numbers we've already seen
        
        while n != 1 and n not in seen:
            seen.add(n)  # Add the number to the set
            n = sum_of_squares(n)  # Update n with the sum of squares of its digits
        
        return n == 1  # If n is 1, it's happy; otherwise, it's not