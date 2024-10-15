# Fundamentals of Python
       # Basics



# What is Data?
   #It's a collection of Facts
   #Ex- 0 1 ,13.4, My name is Satya
# How to store data ?
    # Variables
    # Data/Values can be stored in Storage spaces called Variables.
    # Ex - Student = "Satya"
    # Variable is Student
    # Ex- a=10    b=20
    # Multiple operation on the variables a+b a-b a*b a/b ....


# Lecture 2
     # Decision-Making Statements
     # Ex - If It's raining : sit inside else Go out football
     # EX -2 if marks >70 : Get Ice-cream else Give practice Test

# if...else Pseudo code
#         if(condition){
#         statements to be executed ....
#        }
#         else{
#         Statements to be executed ....
#      }

# Lecture 3
      # Looping Statements
           # There are used to repeat a task multiple times
           # Ex- keep filling this bucket with a mug of water while it is not full
           # Ex - Get your salary credited at the end of each month

# while Loop Pseudo code
#         while(True){
#         keep executing statements.....
#         }

# Lecture 4
       #Functions in programing
            # Functions in real life ex- eating   , Running  , Cycling
            # Functions in programing world
       # Function is a block of code which performs a specific task
           # Ex -
            # Deposit ----> Function to Deposit money
            # Withdraw ----> Function to withdraw money
            # Balance -----> Function to check balance

# Lecture 5
      # Oops Concept
        # Objects - You surrounded with objects Ex - phone,bike ect
        # Class - It is template / blue-print for real world entities
        # Ex - Phone Properties - Color , cost Battery life    Behaviour - Make calls,Watch videos,Play Games
        # Objects - are specific instance of a class
        # Ex- Mobile phone is class and the brand of phone are objects.

# Lecture 6
     # Algorithmic Approach to solve a Problem
         # 1. Step-by-Step approach
         # 2. Algorithmic approach -
         # What is Algorithm ? Step-by-Step approach to solve a problem is known as algorithm.

# Lecture 7
        # Intro Python
            # Introduction to Python
            # - Cross-Platform Compatible
            # - Large Standard Library
            # - Free & Open-Source
            # - Object-Oriented

# Lecture 8
       # Variables and Data-types in Python
               # Variables in python
                      # ex - employee_name = 'Satya'
               #Data-types in Python
                      # Ex - int , float , Boolean , String
                      # Ex- int = 12

# Lecture 9
      # Operators in Python
               # Arithmetic Operator (+,-,*,/)
               # Relational Operator (>,<,==,!=)
               # Logical  Operator (&,|)
# Ex -  Arithmatic
# a= 10
# b=20
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# Ex - Relational
# a=10
# b=20
# print(a>b)
# print(a<b)
# print(a==b)
# print(a!=b)

# Ex - Logical Operator
# a=True
# b=False
# # print(a&b)
# # print(b&a)
# # print(b&b)
# # print(a&a)
# print(a|b)
# print(a|a)
# print(b|b)

# Lecture 10
     # Tokens in Python
        # - Smallest meaningful Components in a Program
        # EX - Keywords, Identifiers, Literals, Operators
        # Keywords - Are Special reserved words

        # Keywords are -

        # False    class        Finally     Is         Return
        # None     continue     For         Lambda     Try
        # True     def          From        Nonlocal   While
        # and      del          Global      Not        With
        # as       elif         if          Or         Yield

        # Identifiers - Are names used for Variables ,Functions, Or Objects
        # Rules -
              # No special character  expect_(Underscore)
              # Identifiers are case Sensitive
              # First Letter cannot be a digit

        # Python Literals - Are Constants in Python
              # Ex - a1 = "Satya" (String Literals)
              # Ex - a1 = 123 (Integer Literals)

# Lecture 11
      # Strings in Python
             # There are sequence of characters enclosed within single quotes (''), double quotes("")
             # Ex- 'Hello World'      "Hello world"
      # Extracting Individuals Characters
        # EX - my_string = "My name is Satya"
                # my_string[0]
                # O/P - 'M'
                # my_string[-1]
                # O/P - 'a'
                # my_string[3:6]
                # O/P - 'nam'

       # Finding Length of String -  len(my_string)
       # Converting String to Lower case - my_string.lower()
       # Converting String to Upper case - my_string.upper()
       # Replacing a substring - my_string.replace()
       # Number of occurrences of substring - new_string.count() ex - new_string = "hello hello world"    new_string.count("hello")  O/P - 2
       # Finding the index of substring - s1 ='This is sparta!!!'
                                        # s1.find('sparta')
                                        # O/P - 8
       # Splitting a string - fruits = 'I like apples,mangoes,bananas'
                            # fruit.split(',')
                            # O/P - ['I like apples','mangoes','bananas']

