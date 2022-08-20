def check_password_ascii(password: str) -> bool:
    has_numeric = False
    has_upper = False
    has_lower = False
    for char in password:
        ascii_code = ord(char)
        if ascii_code >= 65 and ascii_code <= 90:
            has_upper = True
        if ascii_code >= 97 and ascii_code <= 122:
            has_lower = True
        if ascii_code >= 48 and ascii_code <= 57:
            has_numeric = True
    return has_numeric and has_lower and has_upper


def check_password(password: str) -> bool:
    if len(password) < 8:
        return False
    
    has_numeric = False
    has_upper = False
    has_lower = False

    for char in password:
        if char.isdigit():
            has_numeric = True
        if char.isalpha() and char.islower():
            has_lower = True
        if char.isalpha() and char.isupper():
            has_upper = True
        if has_numeric and has_lower and has_upper:
            break

    return has_numeric and has_lower and has_upper


password = input("Password must be at least 8 characters long,\ncontain at least one upper case letter, \none lower case letter and one numeric character: ")
print(check_password(password))