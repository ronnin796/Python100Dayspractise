import re

email = input("Enter your email:")


def validate_email(email):
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):  # regex validation
        return False
    return True


if validate_email(email):
    print("Email is valid")
else:
    print("Email is not valid")
