def safe_divide(numerator, denominator):
    """Safely performs division and handles errors."""
    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)

        # Attempt to divide
        result = num / denom
        return f"Result: {result:.2f}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Both inputs must be numeric."
