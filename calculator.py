def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    print("Simple Calculator")
    
    try:
        # Prompt the user to input two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Display operation choices
        print("Choose the operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        # Prompt the user to choose an operation
        choice = input("Enter the number corresponding to the operation (1/2/3/4): ")
        
        # Perform the calculation based on the user's choice
        if choice == '1':
            result = add(num1, num2)
            operation = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operation = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operation = '*'
        elif choice == '4':
            result = divide(num1, num2)
            operation = '/'
        else:
            print("Invalid choice.")
            return
        
        # Display the result
        print(f"{num1} {operation} {num2} = {result}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for the numbers.")

if __name__ == "__main__":
    main()
