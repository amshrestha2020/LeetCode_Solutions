There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.
Return an integer array answer where answer[i] is the answer to the ith query.

 

Example 1:

ex-1
Input: s = "**|**|***|", queries = [[2,5],[5,9]]
Output: [2,3]
Explanation:
- queries[0] has two plates between candles.
- queries[1] has three plates between candles.
Example 2:

ex-2
Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
Output: [9,0,0,0,0]
Explanation:
- queries[0] has nine plates between candles.
- The other queries have zero plates between candles.
 

Constraints:

3 <= s.length <= 105
s consists of '*' and '|' characters.
1 <= queries.length <= 105
queries[i].length == 2
0 <= lefti <= righti < s.length



class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        # Step 1: Preprocess the prefix sum of plates and nearest candles
        prefix_plates = [0] * n
        left_candle = [-1] * n
        right_candle = [-1] * n
        
        # Fill the prefix_plates array
        plates_count = 0
        for i in range(n):
            if s[i] == '*':
                plates_count += 1
            prefix_plates[i] = plates_count
        
        # Fill the left_candle array (nearest candle to the left or itself)
        candle_pos = -1
        for i in range(n):
            if s[i] == '|':
                candle_pos = i
            left_candle[i] = candle_pos
        
        # Fill the right_candle array (nearest candle to the right or itself)
        candle_pos = -1
        for i in range(n-1, -1, -1):
            if s[i] == '|':
                candle_pos = i
            right_candle[i] = candle_pos
        
        # Step 2: Answer each query
        result = []
        for left, right in queries:
            # Find the nearest candle to the right of `left`
            right_bound = right_candle[left]
            # Find the nearest candle to the left of `right`
            left_bound = left_candle[right]
            
            if right_bound != -1 and left_bound != -1 and right_bound <= left_bound:
                result.append(prefix_plates[left_bound] - prefix_plates[right_bound])
            else:
                result.append(0)
        
        return result        