import logging

logging.basicConfig(level=logging.INFO)

PASSWORD = "admin123"


def divide_numbers(a, b):
    try:
        return a / b
    except Exception:
        return None


def check_user(username):
    if username == "":
        print("Username is empty")
    else:
        print("Welcome " + username)


def main():
    username = input("Enter username: ")
    result = divide_numbers(10, 0)

    if result is None:
        logging.error("Division failed")

    check_user(username)


if __name__ == "__main__":
    main()