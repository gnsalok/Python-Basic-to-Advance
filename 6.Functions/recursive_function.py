#Working with Recursive Function
'''
It is actually used to break down the problem into sub-problem and solve it..
When a function calls itself then that called the recursive function and that 
situation is called as Recursion.
'''

# Just try to print factorial of number using Recursion.

def factorial(value):
    if value<=1:
        return value
    else:
        fact=value*factorial(value-1)
        return fact
    
value = int(input("Enter you number to find factorial? : \t "))
factorialResult=factorial(value)
print("Factorial is :",factorialResult)