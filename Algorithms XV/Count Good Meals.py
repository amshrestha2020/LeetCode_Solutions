A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.

You can pick any two different foods to make a good meal.

Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of different good meals you can make from this list modulo 109 + 7.

Note that items with different indices are considered different even if they have the same deliciousness value.

 

Example 1:

Input: deliciousness = [1,3,5,7,9]
Output: 4
Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.
Example 2:

Input: deliciousness = [1,1,1,3,3,3,7]
Output: 15
Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.
 

Constraints:

1 <= deliciousness.length <= 105
0 <= deliciousness[i] <= 220



class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = 2**21  # Largest sum we care about (2^21 is greater than 2 * 2^20)
        
        # Precompute all powers of 2 up to the relevant limit
        powers_of_two = [1 << i for i in range(22)]  # Powers of 2 from 2^0 to 2^21
        
        count_map = {}
        good_meals = 0
        
        for x in deliciousness:
            for power in powers_of_two:
                y = power - x
                if y in count_map:
                    good_meals += count_map[y]
                    good_meals %= MOD
            
            # Increment the count of the current deliciousness value
            count_map[x] = count_map.get(x, 0) + 1
        
        return good_meals        