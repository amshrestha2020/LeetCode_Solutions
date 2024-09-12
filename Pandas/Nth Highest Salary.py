Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+



import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Check if N is a positive integer
    if not isinstance(N, int) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    # Sort the salaries in descending order and drop duplicates
    sorted_salaries = employee['salary'].sort_values(ascending=False).drop_duplicates()
    
    # If N exceeds the number of distinct salaries, return null
    if N > len(sorted_salaries):
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    # Otherwise, return the nth highest salary
    nth_highest = sorted_salaries.iloc[N - 1]
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_highest]})
