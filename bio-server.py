def calculate_average():
  
    # Prompting the user to enter three numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    # Calculating the average value
    average = (num1 + num2 + num3) / 3

    return average

# Example usage of the calculate_average function
result = calculate_average()
print(f"The average value of the three numbers is: {result}")