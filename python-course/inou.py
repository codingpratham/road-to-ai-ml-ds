i = True
while i:
    print("Select the operation you want to perform:")
    print("1. Addition")
    print("2. Difference")
    print("3. Product")
    print("4. Quotient")
    print("5. Exit")


    n = int(input("Enter a number between 1 to 5: "))

    match n :
        case 1:
            a = int(input("Enter the a value: "))
            b = int(input("Enter the b value: "))
            add = a + b
            print("You have selected Addition")
            print("Addition of a and b is: ", add)
        case 2:
            a = int(input("Enter the a value: "))
            b = int(input("Enter the b value: "))
            difference = a - b
            print("You have selected Difference")
            print("Difference of a and b is: ", difference)     
        case 3:
            a = int(input("Enter the a value: "))
            b = int(input("Enter the b value: "))
            product = a*b
            print("You have selected Product")
            print("Product of a and b is: ", product)
        case 4:
            a = int(input("Enter the a value: "))
            b = int(input("Enter the b value: "))
            quotiont = a / b
            print("You have selected Quotient")
            print("Quotient of a and b is: ", quotiont)
        case 5:
            False
            break
            
            
        