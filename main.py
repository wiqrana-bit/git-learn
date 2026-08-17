#Adding comments to main.py
# This is the main entry point of the application
# It prompts the user for two numbers, performs addition using the add function from the calculator module
from utils.calculator import add


def main() -> None:
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number has been entered")
        return

    result = add(a, b)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
#Adding comments to main.py
# This is the main entry point of the application
# It prompts the user for two numbers, performs addition using the add function from the calculator module