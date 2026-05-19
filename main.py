from utils.calculator import add


def main() -> None:
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number entered")
        return

    result = add(a, b)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
