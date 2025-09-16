#Task 1



def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

# Calling the function with a sample number
sample_number = 5
print(f"The factorial of {sample_number} is: {factorial(sample_number)}")

#Task 2

import math
num = float(input("Enter a number: "))

square_root = math.sqrt(num)
natural_number = math.log(num)
sine_value = math.sin(num)

print(f"Square root of {num} is {square_root}")
print(f"Natural number {num} is {natural_number}")
print(f"Sine value {num} is {sine_value}")