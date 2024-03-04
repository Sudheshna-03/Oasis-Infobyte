import random
import string
def gen_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not any([use_upper, use_lower, use_digits, use_symbols]):
        print("Please select at least one type of character.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the length of the password: "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = gen_password(length, use_upper, use_lower, use_digits, use_symbols)
    if password:
        print("Your generated password is:", password)


if __name__ == "__main__":
    main()
