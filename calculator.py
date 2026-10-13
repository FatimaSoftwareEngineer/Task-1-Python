"""
Simple Calculator - TecniForge ETP (Python Track)

Concepts used in this script:
- Variables : store numbers, user choice, results
- Loops     : keep showing the menu and validate user input (while / for)
- Functions : each operation and each task has its own function
- List      : stores the calculation history
- Dict      : maps each operation symbol to its name and function
"""


# ---------------------------------------------------------
# 1) Functions: one function per operation
# ---------------------------------------------------------
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None  # division by zero is not allowed
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    if b == 0:
        return None  # modulus by zero is not allowed
    return a % b


# ---------------------------------------------------------
# 2) Dictionary: symbol -> (name, function)
# ---------------------------------------------------------
OPERATIONS = {
    "+": ("Addition", add),
    "-": ("Subtraction", subtract),
    "*": ("Multiplication", multiply),
    "/": ("Division", divide),
    "**": ("Power", power),
    "%": ("Modulus", modulus),
}

# ---------------------------------------------------------
# 3) List: calculation history is stored here
# ---------------------------------------------------------
history = []


def show_menu():
    """Print the menu (a loop goes through the dictionary items)."""
    print("\n" + "=" * 35)
    print("        SIMPLE CALCULATOR")
    print("=" * 35)
    for symbol, (name, _) in OPERATIONS.items():
        print(f"  {symbol:<3} -> {name}")
    print("  h   -> Show history")
    print("  c   -> Clear history")
    print("  q   -> Quit")
    print("=" * 35)


def get_number(message):
    """Keep asking until the user enters a valid number."""
    while True:
        value = input(message)
        try:
            return float(value)
        except ValueError:
            print("Invalid input! Please enter a number (e.g. 5 or 3.14).")


def format_number(n):
    """Show 5.0 as 5, and 5.5 as 5.5."""
    if n == int(n):
        return str(int(n))
    return str(round(n, 6))


def show_history():
    """Print all previous calculations."""
    if len(history) == 0:
        print("\nNo history yet.")
        return
    print("\n--- Calculation History ---")
    for index, record in enumerate(history, start=1):
        print(f"{index}. {record}")


def calculate(symbol):
    """Take two numbers and run the selected operation."""
    name, func = OPERATIONS[symbol]
    print(f"\n[{name}]")
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    result = func(num1, num2)

    if result is None:
        print("Error: Cannot divide or take modulus by zero!")
        return

    record = f"{format_number(num1)} {symbol} {format_number(num2)} = {format_number(result)}"
    history.append(record)  # save to the list
    print(f"Result: {record}")


def main():
    """Main loop: the calculator runs until the user chooses to quit."""
    print("Welcome to the Calculator!")

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip().lower()

        if choice == "q":
            print("\nThank you! Goodbye.")
            break
        elif choice == "h":
            show_history()
        elif choice == "c":
            history.clear()
            print("\nHistory cleared.")
        elif choice in OPERATIONS:
            calculate(choice)
        else:
            print("\nInvalid choice! Please select an option from the menu.")


# Run main() only when the script is executed directly
if __name__ == "__main__":
    main()