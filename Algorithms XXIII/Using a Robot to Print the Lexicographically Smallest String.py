You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
Return the lexicographically smallest string that can be written on the paper.

 

Example 1:

Input: s = "zza"
Output: "azz"
Explanation: Let p denote the written string.
Initially p="", s="zza", t="".
Perform first operation three times p="", s="", t="zza".
Perform second operation three times p="azz", s="", t="".
Example 2:

Input: s = "bac"
Output: "abc"
Explanation: Let p denote the written string.
Perform first operation twice p="", s="c", t="ba". 
Perform second operation twice p="ab", s="c", t="". 
Perform first operation p="ab", s="", t="c". 
Perform second operation p="abc", s="", t="".
Example 3:

Input: s = "bdda"
Output: "addb"
Explanation: Let p denote the written string.
Initially p="", s="bdda", t="".
Perform first operation four times p="", s="", t="bdda".
Perform second operation four times p="addb", s="", t="".
 

Constraints:

1 <= s.length <= 105
s consists of only English lowercase letters.


class Solution:
    def robotWithString(self, s: str) -> str:
        t = []  # Use list to simulate StringBuilder for t
        ans = []  # Use list to collect result characters
        st = self.fun(s)
        x = 0

        while st:
            while t and t[-1] <= s[st[-1]]:
                ans.append(t.pop())
            
            t.extend(s[x:st[-1]])  # Append substring from s to t
            ans.append(s[st[-1]])   # Append the current character from s to ans
            
            x = st.pop() + 1
            
            if x == len(s) - 1 and not st:
                break
        
        if t:
            ans.extend(reversed(t))  # Append the reversed t to ans

        return ''.join(ans)  # Join the list into a string

    def fun(self, s: str) -> list:
        st = []
        st.append(len(s) - 1)
        
        for i in range(len(s) - 2, -1, -1):
            if s[st[-1]] < s[i]:
                continue
            st.append(i)
        
        return st        