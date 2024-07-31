# Write a Python program to print the first 6 terms of a geometric sequence starting with 2 and having a common ratio of 3.

def print_geometric_sequence(start, ratio, terms):
    """
    Prints the first `terms` terms of a geometric sequence starting with `start`
    and having a common ratio of `ratio`.
    """
    current = start
    for _ in range(terms):
        print(current, end=" ")
        current *= ratio
    

print_geometric_sequence(2, 3, 6)