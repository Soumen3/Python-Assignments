# Write a program to print fibonacci series

def fibo(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a+b
    
term = int(input("Enter the number of terms: "))
fibo(term)
           