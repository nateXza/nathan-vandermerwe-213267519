import random
import string

def generate_password(length: int = 12, uppercase: bool = True, numbers: bool = True, symbols: bool = True) -> str:
    """
    Generate a random password with the given parameters.

    :param length: Length of the password (minimum 4).
    :param uppercase: Include uppercase letters if True.
    :param numbers: Include numbers if True.
    :param symbols: Include symbols if True.
    :return: Generated password as a string.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if uppercase else ''
    digits = string.digits if numbers else ''
    punctuation = string.punctuation if symbols else ''

    all_characters = lowercase_letters + uppercase_letters + digits + punctuation

    if not all_characters:
        raise ValueError("At least one character set must be selected.")

    password = []
    if uppercase:
        password.append(random.choice(uppercase_letters))
    if numbers:
        password.append(random.choice(digits))
    if symbols:
        password.append(random.choice(punctuation))

    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(all_characters))

    random.shuffle(password)
    return ''.join(password)

def get_user_input() -> tuple:
    """
    Get user input for password generation parameters.

    :return: Tuple containing length, uppercase, numbers, and symbols preferences.
    """
    while True:
        try:
            length = int(input("Enter password length (minimum 4): "))
            if length < 4:
                print("Password length must be at least 4. Setting length to 4.")
                length = 4

            uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
            numbers = input("Include numbers? (y/n): ").lower() == 'y'
            symbols = input("Include symbols? (y/n): ").lower() == 'y'

            return length, uppercase, numbers, symbols
        except ValueError:
            print("Invalid input. Please enter a valid number for password length.")

if __name__ == "__main__":
    print("=== Password Generator ===")
    length, uppercase, numbers, symbols = get_user_input()

    try:
        password = generate_password(length, uppercase, numbers, symbols)
        print("\nGenerated Password:", password)
    except ValueError as e:
        print(f"Error: {e}")