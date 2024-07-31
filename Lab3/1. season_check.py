# Write a function called check-season, it takes a month parameter and returns the season:
# Autumn, Winter, Spring or Summer.

def check_season(month):
	if month in ['september', 'october', 'november']:
		return 'Autumn'
	elif month in ['december', 'january', 'february']:
		return 'Winter'
	elif month in ['march', 'april', 'may']:
		return 'Spring'
	elif month in ['june', 'july', 'august']:
		return 'Summer'
	else:
		return 'Invalid month'
	
month = input('Enter a month: ')
print(check_season(month.lower()))