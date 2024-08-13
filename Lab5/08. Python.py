# Print the season name of the year based on the month number using a dictionary.

month = int(input('Enter the month number: '))

seasons = {
	1: 'Winter',
	2: 'Winter',
	3: 'Spring',
	4: 'Spring',
	5: 'Spring',
	6: 'Summer',
	7: 'Summer',
	8: 'Summer',
	9: 'Fall',
	10: 'Fall',
	11: 'Fall',
	12: 'Winter'
}

print(seasons[month])

