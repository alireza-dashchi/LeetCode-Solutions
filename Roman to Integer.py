class Solution(object):
    def romanToInt(self, s):
        """
        Convert a Roman numeral string to an integer.
        
        :type s: str
        :rtype: int
        """
        # Mapping of Roman numerals to integers
        roman_to_int_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # Convert Roman numerals to their integer values
        values = [roman_to_int_map[char] for char in s]

        # Adjust values for subtraction cases
        for i in range(len(values) - 1):
            if values[i] < values[i + 1]:  # Subtraction rule
                values[i] = -values[i]

        # Return the sum of adjusted values
        return sum(values)