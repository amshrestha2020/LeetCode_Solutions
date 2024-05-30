Solve a given equation and return the value of 'x' in the form of a string "x=#value". The equation contains only '+', '-' operation, the variable 'x' and its coefficient. You should return "No solution" if there is no solution for the equation, or "Infinite solutions" if there are infinite solutions for the equation.

If there is exactly one solution for the equation, we ensure that the value of 'x' is an integer.

 

Example 1:

Input: equation = "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:

Input: equation = "x=x"
Output: "Infinite solutions"
Example 3:

Input: equation = "2x=x"
Output: "x=0"
 

Constraints:

3 <= equation.length <= 1000
equation has exactly one '='.
equation consists of integers with an absolute value in the range [0, 100] without any leading zeros, and the variable 'x'.





class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse_side(side):
            # Function to parse a side and return total x coefficient and constant
            terms = side.replace('-', '+-').split('+')
            x_coeff = 0
            constant = 0
            for term in terms:
                if term == '':  # Skip empty strings from split
                    continue
                if 'x' in term:
                    if term == 'x':
                        x_coeff += 1
                    elif term == '-x':
                        x_coeff -= 1
                    else:
                        x_coeff += int(term.replace('x', ''))
                else:
                    constant += int(term)
            return x_coeff, constant
        
        left, right = equation.split('=')
        left_x, left_const = parse_side(left)
        right_x, right_const = parse_side(right)
        
        total_x = left_x - right_x
        total_const = right_const - left_const
        
        if total_x == 0:
            if total_const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            x_value = total_const // total_x
            return f"x={x_value}"

# Example usage:
sol = Solution()
print(sol.solveEquation("x+5-3+x=6+x-2"))  # Output: "x=2"
print(sol.solveEquation("x=x"))            # Output: "Infinite solutions"
print(sol.solveEquation("2x=x"))           # Output: "x=0"
