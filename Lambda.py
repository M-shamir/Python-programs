add = lambda x,y : x+y
sub = lambda x,y : x-y
mul = lambda x,y : x*y
div = lambda x,y : x/y
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

print("5. Exit")
choice = int(input("Enter your choice: "))
if choice == 1:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Result: ",add(x,y))
elif choice == 2:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Result: ",sub(x,y))
elif choice == 3:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Result: ",mul(x,y))
elif choice == 4:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Result: ",div(x,y))
elif choice == 5:
    exit()
else:
    print("Invalid choice")


