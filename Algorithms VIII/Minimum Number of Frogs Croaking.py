You are given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple "croak" are mixed.

Return the minimum number of different frogs to finish all the croaks in the given string.

A valid "croak" means a frog is printing five letters 'c', 'r', 'o', 'a', and 'k' sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of a valid "croak" return -1.

 

Example 1:

Input: croakOfFrogs = "croakcroak"
Output: 1 
Explanation: One frog yelling "croak" twice.
Example 2:

Input: croakOfFrogs = "crcoakroak"
Output: 2 
Explanation: The minimum number of frogs is two. 
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".
Example 3:

Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.
 

Constraints:

1 <= croakOfFrogs.length <= 105
croakOfFrogs is either 'c', 'r', 'o', 'a', or 'k'.





class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        count = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
        frogs = 0
        max_frogs = 0
        for ch in croakOfFrogs:
            count[ch] += 1
            if ch == 'c':
                frogs += 1
                max_frogs = max(max_frogs, frogs)
            elif ch == 'k':
                frogs -= 1
            if count['c'] < count['r'] or count['r'] < count['o'] or count['o'] < count['a'] or count['a'] < count['k']:
                return -1
        if frogs != 0:
            return -1
        return max_frogs
