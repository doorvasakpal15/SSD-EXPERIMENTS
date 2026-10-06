import logging

# Secure logging configuration
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def divide_numbers():

    try:
        number = float(input("Enter number: "))
        divisor = float(input("Enter divisor: "))

        if divisor == 0:
            raise ValueError("Division by zero")

        result = number / divisor

        print("Result:", result)

    except ValueError as error:

        # Log technical details
        logging.error("Invalid operation: %s", error)

        # Show safe message to user
        print("Error: Invalid input or operation.")

    except Exception as error:

        logging.error("Unexpected error: %s", error)

        print("Error: An unexpected error occurred.")


if __name__ == "__main__":
    divide_numbers()