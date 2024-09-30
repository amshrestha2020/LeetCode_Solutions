You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. n of the observations went missing, and you only have the observations of m rolls. Fortunately, you have also calculated the average value of the n + m rolls.

You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. You are also given the two integers mean and n.

Return an array of length n containing the missing observations such that the average value of the n + m rolls is exactly mean. If there are multiple valid answers, return any of them. If no such array exists, return an empty array.

The average value of a set of k numbers is the sum of the numbers divided by k.

Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.

 

Example 1:

Input: rolls = [3,2,4,3], mean = 4, n = 2
Output: [6,6]
Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.
Example 2:

Input: rolls = [1,5,6], mean = 3, n = 4
Output: [2,3,2,2]
Explanation: The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.
Example 3:

Input: rolls = [1,2,3,4], mean = 6, n = 4
Output: []
Explanation: It is impossible for the mean to be 6 no matter what the 4 missing rolls are.
 

Constraints:

m == rolls.length
1 <= n, m <= 105
1 <= rolls[i], mean <= 6



class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_sum = mean * (n + m)
        
        # Step 2: Calculate the known sum of the rolls we already have
        known_sum = sum(rolls)
        
        # Step 3: Calculate the sum of the missing rolls
        missing_sum = total_sum - known_sum
        
        # Step 4: Check if the missing_sum is feasible to distribute across n rolls
        if missing_sum < n or missing_sum > 6 * n:
            return []
        
        # Step 5: Distribute the missing_sum across n rolls
        # Start by giving each roll a value of 1, then distribute the remaining sum
        result = [1] * n
        remaining_sum = missing_sum - n  # Since each roll is already 1
        
        # Distribute the remaining sum by adding as much as possible to each roll
        for i in range(n):
            # We can add at most 5 more to each roll (to make it a maximum of 6)
            add = min(remaining_sum, 5)
            result[i] += add
            remaining_sum -= add
            if remaining_sum == 0:
                break
        
        return result        