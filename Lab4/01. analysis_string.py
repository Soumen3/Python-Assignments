# Write a program to enter a string. Calculate the length of the string. Find the substring country.
# Count the occurences of each word in the given sentence.
# If the String as input is India is my motherland. I love my country. Capital of India is New Delhi.

def analysis_str(string):
    length = len(string)

    country_count=string.count("country")
    words = string.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    return length, country_count, word_counts

string = "India is my motherland. I love my country. Capital of India is New Delhi."
length, country_count, word_counts = analysis_str(string)
print(f"Length of the string: {length}")
print(f"Count of 'country': {country_count}")
print("Word counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")