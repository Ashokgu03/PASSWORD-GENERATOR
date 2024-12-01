import random
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_symbols=True):
    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ''
    numbers = string.digits if include_numbers else ''
    symbols = string.punctuation if include_symbols else ''

    # Combine pools based on user preferences
    all_characters = lowercase + uppercase + numbers + symbols

    if not all_characters:
        raise ValueError("At least one character type must be selected!")

    # Ensure the password has at least one of each selected type
    password = []
    if include_uppercase:
        password.append(random.choice(uppercase))
    if include_numbers:
        password.append(random.choice(numbers))
    if include_symbols:
        password.append(random.choice(symbols))
    password.append(random.choice(lowercase))  # Always include at least one lowercase

    # Fill the rest of the password length with random characters
    while len(password) < length:
        password.append(random.choice(all_characters))

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Example usage
if __name__ == "__main__":
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        include_uppercase = input("Include uppercase letters? (y/n, default y): ").strip().lower() != 'n'
        include_numbers = input("Include numbers? (y/n, default y): ").strip().lower() != 'n'
        include_symbols = input("Include symbols? (y/n, default y): ").strip().lower() != 'n'

        password = generate_password(length, include_uppercase, include_numbers, include_symbols)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")