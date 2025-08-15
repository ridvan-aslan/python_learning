import re

SPECIAL_CHARS = '!@#$%^&*(),.?":{}|<>'

def check_password(password):
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")
    if not re.search(r"[A-Z]", password):
        raise ValueError("Password must contain at least one uppercase letter")
    if not re.search(r"[a-z]", password):
        raise ValueError("Password must contain at least one lowercase letter")
    if not re.search(r"[0-9]", password):
        raise ValueError("Password must contain at least one digit")
    if not re.search(rf"[{re.escape(SPECIAL_CHARS)}]", password):
        raise ValueError("Password must contain at least one special character")
    if re.search(r"\s", password):
        raise ValueError("Password must not contain spaces")
    if password.startswith(tuple(SPECIAL_CHARS)) or password.endswith(tuple(SPECIAL_CHARS)):
        raise ValueError("Password must not start or end with a special character")

# Example usage:
try:
    check_password("weakpasS.1")
except Exception as e:
    print(f"Password validation failed: {e}")
else:
    print("Password is valid")
finally:
    print("Password check completed")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        if len(name) > 10:
            raise ValueError("Name must not exceed 10 characters")
        if age < 0:
            raise ValueError("Age must be a non-negative integer") 
    
# p = Person("Rıdvannnnnn", -22)