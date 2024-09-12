Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.

 

Example 1:

Input: n = 12
Output: true
Explanation: 12 = 31 + 32
Example 2:

Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34
Example 3:

Input: n = 21
Output: false
 

Constraints:

1 <= n <= 107





class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        powers_of_three = []
        power = 1
        while power <= n:
            powers_of_three.append(power)
            power *= 3
        
        # Check if we can represent `n` as a sum of distinct powers of three
        for power in reversed(powers_of_three):
            if n >= power:
                n -= power
        
        return n == 0        