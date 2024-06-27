class Calculator:
    def add(self, a,b):
        return a+b
    def sub(self, a,b):
        return a-b
    def mul(self, a,b):
        return a*b
    def div(self, a,b):
        if b!=0:
            return a/b
        else:
            return "Cannot divide by zero"
def main():
    calc = Calculator()
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice == '5':
            print("Exit program")
            break
        if choice in ['1','2','3','4']:
            try:
                num1 = float(input("Enter the first number"))
                num2 = float(input("Enter the second number"))
            except ValueError:
                print("Invalid input")
                continue
            if choice == '1':
                result =calc.add(num1,num2)
            elif choice == '2':
                result=calc.sub(num1,num2)
            elif choice == '3':
                result=calc.mul(num1,num2)
            elif choice == '4':
                result=calc.div(num1,num2)

            print(f"result is {num1} and {num2} is {result}")
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()          
    