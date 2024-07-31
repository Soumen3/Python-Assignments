# Write a program in Python to find the sum of digits of a number.

def sum_of_digits(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num //= 10
    return sum


num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))