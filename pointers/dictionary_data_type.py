# works in different way than integers

dict1 = {
    'value':11 
}

dict2 = dict1

print("Before dic2 value is updated:")
print("dic1 =", dict1)
print("dic2 =", dict2)
# Before dic2 value is updated:
# dic1 = {'value': 11}
# dic2 = {'value': 11}

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
# dict1 points to: 4351105664
# dict2 points to: 4351105664

dict2['value'] = 22

print("\nAfter dict2 value is updated:")
print("dic1 =", dict1)
print("dic2 =", dict2)
# After dict2 value is updated:
# dic1 = {'value': 22}
# dic2 = {'value': 22}

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
# dict1 points to: 4351105664
# dict2 points to: 4351105664

dict3 = {
    'value':33
}
dict2 = dict3

print("\nAfter dict1 point is updated:")
print("dic3 =", dict3)
print("dic2 =", dict2)
# After dict1 point is updated:
# dic3 = {'value': 33}
# dic2 = {'value': 33}

print("\ndict3 points to:", id(dict3))
print("dict2 points to:", id(dict2))
# dict3 points to: 4378009344
# dict2 points to: 4378009344

dict1 = dict2

print("\nAfter dict1 point is updated:")
print("dic3 =", dict3)
print("dic2 =", dict2)
print("dic1 =", dict1)
# After dict1 point is updated:
# dic3 = {'value': 33}
# dic2 = {'value': 33}
# dic1 = {'value': 33}

print("\ndict3 points to:", id(dict3))
print("dict2 points to:", id(dict2))
print("dict1 points to:", id(dict1))
# dict3 points to: 4378009344
# dict2 points to: 4378009344
# dict1 points to: 4378009344

