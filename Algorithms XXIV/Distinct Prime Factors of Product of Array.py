Given an array of positive integers nums, return the number of distinct prime factors in the product of the elements of nums.

Note that:

A number greater than 1 is called prime if it is divisible by only 1 and itself.
An integer val1 is a factor of another integer val2 if val2 / val1 is an integer.
 

Example 1:

Input: nums = [2,4,3,7,10,6]
Output: 4
Explanation:
The product of all the elements in nums is: 2 * 4 * 3 * 7 * 10 * 6 = 10080 = 25 * 32 * 5 * 7.
There are 4 distinct prime factors so we return 4.
Example 2:

Input: nums = [2,4,8,16]
Output: 1
Explanation:
The product of all the elements in nums is: 2 * 4 * 8 * 16 = 1024 = 210.
There is 1 distinct prime factor so we return 1.
 

Constraints:

1 <= nums.length <= 104
2 <= nums[i] <= 1000




class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def sieve(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
            for i in range(2, int(n ** 0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            primes = [i for i in range(2, n + 1) if is_prime[i]]
            return primes
        
        # Step 2: Prime factorization of a number
        def prime_factors(num, primes):
            factors = set()
            for prime in primes:
                if prime * prime > num:  # No need to check beyond square root of num
                    break
                while num % prime == 0:
                    factors.add(prime)
                    num //= prime
            if num > 1:  # if num itself is a prime number
                factors.add(num)
            return factors
        
        # Step 3: Find all distinct prime factors in the product of nums
        max_num = 1000  # given constraint
        primes = sieve(max_num)
        distinct_primes = set()
        
        for num in nums:
            distinct_primes.update(prime_factors(num, primes))
        
        return len(distinct_primes)        