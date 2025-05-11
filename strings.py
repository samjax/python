chars = list('aniiissshkkkkaaaa')
print(set(chars))

first_set = {1,2,3,4,5}
second_set = {1,2,3,4,5,6,7,8}


print(f"Union of the sets: {first_set | second_set}")

print(f"Intersection of the sets: {first_set & second_set}")

print(f"Difference between sets: {first_set - second_set}")

print(f"Difference between sets: {second_set - first_set}")

#symmetric difference --> they are in one set but not in the other

s1 = {1,2,3,4}
s2 = {1,2,3,4}

print(f"Symmetric difference is : {s1 ^ s2}")

s1 = {1,2,3,4,5}
s2 = {1,2,3,4,}

print(f"Symmetric difference is : {s1 ^ s2}")

set5 = set([])
print(set5)