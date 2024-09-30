You are given an m x n matrix board, representing the current state of a crossword puzzle. The crossword contains lowercase English letters (from solved words), ' ' to represent any empty cells, and '#' to represent any blocked cells.

A word can be placed horizontally (left to right or right to left) or vertically (top to bottom or bottom to top) in the board if:

It does not occupy a cell containing the character '#'.
The cell each letter is placed in must either be ' ' (empty) or match the letter already on the board.
There must not be any empty cells ' ' or other lowercase letters directly left or right of the word if the word was placed horizontally.
There must not be any empty cells ' ' or other lowercase letters directly above or below the word if the word was placed vertically.
Given a string word, return true if word can be placed in board, or false otherwise.

 

Example 1:


Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"
Output: true
Explanation: The word "abc" can be placed as shown above (top to bottom).
Example 2:


Input: board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"
Output: false
Explanation: It is impossible to place the word because there will always be a space/letter above or below it.
Example 3:


Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"
Output: true
Explanation: The word "ca" can be placed as shown above (right to left). 
 

Constraints:

m == board.length
n == board[i].length
1 <= m * n <= 2 * 105
board[i][j] will be ' ', '#', or a lowercase English letter.
1 <= word.length <= max(m, n)
word will contain only lowercase English letters.





class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        from typing import List

        # Helper function to check if the word fits in a given segment of the board.
        def can_place(segment: List[str], word: str) -> bool:
            if len(segment) != len(word):
                return False
            for i in range(len(word)):
                if segment[i] != ' ' and segment[i] != word[i]:
                    return False
            return True

        # Reverse word helper
        def reverse(word: str) -> str:
            return word[::-1]

        # Check if the word can be placed horizontally
        for row in board:
            n = len(row)
            start = 0
            while start < n:
                # Find the start of a valid horizontal block
                while start < n and row[start] == '#':
                    start += 1
                end = start
                while end < n and row[end] != '#':
                    end += 1
                # Check the block of empty spaces or letters between start and end
                if can_place(row[start:end], word) or can_place(row[start:end], reverse(word)):
                    return True
                start = end

        # Check if the word can be placed vertically
        m, n = len(board), len(board[0])
        for col in range(n):
            start = 0
            while start < m:
                # Find the start of a valid vertical block
                while start < m and board[start][col] == '#':
                    start += 1
                end = start
                while end < m and board[end][col] != '#':
                    end += 1
                # Extract the vertical block from start to end
                vertical_segment = [board[row][col] for row in range(start, end)]
                # Check the block of empty spaces or letters between start and end
                if can_place(vertical_segment, word) or can_place(vertical_segment, reverse(word)):
                    return True
                start = end
        
        return False