# Lecture 12
        #  Data-Structures in Python
                    # Tuple
                    # List
                    # Dictionary
                    # Set

       # Tuple - It is an ordered collection of elements enclosed within()
               # - these are immutable
               # EX- tup1 = (1,'a',True)
          # Extracting Individual Elements -
                      #  tup1 = (1,"a",True,2,"b",False)
                      #  tup[0]
                      # O/P - 1
                      #   tup[-1]
                      # O/P - False
                      #   tup[1:4]
                      # O/P - ('a',True,2)
         # Modifying a Tuple -
                  # tup1[2] = "hello"
                  # O/P - TypeError: 'tuple' object does not support item assignment
         # Finding Length of Tuple -
                  # tup1 = (1,"a",True,2,"b",False)
                  # len(tup1)
                  # O/P - 6
         # Concatenating Tuples -
                  # tup1 = (1,2,3)
                  # tup2 = (4,5,6)
                  # tup1+tup2
                  # O/P - (1,2,3,4,5,6)
         # Repeating Tuple Elements -
                  # tup1 = ('sparta',300)
                  # tup1*3
                  # ('sparta',300,'sparta',300,'sparta',300)
         # Repeating and Concatenating -
                  # tup1 = ('sparta',300)
                  # tup2 = ('4,5,6')
                  # tup*3+ tup2
                  # O/P - ('sparta',300,'sparta',300,'sparta',300,4,5,6)
         # Minimum Value -
                  # tup1 = (1,2,3,4,5)
                  # min(tup1)
                  # O/P - 1
         # Maximum Value -
                  # tup1 = (1,2,3,4,5)
                  # max(tup1)
                  # O/P - 5

# Lecture 13
        # List in Python
              # It is an ordered collection of elements enclosed within []
              # List are mutable
              # Ex - l1 = [1,'a',True]
              # Ex - l1 = [1,"sparta",3.14,True]
        # Extracting individual elements
              # l1 = [1,"a",2,"b",3,"c"]
              # l1[1]
              # O/P - 'a'

              # l1 = [1,"a",2,"b",3,"c"]
              # l1[2:5]
              # O/P - [2,'b',3]
       # Modifying a List
           # Changing the element at 0th index
                # l1 = [1,"a",2,"b",3,"c"]
                # l1[0] = 100
                # l1
                # O/P - [100,'a',2,'b',3,'c']
           # Popping the last element
                # l1 = [1,"a",2,"b",3,"c"]
                # l1.pop()
                # l1
                # O/P - [1,'a',2,'b',3]
           # Appending a new element
                # l1 = [1,"a",2,"b",3,"c"]
                # l1.append("sparta")
                # l1
                # O/P - [1,'a',2,'b',3,'c','sparta']
           # Reversing elements of a list
                # l1 = [1,"a",2,"b",3,"c"]
                # l1.reverse()
                # l1
                # O/P - ['c',3,'b',2,'a',1]
           # Sorting a list
                # l1 = ["mango","banana","guava","apple"]
                # l1.sort()
                # l1
                # O/P - ['apple','banana','guava','mango']
           # Inserting element at a Specific index
                # l1 = [1,"a",2,"b",3,"c"]
                # l1.insert(1,"sparta")
                # l1
                # O/P - [1,'sparta','a',2,'b',3,'c']
           # Concatenating Lists
                # l1 = [1,2,3]
                # l2 = ["a","b","c"]
                # l1+l2
                # O/P - [1,2,3,'a','b','c']
           # Repeating elements
                # l1 = [1,"a",True]
                # l1*3
                # O/P - [1,'a',True,1,'a',True,1,'a',True]

