items = [
    ('shampoo', 458),
    ('phone', 458),
    ('notebook', 457)
]


#to create a sorted list using filter or map
#steps:
# iterate through the list of items and get the prices in to a different list called price list
# iterate through the price list and for each price you see get the item from the items list and add to a new list called sorted list
# print the sorted list

price_list = []
for item in items:
    price_list.append(item[1])
price_list.sort()

sorted_list = []
for price in price_list:
    temp_item = list(filter(lambda item: item[1] == price, items))
    ind = items.index(temp_item[0])
    items.pop(ind)
    sorted_list.append(temp_item[0])
print(sorted_list)


# filtered_results = []
# filtered_results.append(items[1][1])
# # print(f"Price of shampoo is: {items[1][1]}")
# print(filtered_results)

# x = list(filter(lambda item: item[1] >= 1000, items))
# print(x)

# y = list(map(lambda item: item[1], items))
# print(y)

items = [
    ('shampoo', 458),
    ('phone', 458),
    ('notebook', 459)
]

def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)


#using lambda function --> gets the same effect as above

items.sort(key=lambda item: item[1])
print(items)