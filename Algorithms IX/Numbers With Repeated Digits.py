Given an integer n, return the number of positive integers in the range [1, n] that have at least one repeated digit.

 

Example 1:

Input: n = 20
Output: 1
Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.
Example 2:

Input: n = 100
Output: 10
Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
Example 3:

Input: n = 1000
Output: 262
 

Constraints:

1 <= n <= 109





class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        L = list(map(int, str(n + 1)))
        n_digits = len(L)
        
        # Step 1: Calculate numbers with unique digits for lengths < n_digits
        unique_count = 0
        for i in range(1, n_digits):
            unique_count += 9 * self.perm(9, i - 1)
        
        # Step 2: Calculate numbers with unique digits for length == n_digits
        seen = set()
        for i, x in enumerate(L):
            for y in range(i == 0, x):
                if y not in seen:
                    unique_count += self.perm(9 - i, n_digits - i - 1)
            if x in seen:
                break
            seen.add(x)
        
        # Total numbers is n, numbers with repeated digits is n - unique_count
        return n - unique_count

    def perm(self, m, n):
        if n == 0:
            return 1
        return self.perm(m, n - 1) * (m - n + 1)

# Example usage:
sol = Solution()
print(sol.numDupDigitsAtMostN(20))   # Output: 1
print(sol.numDupDigitsAtMostN(100))  # Output: 10
print(sol.numDupDigitsAtMostN(1000)) # Output: 262
