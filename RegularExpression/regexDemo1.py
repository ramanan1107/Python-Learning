import re
password = input("Enter password: ")

if (
    len(password) >= 8
    and re.search(r"[A-Z]", password)
    and re.search(r"[a-z]", password)
    and re.search(r"\d.*\d", password)
    and re.search(r"[@#$%!]", password)
    and not re.search(r"\s", password)
):
    print("Strong password")
else:
    print("Weak password")
