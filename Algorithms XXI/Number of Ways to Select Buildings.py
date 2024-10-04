You are given a 0-indexed binary string s which represents the types of buildings along a street where:

s[i] = '0' denotes that the ith building is an office and
s[i] = '1' denotes that the ith building is a restaurant.
As a city official, you would like to select 3 buildings for random inspection. However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.

For example, given s = "001101", we cannot select the 1st, 3rd, and 5th buildings as that would form "011" which is not allowed due to having two consecutive buildings of the same type.
Return the number of valid ways to select 3 buildings.

 

Example 1:

Input: s = "001101"
Output: 6
Explanation: 
The following sets of indices selected are valid:
- [0,2,4] from "001101" forms "010"
- [0,3,4] from "001101" forms "010"
- [1,2,4] from "001101" forms "010"
- [1,3,4] from "001101" forms "010"
- [2,4,5] from "001101" forms "101"
- [3,4,5] from "001101" forms "101"
No other selection is valid. Thus, there are 6 total ways.
Example 2:

Input: s = "11100"
Output: 0
Explanation: It can be shown that there are no valid selections.
 

Constraints:

3 <= s.length <= 105
s[i] is either '0' or '1'.




class Solution:
    def numberOfWays(self, s: str) -> int:
        zero = 0          # Individual zeroes count
        zeroOne = 0       # Number of combinations of "01"
        one = 0           # Individual ones count
        oneZero = 0       # Number of combinations of "10"
        total = 0         # Final answer

        for ch in s:
            if ch == '0':
                zero += 1
                oneZero += one  # Each of the previously found 1s can pair up with the current 0 to form "10"
                total += zeroOne  # Each of the previously formed "01" can form a triplet with the current 0 to form "010"
            else:
                one += 1
                zeroOne += zero  # Each of the previously found 0s can pair to form "01"
                total += oneZero  # Each of the previously formed "10" can form "101"

        return total        