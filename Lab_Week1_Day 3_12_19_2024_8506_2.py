#2. Using input function take two number and then swap the number
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num1 = num1 + num2  
num2 = num1 - num2  
num1 = num1 - num2  
print(f"After swapping: First number = {num1}, Second number = {num2}")
