#comment in separate line
# Hello dear learner !!!!!!
x=3
x = x*3 #multiply by 3
print(x)


#variables in python
numofLaptops = 3
ownerName = "Satya"
print("Number of Laptops = ",numofLaptops)
print("owner Name = ",ownerName)
#Variable name begins with letter or underscore character
#Alpha-numeric and underscores are allowed in the rest of name
#variable names are case-sensitive


#Arithemetic Operation
a=10
b=6
print(a + b) #Addition
print(a - b) #Subtraction
print(a * b) #Multiplication
print(a / b) #Division
print(a % b) #Modulus
print(a ** b)  #Exponentiation


#Logical Operators in Python
a=5
b=8
#will return true if Both Conditions true
print(3 < a < 7)
#will return true if any one condition is true
print(a > 6 or b < 7)
#True if given condition is false
print(not (a > 3))

#User Input
city = input("Where do you live?\n")
print("\n The city you live is : "+ city)

#NumPy- It is an easy -to - use array processing package in python.Used for creation of multidimensional array objects.

#Pandas-There are used for data manipulation - mostly for data preparation ,modeling and analysis in python.

#Data Structures in Pandas
     # It  supports the usage of series and DataFrames.
         # Series is used when requirement is of one-dimensional only.
         # DataFrames are used when working with two-dimensional data.
# DataFrames can be created using lists or dictionaries.

#Creating a 1D and 2D array using NumPy

# >num1d = [1,2,3,4,5]
# >num2d = [1,2,3,4,5],["hello","learners"]
# >num1d = np.array(num1d)
# >num2d = np.array(num2d)

#The eye()function in NumPy

    #printing a matrix with 1 across diagonal and 0 everywhere else:
         # >eye_mat = np.eye(4)
         # >print("One across diagonals: \n\n",eye_mat)

#Priniting random numbers using NumPy

#Easily done using randint()function in NumPy
    # >random_print = np.random.randint (0,100,10)
    # >print("Random numbers from 0 to 100 printing 10:\n\n",random_print)

#Printing the last element in an array
       #Last element can be printing by accessing the -1 index.
             # >names = np.array(["Satya","Lucky","Vicky","Sai"])
             # >print("\n Last element of the array is :",names[-1])

#Printing specific index in a multidimensional array
     # Print the 3rd element of the 2nd row in a 3D array :
          # >numbers = np.array([[5,8,3],[3,1,2],[5,7,8]])
          # >print("second Row,third element :",numbers[1][2])

#Insering elements into an array and reshaping it
       # with 5X5 array, let us insert numbers 1 to 25 :
              # >numbers = np.arrange (1,26).reshape(5,5)
              # >print("Numbers inserted \n\n",numbers)

#Replacing all the even numbers with 10!
        # >numbers = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
        # >numbers[numbers % 2 == 0] = 10
        # >print(numbers)

#Converting a 1D array into a 2D array
        # This can be easily done using the reshape
        #Example:
               # >numbers = np.arrange(10)
               # >print(numbers)
               # >print("Reshaped into 2 dimensions:\n")
               # >numbers.reshaped(2,-1)

# Printing common elements from two NumPy arrays
           # It can be easily done using interest1d() as shown below :
                 # >x = np.array done interest1d() as shown below :
                 # >y = np.array([36,85,10,2,7,30])
                 # >np.interest1d(x,y)

#Print custom range values in an array
         # Numbers from 3 to 6 are printed using a logical operation :
                  # >numbers = np.arrange(10)
                  # print(numbers)
                  # numbers[(numbers >= 3)&(numbers <= 6)]

# Creation of series using dictionaries in Pandas
          #This can be easily achieved with the following piece of code :
                # >sample_dict = {"x":1,"y":2,"z":3}
                # >the_series = pd.Series(sample_dict)
                # >print(the_series)