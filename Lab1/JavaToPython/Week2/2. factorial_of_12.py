# Write a progrma to calculate factorial of 12 

def factorial():
    fact = 1
    for i in range(1, 13):
        fact *= i
    return fact
print(factorial())