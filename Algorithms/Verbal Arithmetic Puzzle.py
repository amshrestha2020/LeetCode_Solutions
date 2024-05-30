Given an equation, represented by words on the left side and the result on the right side.

You need to check if the equation is solvable under the following rules:

Each character is decoded as one digit (0 - 9).
No two characters can map to the same digit.
Each words[i] and result are decoded as one number without leading zeros.
Sum of numbers on the left side (words) will equal to the number on the right side (result).
Return true if the equation is solvable, otherwise return false.

 

Example 1:

Input: words = ["SEND","MORE"], result = "MONEY"
Output: true
Explanation: Map 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
Such that: "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652
Example 2:

Input: words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
Output: true
Explanation: Map 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1, 'W'->'3', 'Y'->4
Such that: "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 = 138214
Example 3:

Input: words = ["LEET","CODE"], result = "POINT"
Output: false
Explanation: There is no possible mapping to satisfy the equation, so we return false.
Note that two different characters cannot map to the same digit.
 

Constraints:

2 <= words.length <= 5
1 <= words[i].length, result.length <= 7
words[i], result contain only uppercase English letters.
The number of different characters used in the expression is at most 10.





class Solution:
    def isAnyMapping(self, words, row, col, bal, letToDig, digToLet, totalRows, totalCols):
        # If traversed all columns.
        if col == totalCols:
            return bal == 0

        # At the end of a particular column.
        if row == totalRows:
            return bal % 10 == 0 and self.isAnyMapping(words, 0, col + 1, bal // 10, letToDig, digToLet, totalRows, totalCols)

        w = words[row]

        # If the current string 'W' has no character in the ('COL')th index.
        if col >= len(w):
            return self.isAnyMapping(words, row + 1, col, bal, letToDig, digToLet, totalRows, totalCols)

        # Take the current character in the variable letter.
        letter = w[len(w) - 1 - col]

        # Create a variable 'SIGN' to check whether we have to add it or subtract it.
        sign = 1 if row < totalRows - 1 else -1

        # If we have a prior valid mapping, then use that mapping.
        # The second condition is for the leading zeros.
        if letter in letToDig and (letToDig[letter] != 0 or (letToDig[letter] == 0 and len(w) == 1) or col != len(w) - 1):
            return self.isAnyMapping(words, row + 1, col, bal + sign * letToDig[letter], letToDig, digToLet, totalRows, totalCols)
        else:
            # Choose a new mapping.
            for i in range(10):
                # If 'i'th mapping is valid then select it.
                if digToLet[i] == '-' and (i != 0 or (i == 0 and len(w) == 1) or col != len(w) - 1):
                    digToLet[i] = letter
                    letToDig[letter] = i

                    # Call the function again with the new mapping.
                    x = self.isAnyMapping(words, row + 1, col, bal + sign * letToDig[letter], letToDig, digToLet, totalRows, totalCols)
                    if x:
                        return True

                    # Unselect the mapping.
                    digToLet[i] = '-'
                    if letter in letToDig:
                        del letToDig[letter]

        # If nothing is correct then just return false.
        return False

    def isSolvable(self, words, result):
        # Add the string 'RESULT' in the vector 'WORDS'.
        words.append(result)

        totalRows = len(words)
        totalCols = max(len(word) for word in words)

        # Create a HashMap for the letter to digit mapping.
        letToDig = {}

        # Create a vector for the digit to letter mapping.
        digToLet = ['-'] * 10

        return self.isAnyMapping(words, 0, 0, 0, letToDig, digToLet, totalRows, totalCols)
