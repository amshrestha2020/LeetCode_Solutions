The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

 

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1
 

Constraints:

0 <= x, y <= 231 - 1





class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR of two numbers will have all the differing bits set to 1
        xor = x ^ y

        # Count the number of set bits (1s)
        hamming_distance = 0
        while xor:
            # bitwise AND of xor and 1 will be 1 if the last bit is set
            hamming_distance += xor & 1
            # right shift xor by 1 to check the next bit
            xor >>= 1

        return hamming_distance
