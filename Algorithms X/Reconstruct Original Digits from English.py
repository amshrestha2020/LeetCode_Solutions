Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.

 

Example 1:

Input: s = "owoztneoer"
Output: "012"
Example 2:

Input: s = "fviefuro"
Output: "45"
 

Constraints:

1 <= s.length <= 105
s[i] is one of the characters ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].
s is guaranteed to be valid.






class Solution:
    def originalDigits(self, s: str) -> str:
        # count the occurrence of each character
        count = [0]*26
        for c in s:
            count[ord(c)-ord('a')] += 1

        # find the count of each digit
        digitCount = [0]*10
        digitCount[0] = count[ord('z')-ord('a')]
        digitCount[2] = count[ord('w')-ord('a')]
        digitCount[4] = count[ord('u')-ord('a')]
        digitCount[6] = count[ord('x')-ord('a')]
        digitCount[8] = count[ord('g')-ord('a')]
        digitCount[1] = count[ord('o')-ord('a')] - digitCount[0] - digitCount[2] - digitCount[4]
        digitCount[3] = count[ord('h')-ord('a')] - digitCount[8]
        digitCount[5] = count[ord('f')-ord('a')] - digitCount[4]
        digitCount[7] = count[ord('s')-ord('a')] - digitCount[6]
        digitCount[9] = count[ord('i')-ord('a')] - digitCount[5] - digitCount[6] - digitCount[8]

        # build output
        output = [str(i)*digitCount[i] for i in range(10)]
        return "".join(output)
