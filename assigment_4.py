#TASK 1
def read_file():
    try:
        with open(filename, 'r') as file:
            print("Reading file content:")
            for line_number, line in enumerate(file, start=1):
                print(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Specify the filename
filename = 'sample.txt'

# Call the function to read the file
read_file()

#TASK 2
user_input = input("Enter text to write to the file: ")
with open("output.txt", 'w') as file:
    file.write(user_input + '\n')
print("Data successfully written to output.txt.")

additional_input = input("Enter additional text to append:")
with open("output.txt", 'a') as file:
    file.write(additional_input + '\n')
    print("Data successfully appended.")

print("\nFinal contents of output.txt")
with open("output.txt", 'r') as file:
    print(file.read())

