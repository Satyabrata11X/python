# Functions in Python
            # Function is a block of code which performs a special task
            # Ex -
                 # Deposit --> Function to deposit money
                 # Withdraw --> Function to withdraw money
                 # Bala ce ---> Function to check balance

            # Syntax -
                    # Normal function Syntax -
                            # def function_name :
                                  # Execute Statements

                    # Lambda Function Syntax -
                            # lambda arguments : expression

# Ex - create a hello function
from functools import reduce


def hello():
    print("Hello World")
hello()

# function with parameter
def add10(x):

    return x+10
print(add10(10))

# even or odd
def even_odd(x):
    if x%2 == 0:
        print(x , "is even")
    else:
        print(x , "is odd ")
even_odd(5)

# Lambda function
g = lambda x : x*x*x
print(g(7))

# Lambda function with filter
li = [5,7,22,97,54,62,77,23,73,61]
final_list = list(map(lambda x:(x%2 != 0),li))
print(final_list)

# Lambda functions with map
li = [5,7,22,97,54,62,77,23,73,61]
final_list = list (map ( lambda x : x*2 ,li))
print(final_list)

# from funtools import reduce
li = [5,8,10,20,50,100]
add = reduce((lambda x, y : x + y), li)
print(add)
