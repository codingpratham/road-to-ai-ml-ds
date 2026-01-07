# BASIC INPUT–OUTPUT & VARIABLES (1–5)

# Take two numbers as input and print their sum, difference, product, and quotient.
# i = True
# while i:
#     print("Select the operation you want to perform:")
#     print("1. Addition")
#     print("2. Difference")
#     print("3. Product")
#     print("4. Quotient")
#     print("5. Exit")


#     n = int(input("Enter a number between 1 to 5: "))

#     match n :
#         case 1:
#             a = int(input("Enter the a value: "))
#             b = int(input("Enter the b value: "))
#             add = a + b
#             print("You have selected Addition")
#             print("Addition of a and b is: ", add)
#         case 2:
#             a = int(input("Enter the a value: "))
#             b = int(input("Enter the b value: "))
#             difference = a - b
#             print("You have selected Difference")
#             print("Difference of a and b is: ", difference)     
#         case 3:
#             a = int(input("Enter the a value: "))
#             b = int(input("Enter the b value: "))
#             product = a*b
#             print("You have selected Product")
#             print("Product of a and b is: ", product)
#         case 4:
#             a = int(input("Enter the a value: "))
#             b = int(input("Enter the b value: "))
#             quotiont = a / b
#             print("You have selected Quotient")
#             print("Quotient of a and b is: ", quotiont)
#         case 5:
#             False
#             break

# Write a program to swap two numbers
# a) Using a third variable
# a = int(input("Enter the value of a: "))
# b= int(input("Enter the value of b:"))

# print("The value of a before swapping is: ", a)
# print("The value of b before swapping is: ", b)

# temp = a
# a=b
# b=temp

# print("The value of a after swapping is: ", a)
# print("The value of b after swapping is: ", b)



# b) Without using a third variable
# a = int(input("Enter the value of a: "))
# b= int(input("Enter the value of b:"))

# print("The value of a before swapping is: ", a)
# print("The value of b before swapping is: ", b)

# a,b = b,a

# print("The value of a after swapping is: ", a)
# print("The value of b after swapping is: ", b)

# Take a number and check whether it is positive, negative, or zero.
# num = int(input("Enter the number: "))

# if num <0 :
#     print("the number is positive")
# elif num>0:
#     print("the number is negative")
# else:
#     print("the number is zero")


# Convert Celsius to Fahrenheit.
# c = int(input("Enter the temperature in celsius: "))
# f= (9/5 * c) + 32

# print("The temperature in fahrenheit is: ", f)

# Find the simple interest given principal, rate, and time.
p = int(input("Enter the principal amount: "))
r = int(input("Enter the rate of interest: "))
t = int(input("Enter the time: "))
a =float (p(1+r*t)) 

print("The simple interest is: ", a)

            
            
        