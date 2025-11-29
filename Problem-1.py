class Calculator:
    """Simple calculator supporting add, sub, mul, div."""
    def calculate(self, a: float, b: float, operation: str):
        op = operation.strip().lower()
        if op in ("add", "+", "plus"):
            return a + b
        if op in ("sub", "-", "minus"):
            return a - b
        if op in ("mul", "*", "x", "times"):
            return a * b
        if op in ("div", "/", "divide"):
            if b == 0:
                return "Error: Division by zero is not allowed."
            return a / b
        return f"Invalid operation: '{operation}'. Use add/sub/mul/div."

def read_float(prompt: str):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number (e.g., 3.5).")

if __name__ == "__main__":
    a = read_float("Enter first number (a): ")
    b = read_float("Enter second number (b): ")
    op = input("Enter operation (add/sub/mul/div): ")
    calc = Calculator()
    result = calc.calculate(a, b, op)
    print("Result:", result)
