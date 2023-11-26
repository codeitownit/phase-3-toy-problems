def is_positive(a, b, c):
    # Count the number of positive integers
    positive_count = 0
    
    # Check the positivity of each integer
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    
    # Return True if exactly two integers are positive, otherwise False
    return positive_count == 2

print(is_positive(2, 4, -3))  #True
print(is_positive(-4, 6, 8)) #True 
print(is_positive(4, -6, 9)) #True 
print(is_positive(-4, 6, 0)) #False
print(is_positive(4, 6, 10)) #False
print(is_positive(-14, -3, -4)) #False




 






