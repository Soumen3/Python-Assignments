# Write a program to check wheather a number is buzz number or not 

def is_buzz_num(num):
    """
    Checks if a number is a buzz number
    A buzz number is a number that is divisible by 7 or ends with 7
    """
    if num % 7 == 0 or num % 10 == 7:
        return True
    else:
        return False


num = int(input("Enter a number: "))
if is_buzz_num(num):
    print(f"{num} is a buzz number")
else:
    print(f"{num} is not a buzz number")