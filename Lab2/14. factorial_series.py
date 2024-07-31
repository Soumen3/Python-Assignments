# Print the series upto N terms: 1,2,6,24,120,720 …

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    
n = int(input("Enter the number of terms: "))
for i in range(n):
    print(factorial(i+1), end=", ")