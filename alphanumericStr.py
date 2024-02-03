def has_letter_and_number(input_str):
    has_letter = any(char.isalpha() for char in input_str)
    has_number = any(char.isdigit() for char in input_str)
    return has_letter and has_number

# Example usage
input_str1 = input("enter string ")


output1 = has_letter_and_number(input_str1)
print(output1)
