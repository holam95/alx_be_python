def safe_divide(numerator, denominator):
    """Safely performs division and handles errors."""
    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)

        # Attempt to divide
        result = num / denom
        return f"The result of the division is {result:.1f}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
