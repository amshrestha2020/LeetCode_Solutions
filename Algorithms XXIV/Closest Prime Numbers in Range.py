Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right .
num1 and num2 are both prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the minimum num1 value or [-1, -1] if such numbers do not exist.

A number greater than 1 is called prime if it is only divisible by 1 and itself.

 

Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.
Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
 

Constraints:

1 <= left <= right <= 106
 


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve_of_eratosthenes(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False
            
            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            return is_prime
        
        # Generate primes up to 'right'
        is_prime = sieve_of_eratosthenes(right)
        
        # Collect primes in the range [left, right]
        primes_in_range = [i for i in range(left, right + 1) if is_prime[i]]
        
        # Edge case: if there are less than 2 primes, return [-1, -1]
        if len(primes_in_range) < 2:
            return [-1, -1]
        
        # Find the pair with the minimum difference
        min_diff = float('inf')
        closest_pair = [-1, -1]
        
        for i in range(1, len(primes_in_range)):
            num1 = primes_in_range[i - 1]
            num2 = primes_in_range[i]
            diff = num2 - num1
            if diff < min_diff:
                min_diff = diff
                closest_pair = [num1, num2]
        
        return closest_pair        