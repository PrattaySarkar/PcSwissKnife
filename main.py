import random
import string
import math
import pyqrcode
import hashlib
import os


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def convert_length(value, from_unit, to_unit):
    units = {'m': 1, 'cm': 0.01, 'mm': 0.001, 'km': 1000, 'in': 0.0254, 'ft': 0.3048, 'yd': 0.9144, 'mi': 1609.34}
    return value * units[from_unit] / units[to_unit]


def basic_calculator():
    expression = input("Enter a mathematical expression: ")
    try:
        result = eval(expression)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)


def generate_qr_code(data, file_name='qr_code.png'):
    qr = pyqrcode.create(data)
    qr.png(file_name, scale=8)


def hash_file(file_path, algorithm='sha256'):
    if not os.path.exists(file_path):
        print("File not found.")
        return
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
            hashed_content = hashlib.new(algorithm, content).hexdigest()
            print(f"{algorithm.upper()} Hash of {file_path}: {hashed_content}")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    print("Welcome to SwissKnife - Your All-in-One Tool!")
    print("1. Generate Random Password")
    print("2. Convert Length Units")
    print("3. Basic Calculator")
    print("4. Generate QR Code")
    print("5. Hash File")
    choice = input("Please select an option (1/2/3/4/5): ")

    if choice == '1':
        password_length = int(input("Enter the length of the password (default is 12): "))
        print("Generated Password:", generate_password(password_length))
    elif choice == '2':
        value = float(input("Enter the value: "))
        from_unit = input("Enter the source unit (m/cm/mm/km/in/ft/yd/mi): ")
        to_unit = input("Enter the target unit (m/cm/mm/km/in/ft/yd/mi): ")
        print("Converted Value:", convert_length(value, from_unit, to_unit))
    elif choice == '3':
        basic_calculator()
    elif choice == '4':
        data = input("Enter the data for the QR code: ")
        file_name = input("Enter the file name for the QR code (default is qr_code.png): ")
        generate_qr_code(data, file_name)
    elif choice == '5':
        file_path = input("Enter the path to the file: ")
        algorithm = input("Enter the hashing algorithm (default is sha256): ")
        hash_file(file_path, algorithm)
    else:
        print("Invalid choice. Please select a valid option.")
