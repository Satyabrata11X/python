# Factorial of a number
num = int(input("Enter a number : "))
if num < 0 :
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    num = int(num)
    factorial =1
    for i in range (1, num+1):
        factorial *=i
    print(f"The factorial is {num}is {factorial}")

