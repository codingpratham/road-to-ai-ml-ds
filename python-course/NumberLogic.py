# NUMBER LOGIC (16–18)

# Check whether a number is prime.
# def is_prime(num):
#     if num <=1:
#         return False
#     for i in range (2 , num):
#         if num%i == 0:
#             return False
#     return True

# print(is_prime(9))

# Check whether a number is a palindrome.
# def is_palindrome(num):
#     for i in range(len(num)//2):
#         if num[i] != num[len(num)-1-i]:
#             return False
#     return True

# print(is_palindrome("023"))


# Find the factorial of a number
# a) Using loop
# def factorial_loop(num):
#     fact = 1
#     for i in range ( 1 , num +1):
#         fact = fact * i
#     return fact

# print(factorial_loop(5))

# b) Using recursion
def factorial_recursion(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursion(num - 1)
    
print(factorial_recursion(5))