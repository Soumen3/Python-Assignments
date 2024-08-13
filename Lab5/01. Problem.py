# 1.The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# I. Sort the list and find the min and max age
# II. Add the min age and the max age again to the list
# III. Find the median age (one middle item or two middle items divided by two)
# IV. Find the average age (sum of all items divided by their number )
# V. Find the range of the ages (max minus min)
# VI. Compare the value of (min - average) and (max - average), use _abs()_ method


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# I. Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f"Min age: {min_age}")
print(f"Max age: {max_age}")

# II. Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(ages)

# III. Find the median age (one middle item or two middle items divided by two)
if len(ages) % 2 == 0:
	median_age = (ages[len(ages) // 2] + ages[len(ages) // 2 - 1]) / 2
else:
	median_age = ages[len(ages) // 2]
print(f"Median age: {median_age}")

# IV. Find the average age (sum of all items divided by their number )
average_age = sum(ages) / len(ages)
print(f"Average age: {average_age}")

# V. Find the range of the ages (max minus min)
range_age = max_age - min_age
print(f"Range of ages: {range_age}")

# VI. Compare the value of (min - average) and (max - average), use _abs()_ method
if abs(min_age - average_age) > abs(max_age - average_age):
	print("Min - average is greater")
else:
	print("Max - average is greater")
