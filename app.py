# Simple Python Program

# Ask user for name
name = input("Enter your name: ")

# Ask user for age
age = int(input("Enter your age: "))

# Greet user
print("Hello", name + "!")

# Check age
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Loop example
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

print("Program finished.")

