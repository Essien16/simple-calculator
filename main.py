from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

mathematical_operation = {
  "+" : add,
  "-": subtract,
  "*" : multiply,
  "/" : divide,
}

num1 = float(input("What is the first number?: "))

for operation in mathematical_operation:
  print(operation)
operation_symbol = input("Pick an operation from the line above: ")
num2 = float(input("What is the second number?: "))
calculation = mathematical_operation[operation_symbol]
first_answer = calculation(num1, num2)

# if operation_symbol == "+":
#   answer = add(num1, num2)
# elif operation_symbol == "-":
#   answer = subtract(num1, num2)
# elif operation_symbol == "*":
#   answer = multiply(num1, num2)
# elif operation_symbol == "/":
#   answer = divide(num1, num2)
# else:
#   print("Invalid Operation, try again.")

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

game_on = False
while not game_on:
    should_continue = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit.")
    if should_continue == "n":
        game_on = True
    elif should_continue == "y":
        operation_symbol = input("Pick an operation: ")
        num3 = float(input("What is the next number?: "))
        calculation = mathematical_operation[operation_symbol]
        second_answer = calculation(first_answer, num3)

        print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")