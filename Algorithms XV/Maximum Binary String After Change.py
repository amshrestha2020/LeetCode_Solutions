You are given a binary string binary consisting of only 0's or 1's. You can apply each of the following operations any number of times:

Operation 1: If the number contains the substring "00", you can replace it with "10".
For example, "00010" -> "10010"
Operation 2: If the number contains the substring "10", you can replace it with "01".
For example, "00010" -> "00001"
Return the maximum binary string you can obtain after any number of operations. Binary string x is greater than binary string y if x's decimal representation is greater than y's decimal representation.

 

Example 1:

Input: binary = "000110"
Output: "111011"
Explanation: A valid transformation sequence can be:
"000110" -> "000101" 
"000101" -> "100101" 
"100101" -> "110101" 
"110101" -> "110011" 
"110011" -> "111011"
Example 2:

Input: binary = "01"
Output: "01"
Explanation: "01" cannot be transformed any further.
 

Constraints:

1 <= binary.length <= 105
binary consist of '0' and '1'.




class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # Find the first '0'
        first_zero = binary.find('0')
        
        # If there are no '0's or only one '0', the string is already maximized
        if first_zero == -1 or binary.count('0') <= 1:
            return binary
        
        # Count total '0's after the first '0'
        zero_count = binary.count('0', first_zero)
        
        # Construct the result:
        # - Keep all leading '1's (before the first '0')
        # - Followed by as many '1's as possible, leave exactly one '0'
        # - The remaining part should be '1's
        return '1' * first_zero + '1' * (zero_count - 1) + '0' + '1' * (len(binary) - first_zero - zero_count)
        