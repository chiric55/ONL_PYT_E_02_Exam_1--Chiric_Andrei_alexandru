def check_character(input_string, target_character):
    return sum(1 for char in input_string if char == target_character)

result = check_character('Order of the Phoenix', 'o')
print(result)