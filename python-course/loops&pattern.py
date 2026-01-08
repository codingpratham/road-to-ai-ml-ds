# Print numbers from 1 to N using a loop.
# num = int ( input ( "Enter a number:"))
# for i in range ( 1 , num+1):
#     print ( i )


# Print the multiplication table of a number.
# num = int ( input ( "Enter a number:"))
# for i in range(1 , 11):
#     print(num * i)

# Find the sum of first N natural numbers.
# num = int ( input ( "Enter a number:"))
# sum = 0
# for i in range(1 , num+1):
#     sum=float(sum+i)

# print(sum)

# Print a right-angled triangle star pattern.
# num = int ( input ( "Enter a number:"))
# for i in range (num+1):
#     print("*" * i)

# Count the number of digits in a given number.
num = int ( input ( "Enter a number:"))
count = 0
while num > 0:
    num = num // 10
    count = count + 1
print(count)

    