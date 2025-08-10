def basic_calc():
    print("🧮 This is a basic calculator program.")
    print("Enter two numbers and a math operation (+, -, *, /).")
    print("Type 'q' anytime to quit.\n")

basic_calc()

# --- Input Validation Loop for num1 ---
while True:
    num1 = input("Enter first number (or q to quit): ").strip()
    if num1.lower() == 'q':
        exit("👋 Exiting calculator. Goodbye!")
    try:
        num1 = float(num1)
        break
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")

# --- Input Validation Loop for num2 ---
while True:
    num2 = input("Enter second number (or q to quit): ").strip()
    if num2.lower() == 'q':
        exit("👋 Exiting calculator. Goodbye!")
    try:
        num2 = float(num2)
        break
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")

# --- Select Operation ---
print("\nAvailable operations: +  -  *  /")
print("Type 'q' to quit.")
while True:
    operation = input("Select operation to be carried out (+ - * /): ").strip()
    if operation.lower() == "q":
        exit("👋 Exiting calculator. Goodbye!")

    if operation == "+":
        calc = num1 + num2
        print(f"✅ Your answer is {num1} + {num2} = {calc}")
        break
    elif operation == "-":
        calc = num1 - num2
        print(f"✅ Your answer is {num1} - {num2} = {calc}")
        break
    elif operation == "*":
        calc = num1 * num2
        print(f"✅ Your answer is {num1} * {num2} = {calc}")
        break
    elif operation == "/":
        if num2 == 0:
            print("🚫 Division by zero is not allowed. Please re-enter the second number.")
            # re-prompt only num2
            while True:
                num2 = input("Enter a non-zero second number: ")
                try:
                    num2 = float(num2)
                    if num2 != 0:
                        break
                except ValueError:
                    print("❌ Invalid number. Try again.")
        calc = num1 / num2
        print(f"✅ Your answer is {num1} / {num2} = {calc}")
        break
    else:
        print("❌ Invalid operation. Choose one of: +  -  *  / or q to quit.")
