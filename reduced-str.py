def reduce_string(str1):
    stack = []

    for char in str1:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    result = ''.join(stack)
    return result if result else "Empty String"


# Example usage
str1 = "aaabbccddd"

output1 = reduce_string(str1)
print(output1)