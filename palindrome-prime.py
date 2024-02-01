def is_prime(num):
    """Checks if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    """Checks if a number is a palindrome."""
    sum = 0
    k = num
    while k > 0:
        rem = k % 10
        k = k // 10  # Corrected this line to use integer division
        sum = sum * 10 + rem
    if sum == num:
        return num

def find_palindromic_primes(start, end):
    """Finds palindromic prime numbers between a range."""
    palindromic_primes = []
    for num in range(start, end + 1):
        if is_palindrome(num) and is_prime(num):
            palindromic_primes.append(num)
    return palindromic_primes

# Example usage
start = int(input("Enter starting position: "))
end = int(input("Enter ending position: "))
palindromic_primes = find_palindromic_primes(start, end)

if palindromic_primes:
    print("Palindromic prime numbers between", start, "and", end, ":", palindromic_primes)
else:
    print("No palindromic prime numbers found in the given range.")

