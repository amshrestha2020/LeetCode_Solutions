You are given an integer array of unique positive integers nums. Consider the following graph:

There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

 

Example 1:


Input: nums = [4,6,15,35]
Output: 4
Example 2:


Input: nums = [20,50,9,63]
Output: 2
Example 3:


Input: nums = [2,3,6,7,4,12,21,39]
Output: 8
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 105
All the values of nums are unique.




from typing import List
from collections import defaultdict

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def prime_factors(n):
            out = set()
            while n % 2 == 0:
                out.add(2)
                n //= 2
            for i in range(3, int(n**0.5) + 1, 2):
                while n % i == 0:
                    out.add(i)
                    n //= i
            if n > 2:
                out.add(n)
            return out

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        parent = {x: x for x in nums}
        factor_dict = defaultdict(list)

        for num in nums:
            primes = prime_factors(num)
            for prime in primes:
                factor_dict[prime].append(num)

        for _, values in factor_dict.items():
            for i in range(len(values) - 1):
                union(values[i], values[i + 1])

        return max(Counter(find(x) for x in nums).values())
