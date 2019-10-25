# Map and filter
# custom sorting

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 11)
]

# simple sorting
items.sort(key=lambda item: item[1])

#Map and filter
prices = list(map(lambda items: item[1], items))
expensive_items = list(filter(lambda item: item[1] >= 10, items))


# #Example

# values = [2,3,4,5,6]

# def double(x):
#     return x*2

# result = list(map(double,values))
# print(result)
