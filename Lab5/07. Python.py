# 7.Create a person dictionary.
# person={
# 'first_name': 'Asabeneh',
# 'last_name': 'Yetayeh',
# 'age': 250,
# 'country': 'Finland',
# 'is_marred': True,
# 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
# 'address': {
# 'street': 'Space street',
# 'zipcode': '02210'
# }
# }
# I. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# II. Check if the person dictionary has skills key, if so check if the person has 'Python' skill and
# print out the result.
# III. If a person skills has only JavaScript and React, print('He is a front end developer'), if the
# person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person
# skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown
# title') - for more accurate results more conditions can be nested!
# IV. If the person is married and if he lives in Finland, print the information in the following
# format:

# ```py
# Asabeneh Yetayeh lives in Finland. He is married.
# ``



person={
	'first_name': 'Asabeneh',
	'last_name': 'Yetayeh',
	'age': 250,
	'country': 'Finland',
	'is_marred': True,
	'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
	'address': {
		'street': 'Space street',
		'zipcode': '02210'
	},
}

# I. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
	skills = person['skills']
	middle = len(skills) // 2
	print(skills[middle])

# II. Check if the person dictionary has skills key, if so check if the person has 'Python' skill and
# print out the result.
if 'skills' in person:
	skills = person['skills']
	if 'Python' in skills:
		print("Python is in skills")
	else:
		print("Python is not in skills")

# III. If a person skills has only JavaScript and React, print('He is a front end developer'), if the
# person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person
# skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown
# title') - for more accurate results more conditions can be nested!
if 'skills' in person:
	skills = person['skills']
	if skills == ['JavaScript', 'React']:
		print("He is a front end developer")
	elif set(skills) == set(['Node', 'Python', 'MongoDB']):
		print("He is a backend developer")
	elif set(skills) == set(['React', 'Node', 'MongoDB']):
		print("He is a fullstack developer")
	else:
		print("Unknown title")

# IV. If the person is married and if he lives in Finland, print the information in the following
# format:
if person['is_marred'] and person['country'] == 'Finland':
	print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")

