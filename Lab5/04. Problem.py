# Create a set given below
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# A = {19, 22, 24, 20, 25, 26}
# B = {19, 22, 20, 25, 26, 24, 28, 27}
# age = [22, 19, 24, 25, 26, 24, 25, 24]
# I. Find the length of the set it_companies
# II. Add 'Twitter' to it_companies
# III. Insert multiple IT companies at once to the set it_companies
# IV. Remove one of the companies from the set it_companies
# V. What is the difference between remove and discard


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# I. Find the length of the set it_companies
print(len(it_companies))

# II. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# III. Insert multiple IT companies at once to the set it_companies
it_companies.update(['LinkedIn', 'Instagram', 'Snapchat'])
print(it_companies)

# IV. Remove one of the companies from the set it_companies
it_companies.remove('LinkedIn')
print(it_companies)

# V. What is the difference between remove and discard
# remove raises an error if the element is not present in the set
# discard does not raise an error if the element is not present in the set


# From the above sets A and B
# I. Join A and B
# II. Find A intersection B
# III. Is A subset of B
# IV. Are A and B disjoint sets
# V. Join A with B and B with A
# VI. What is the symmetric difference between A and B
# VII. Delete the sets completely

# I. Join A and B
print(A.union(B))

# II. Find A intersection B
print(A.intersection(B))

# III. Is A subset of B
print(A.issubset(B))

# IV. Are A and B disjoint sets
print(A.isdisjoint(B))

# V. Join A with B and B with A
print(A.union(B))

# VI. What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# VII. Delete the sets completely
del A
del B
