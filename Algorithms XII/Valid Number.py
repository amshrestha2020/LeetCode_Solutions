Given a string s, return whether s is a valid number.

For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

Formally, a valid number is defined using one of the following definitions:

An integer number followed by an optional exponent.
A decimal number followed by an optional exponent.
An integer number is defined with an optional sign '-' or '+' followed by digits.

A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:

Digits followed by a dot '.'.
Digits followed by a dot '.' followed by digits.
A dot '.' followed by digits.
An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

The digits are defined as one or more digits.

 

Example 1:

Input: s = "0"

Output: true

Example 2:

Input: s = "e"

Output: false

Example 3:

Input: s = "."

Output: false

 

Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.





class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()  # Remove leading and trailing whitespaces
        
        seen_digit = seen_dot = seen_exponent = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in {'+', '-'}:
                # Sign can only appear at the beginning or after 'e' or 'E'
                if i > 0 and s[i - 1] not in {'e', 'E'}:
                    return False
            elif char == '.':
                # Dot can only appear once and cannot appear after 'e' or 'E'
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            elif char in {'e', 'E'}:
                # Exponent can only appear once and must be followed by an integer
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False  # Reset seen_digit for the integer part after exponent
            else:
                # Other characters are invalid
                return False
        
        # The string must contain at least one digit
        return seen_digit
