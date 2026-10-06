import subprocess


def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login successful"
    return "Invalid credentials"


def run_command(command):
    return subprocess.call(command, shell=True)


if __name__ == "__main__":
    print(login("admin", "admin123"))