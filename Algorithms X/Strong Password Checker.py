A password is considered strong if the below conditions are all met:

It has at least 6 characters and at most 20 characters.
It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
It does not contain three repeating characters in a row (i.e., "Baaabb0" is weak, but "Baaba0" is strong).
Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

In one step, you can:

Insert one character to password,
Delete one character from password, or
Replace one character of password with another character.
 

Example 1:

Input: password = "a"
Output: 5
Example 2:

Input: password = "aA1"
Output: 3
Example 3:

Input: password = "1337C0d3"
Output: 0
 

Constraints:

1 <= password.length <= 50
password consists of letters, digits, dot '.' or exclamation mark '!'.






class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        
        # Checking the missing types of characters
        missing_lower = missing_upper = missing_digit = 1
        for char in password:
            if char.islower():
                missing_lower = 0
            elif char.isupper():
                missing_upper = 0
            elif char.isdigit():
                missing_digit = 0
        
        # Calculate the number of missing character types
        missing_types = missing_lower + missing_upper + missing_digit
        
        # Check for repeating characters and required replacements
        replace = 0
        one_seq = two_seq = 0
        i = 2
        while i < n:
            if password[i] == password[i-1] == password[i-2]:
                length = 2
                while i < n and password[i] == password[i-1]:
                    length += 1
                    i += 1
                replace += length // 3
                if length % 3 == 0:
                    one_seq += 1
                elif length % 3 == 1:
                    two_seq += 1
            else:
                i += 1
        
        if n < 6:
            return max(missing_types, 6 - n)
        elif n <= 20:
            return max(missing_types, replace)
        else:
            # If length > 20, we need deletions
            delete = n - 20
            # Optimize replacements with deletions
            replace -= min(delete, one_seq * 1) // 1
            replace -= min(max(delete - one_seq, 0), two_seq * 2) // 2
            replace -= max(delete - one_seq - 2 * two_seq, 0) // 3
            return delete + max(missing_types, replace)

# Example usage:
solution = Solution()
print(solution.strongPasswordChecker("a"))          # Output: 5
print(solution.strongPasswordChecker("aA1"))        # Output: 3
print(solution.strongPasswordChecker("1337C0d3"))   # Output: 0
