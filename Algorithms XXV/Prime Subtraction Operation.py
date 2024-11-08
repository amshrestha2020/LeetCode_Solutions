You are given a 0-indexed integer array nums of length n.

You can perform the following operation as many times as you want:

Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].
Return true if you can make nums a strictly increasing array using the above operation and false otherwise.

A strictly increasing array is an array whose each element is strictly greater than its preceding element.

 

Example 1:

Input: nums = [4,9,6,10]
Output: true
Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
After the second operation, nums is sorted in strictly increasing order, so the answer is true.
Example 2:

Input: nums = [6,8,11,12]
Output: true
Explanation: Initially nums is sorted in strictly increasing order, so we don't need to make any operations.
Example 3:

Input: nums = [5,8,3]
Output: false
Explanation: It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
nums.length == n



class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        from typing import List

        primes = self.sieveOfEratosthenes(1000)
        
        # Traverse nums from the second last element to the beginning
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] >= nums[i]:
                index = -1
                for prime in primes:
                    if prime >= nums[i - 1]:
                        break
                    if nums[i - 1] - prime < nums[i]:
                        index = prime
                        break
                if index == -1:
                    return False
                nums[i - 1] -= index  # Subtract the found prime from nums[i-1]
        
        return True

    def sieveOfEratosthenes(self, count: int) -> List[int]:
        primes = [True] * (count + 1)
        result = []
        
        for i in range(2, int(count**0.5) + 1):
            if primes[i]:
                for j in range(i * i, count + 1, i):
                    primes[j] = False
        
        for i in range(2, count + 1):
            if primes[i]:
                result.append(i)
        
        return result

