#How to find if a given arithmetic expression is a valid one?

#To verify if an arthematic expression is correct or not we use ast module

import ast

def is_valid_expression(expression):
    try:
        ast.parse(expression,mode = 'eval')
        return True
    except:
        return False

expressions = [
    "3 + (5 * 2)",      # Valid
    "7 / (3 - 1)",      # Valid
    "(4 + 5",           # Invalid: unbalanced parentheses
    "5 **",             # Invalid: incomplete expression
    "3 + abc",          # Invalid: undefined name
]

for expression in expressions:
    print(f"{expression} = {is_valid_expression(expression)}")
