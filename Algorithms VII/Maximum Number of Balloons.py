Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.







class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Count the frequency of each character in the text
        count = {}
        for char in text:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        
        # The word "balloon" contains 'b', 'a', 'l', 'o', 'n'. 
        # 'l' and 'o' appear twice in "balloon", so we divide their counts by 2.
        # Then, we find the minimum count among these characters, which gives the maximum number of "balloon"s we can form.
        return min(count.get('b', 0), count.get('a', 0), count.get('l', 0) // 2, count.get('o', 0) // 2, count.get('n', 0))

