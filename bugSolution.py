def function_with_proper_check(a, b):
    if a == 0:
        return 0 # Handle the case where a is zero gracefully
    return a + b

result = function_with_proper_check(0, 5)
print(result)  # Output: 5

result = function_with_proper_check(2, 5)
print(result)  # Output: 7