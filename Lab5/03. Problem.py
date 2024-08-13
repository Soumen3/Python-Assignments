# 3.Create fruits, vegetables and animal products tuples.
# I. Join the three tuples and assign it to a variable called food_stuff_tp.
# II. Change the about food_stuff_tp tuple to a food_stuff_lt list
# III. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# IV. Slice out the first three items and the last three items from food_staff_lt list
# V. Delete the food_staff_tp tuple completely

fruits = ("apple", "banana", "cherry")
vegetables = ("artichoke", "broccoli", "carrot")
animal_products = ("beef", "chicken", "duck")

# I. Join the three tuples and assign it to a variable called food_stuff_tp.
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# II. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# III. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = len(food_stuff_tp) // 2
print(food_stuff_tp[middle])

# IV. Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

# V. Delete the food_staff_tp tuple completely
del food_stuff_tp