# Lecture 14
       # Dictionary in Python
             # It is an unordered collection of key-value pairs enclosed with {}
             # It is Mutable
             # Ex - fruit{"Apple":10,"Orange":20}
             # In the example Apple is the key and 10 is the value ....
       # Extracting Keys
             # fruit = {"Apple":10,"Orange":20,"Banana":30,"Guava":40}
             # fruit.keys()
             # O/P - dict_keys(['Apple','Orange','Banana','Guava'])
       # Extracting Values
             # fruit = {"Apple":10,"Orange":20,"Banana":30,"Guava":40}
             # fruit.values()
             # dict_values([10,20,30,40])
       # Adding a new element
             # fruit = {"Apple":10,"Orange":20,"Banana":30,"Guava":40}
             # fruit["Mango"]=50
             # fruit
             # O/P - {'Apple':10,'Orange':20,'Banana':30,'Guava':40,'Mango':50}
       # Changing an existing element
             # fruit = {"Apple":10,"Orange":20,"Banana":30,"Guava":40,"Mango":50}
             # fruit["Apple"]= 100
             # fruit
             # O/P - {'Apple':100,'Orange':20,'Banana':30,'Guava':40,'Mango':50}
       # Update one dictionary's  elements with another
             # fruit1 = {"Apple":10,"Orange":20}
             # fruit2 = {"Banana":30,"Guava":40}
             # fruit1.update(fruit2)
             # fruit1
             # O/P - {'Apple':10,'Orange':20,'Banana':30,'Guava':40}
       # Popping an element
             # fruit = {"Apple":10,"Orange":20,"Banana":30,"Guava":40}
             # fruit.pop("Orange")
             # fruit
             # O/P - {'Apple':10,'Banana':30,'Guava':40}

# Lecture 15
       # Set in Python
            # It is an unordered and un-indexed collection of elements enclosed with {}
            # Duplicates are not allow in Set
            # Ex - s1 = {1,"a",True}
       # Adding a new element
            # s1 = {1,"a",True,2,"b",False}
            # s1.add("Hello")
            # s1
            # O/P - {1,2,false,'Hello','a','b'}
       # Updating multiple elements
            # s1 = {1,"a",True,2,"b",false}
            # s1.update([10,20,30])
            # s1
            # O/P - {1,10,2,20,30,false,'a','b'}
       # Removing an element
            # s1 = {1,"a",True,2,"b",false}
            # s1.remove("b")
            # s1
            # O/P - {1,2,false,'a'}
      # Set Functions
           # Union of two sets
                # s1 = {1,2,3}
                # s2 = {"a","b',"c"}
                # s1.union(s2)
                # O/P - {1,2,3,'a','b','c'}
           # Intersection of two sets
                # s1 = {1,2,3,4,5,6}
                # s2 = {5,6,7,8,9}
                # s1,intersection(s2)
                # O/P - {5,6}
                
# Lecture 16
     # If Statement in Python
            # let a=10
                # b=20
                # then
                # if a>b :
                    # print (' a is grater than b')

# Lecture 17
     # Looping Statements in Python
            # Looping Statements are used to repeat a task multiple times
            # EX - keep filing this bucket with a mug of water while it is not full
            # Syntax - while condition:
                             # Execute Statements
 # Print first 10 number using while loop
 # i=1
 # While i<=10:
 #      print(i)
 #      i=i+1

# Print 2 table using while loop
# i =1
# n=2
# while i<=10:
#    print(n , "*" , i , "=" ,n*i)
#    i=i+1

# While loop in list
#l1 = [1,2,3,4,5]
#i=0
#while i< len(l1):
#    l1[i] = l1[i]+100
#    i= i+1
#print(l1)

             # For loop
                  # It is used to iterate over a sequence (tuple, list, dictionary ...)
                  # Syntax - for val in sequence:
                                    # Body of for

# List using for loop
#l1 = ["apple","banana","Orange"]
#for i in l1:
#    print(i)

# Nested for loop

#l1 = ["Orange","blue","green"]
#l2 = ["book","chair","phone"]
#for i in l1:
#    for j in l2:
#        print(i,j)

# Lecture 18
       # Basic Problem in Python

# Lecture 19
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
#def hello():
#    print("Hello World")
#hello()

# function with parameter
#def add10(x):

 #   return x+10
#print(add10(10))

# even or odd
#def even_odd(x):
#    if x%2 == 0:
 #       print(x , "is even")
  #  else:
   #     print(x , "is odd ")
#even_odd(5)

# Lambda function
#g = lambda x : x*x*x
#print(g(7))

# Lambda function with filter
#li = [5,7,22,97,54,62,77,23,73,61]
#final_list = list(map(lambda x:(x%2 != 0),li))
#print(final_list)
# Lambda functions with map
#li = [5,7,22,97,54,62,77,23,73,61]
#final_list = list (map ( lambda x : x*2 ,li))
#print(final_list)

# from funtools import reduce
#li = [5,8,10,20,50,100]
#add = reduce((lambda x, y : x + y), li)
#print(add)







