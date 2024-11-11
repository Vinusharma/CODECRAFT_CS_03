import re

def check_password_strength(password):
    # Define initial strength score
    strength_score = 0

    # Check length of the password
    if len(password) >= 8:
        strength_score += 1
    else:
        print("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength_score += 1
    else:
        print("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength_score += 1
    else:
        print("Password should contain at least one lowercase letter.")

    # Check for digits
    if re.search(r"[0-9]", password):
        strength_score += 1
    else:
        print("Password should contain at least one digit.")

    # Check for special characters
    if re.search(r"[@$!%*?&#]", password):
        strength_score += 1
    else:
        print("Password should contain at least one special character (@, $, !, %, *, ?, & or #).")

    # Determine password strength based on the score
    if strength_score == 5:
        return "Strong Password"
    elif 3 <= strength_score < 5:
        return "Moderate Password"
    else:
        return "Weak Password"

# Example usage
password = input("Enter a password to check its strength: ")
strength = check_password_strength(password)
print("Password Strength:", strength)
