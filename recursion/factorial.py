# 4!
# 4 * 3!
#     3 * 2!
#         2 * 1!
#             1 (Base case)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(4))
# 24

# look at run and debug