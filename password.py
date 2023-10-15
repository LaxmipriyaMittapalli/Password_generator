import string
import secrets
def generate_random_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True, special_chars='!@#$%^&*'):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += special_chars
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password
def get_password_criteria():
    length = int(input("Enter the password length: "))
    use_lowercase = input("Use lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Use uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Use digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Use special characters? (y/n): ").lower() == 'y'
    if use_special_chars:
        special_chars = input("Enter special characters to use: ")
    else:
        special_chars = ''
    return length, use_lowercase, use_uppercase, use_digits, use_special_chars, special_chars
def main():
    print("Random Password Generator")
    length, use_lowercase, use_uppercase, use_digits, use_special_chars, special_chars = get_password_criteria()
    password = generate_random_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars, special_chars)
    print("Generated Password:", password)
if __name__ == "__main__":
    main()
