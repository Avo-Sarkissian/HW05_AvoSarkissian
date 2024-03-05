# Defines the BasicMathOperations class
class BasicMathOperations:
    # Method to greet the user with their full name
    def greet_user(self, first_name, last_name):
        
        return f"Hello, {first_name} {last_name}. Welcome!"

    # Method to add two numbers provided by the user and return the sum
    def add_numbers(self):
       
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1 + num2
        except ValueError:
            return "Please enter valid numbers."

    # Method to perform a basic operation (addition, subtraction, multiplication, division) on two numbers
    def perform_operation(self, num1, num2, operator):
    
        try:
            if operator == '+':
                return num1 + num2
            elif operator == '-':
                return num1 - num2
            elif operator == '*':
                return num1 * num2
            elif operator == '/':
                return num1 / num2
        except ZeroDivisionError:
            return "Error: Division by zero."
        return "Invalid operator."

    # Method to return the square of a number
    def square_number(self, num):
       
        return num ** 2

    # Method to compute the factorial of a number
    def factorial(self, n):
      
        if n < 0:
            return "Error: Factorial of a negative number doesn't exist."
        elif n == 0:
            return 1
        else:
            fact = 1
            for i in range(1, n + 1):
                fact *= i
            return fact

    # Method to display counting from a start number to an end number
    def counting(self, start, end):
     
        if start > end:
            return "Error: Start number is greater than end number."
        for number in range(start, end + 1):
            print(number)

    # Helper method to calculate and return the square of a number
    def calculate_square(self, num):
    
        return num ** 2

    # Method to compute the hypotenuse of a right-angle triangle given the base and perpendicular
    def calculate_hypotenuse(self, base, perpendicular):
        
        return (self.calculate_square(base) + self.calculate_square(perpendicular)) ** 0.5

    # Method to calculate the area of a rectangle given its width and height
    def area_of_rectangle(self, width, height):
        
        return width * height

    # Method to compute the power of a number given a base and an exponent
    def power_of_number(self, base, exponent):
        
        return base ** exponent

    # Method to return the type of the provided argument
    def type_of_argument(self, arg):
       
        return type(arg).__name__

# Main function to interact with the user and call the appropriate class method based on user choice
def main():
    # Create an instance of the BasicMathOperations class
    bmo = BasicMathOperations()

    while True:
        print("\nChoose an operation:\n"
              "1. Greet User\n"
              "2. Add Numbers\n"
              "3. Perform Operation\n"
              "4. Square Number\n"
              "5. Factorial\n"
              "6. Counting\n"
              "7. Compute Hypotenuse\n"
              "8. Area of Rectangle\n"
              "9. Power of Number\n"
              "10. Type of Argument\n"
              "11. Exit")
        choice = input("Enter your choice: ")


# The following options within the main function prompt the user for the proper inputs, then call the different operator functions within the BMO class in order to calculate the correct answer

        if choice == '11':
            break  # Exit the program
        elif choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            print(bmo.greet_user(first_name, last_name))
            
        elif choice == '2':
            print("The sum is:", bmo.add_numbers())
            
        elif choice == '3':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter the operator (+, -, *, /): ")
            print("Result:", bmo.perform_operation(num1, num2, operator))
            
        elif choice == '4':
            num = float(input("Enter a number to square: "))
            print("Square of the number is:", bmo.square_number(num))
            
        elif choice == '5':
            n = int(input("Enter a number to find the factorial: "))
            print("Factorial of the number is:", bmo.factorial(n))
            
        elif choice == '6':
            start = int(input("Enter the start number: "))
            end = int(input("Enter the end number: "))
            print("Counting from start to end:")
            bmo.counting(start, end)
            
        elif choice == '7':
            base = float(input("Enter the base of the triangle: "))
            perpendicular = float(input("Enter the perpendicular of the triangle: "))
            print("Hypotenuse of the triangle is:", bmo.calculate_hypotenuse(base, perpendicular))
            
        elif choice == '8':
            width = float(input("Enter the width of the rectangle: "))
            height = float(input("Enter the height of the rectangle: "))
            print("Area of the rectangle is:", bmo.area_of_rectangle(width, height))
            
        elif choice == '9':
            base = float(input("Enter the base number: "))
            exponent = float(input("Enter the exponent: "))
            print("Result of power calculation is:", bmo.power_of_number(base, exponent))
            
        elif choice == '10':
            arg = input("Enter something to check its type: ")
            print("The type of the input is:", bmo.type_of_argument(arg))
            
        else:
            print("Invalid choice, please try again.")


# Ensure that the main function runs only when the script is executed directly (not imported as a module)
if __name__ == "__main__":
    main()



