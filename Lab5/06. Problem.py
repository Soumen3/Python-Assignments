# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills,
# country, city and address as keys for the dictionary
# I. Get the length of the student dictionary
# II. Get the value of skills and check the data type, it should be a list
# III. Modify the skills values by adding one or two skills
# IV. Get the dictionary keys as a list
# V. Get the dictionary values as a list
# VI. Change the dictionary to a list of tuples using _items()_ method
# VII. Delete one of the items in the dictionary
# VIII. Delete one of the dictionaries

student = {
	"first_name": "John",
	"last_name":"Doe",
	"gender":"male",
	"age":22,
	"marital_status":"single",
	"skills":["Python", "Java"],
	"country":"United States",
	"city":"New York",
	"address":"123 Main St"
}

# I. Get the length of the student dictionary
print(len(student))

# II. Get the value of skills and check the data type, it should be a list
skills = student["skills"]
print(type(skills))

# III. Modify the skills values by adding one or two skills
skills.append("C++")
skills.append("JavaScript")
print(skills)

# IV. Get the dictionary keys as a list
keys = list(student.keys())
print(keys)

# V. Get the dictionary values as a list
values = list(student.values())
print(values)

# VI. Change the dictionary to a list of tuples using _items()_ method
items = list(student.items())
print(items)

# VII. Delete one of the items in the dictionary
del student["address"]
print(student)

# VIII. Delete one of the dictionaries
del student

