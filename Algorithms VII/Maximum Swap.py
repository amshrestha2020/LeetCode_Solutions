You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108





class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of characters
        num = list(str(num))
        
        # Create a dictionary to store the last occurrence of each digit
        last = {int(v): i for i, v in enumerate(num)}
        
        # Iterate over the digits in the number
        for i, v in enumerate(num):
            # For each digit, check if there is a larger digit that occurs later
            for d in range(9, int(v), -1):
                if last.get(d, -1) > i:
                    # If there is, swap these two digits and return the result
                    num[i], num[last[d]] = num[last[d]], num[i]
                    return int(''.join(num))
        
        # If no swap is made, return the original number
        return int(''.join(num))
