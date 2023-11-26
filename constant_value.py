
def highest_consonant_value(s):
    s = s.lower()
    # Function to calculate the value of a substring
    def substring_value(sub):
        return sum(ord(char) - ord('a') + 1 for char in sub)
    
    max_value = 0  # Variable to store the highest value

    # Iterate through the string
    current_substring = ""
    for char in s:
        # Check if the character is a consonant
        if char not in "aeiou":
            current_substring += char
        else:
            # Calculate the value of the current consonant substring
            current_value = substring_value(current_substring)
            
            # Update the maximum value if the current value is higher
            max_value = max(max_value, current_value)
           
            # Reset the current substring for the next consonant substring
            current_substring = ""
    
    # Check the value of the last consonant substring
    max_value = max(max_value, substring_value(current_substring))
    
    return max_value

# Example usage
input_string = "Strength"
result = highest_consonant_value(input_string)
print(f"max result: {result}")  
