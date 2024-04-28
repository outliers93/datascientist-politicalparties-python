"""def fibonacci(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(1))"""

"""def countdown(n):
    print(n)
    if n > 0:
        print(f"chupalo {n}")
        countdown(n - 1)
        print(f"chupalo 2 {n}")
        print(n-1)


countdown(10)"""

"""def is_palindrome(word):
    #Return True if word is a palindrome, False if not.
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome(word[1:-1])"""