items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 11)
]

# simple sorting
items.sort(key=lambda item: item[1])
print(items)

#Map and filter
prices = list(map(lambda item: items[1], items))
print(prices)



expensive_items = list(filter(lambda item: item[1] >= 10, items))
print(expensive_items)
