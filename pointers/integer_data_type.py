num1 = 11
num2 = num1

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)
# Before num2 value is updated:
# num1 = 11
# num2 = 11

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))
# num1 points to: 4401709616
# num2 points to: 4401709616

num2 = 22

print("\nAfter num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)
# After num2 value is updated:
# num1 = 11
# num2 = 22

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))
# num1 points to: 4401709616
# num2 points to: 4401709968

