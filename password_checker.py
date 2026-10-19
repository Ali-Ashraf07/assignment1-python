def check_password_strength(password):
    score = 0
    
    # Check length
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
        
    # Check for character types
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in "!@#$%^&*()_+-=" for char in password):
        score += 1
        
    # Evaluate strength
    if score >= 5:
        return "Strong Password"
    elif score >= 3:
        return "Moderate Password"
    else:
        return "Weak Password"

if __name__ == "__main__":
    pwd = input("Enter a password to test: ")
    result = check_password_strength(pwd)
    print(f"Password Rating: {result}")