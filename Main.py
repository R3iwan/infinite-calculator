def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary


def binary_to_decimal(binary):
    decimal = 0
    binary = str(binary)
    for i in range(len(binary)):
        decimal += int(binary[i]) * (2 ** (len(binary) - 1 - i))
    return decimal


def decimal_to_octal(decimal):
    octal = ''
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal = decimal // 8
    return octal


def octal_to_decimal(octal):
    decimal = 0
    octal = str(octal)
    for i in range(len(octal)):
        decimal += int(octal[i]) * (8 ** (len(octal) - 1 - i))
    return decimal


def decimal_to_hexadecimal(decimal):
    hexadecimal = ''
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(remainder + 55) + hexadecimal
        decimal = decimal // 16
    return hexadecimal


def hexadecimal_to_decimal(hexadecimal):
    decimal = 0
    hexadecimal = str(hexadecimal)
    for i in range(len(hexadecimal)):
        if hexadecimal[i].isdigit():
            decimal += int(hexadecimal[i]) * (16 ** (len(hexadecimal) - 1 - i))
        else:
            decimal += (ord(hexadecimal[i]) - 55) * (16 ** (len(hexadecimal) - 1 - i))
    return decimal

def add(num1, num2, base):
    if base == 'bin':
        decimal1 = binary_to_decimal(num1)
        decimal2 = binary_to_decimal(num2)
        decimal_sum = decimal1 + decimal2
        return decimal_to_binary(decimal_sum)
    elif base == 'oct':
        decimal1 = octal_to_decimal(num1)
        decimal2 = octal_to_decimal(num2)
        decimal_sum = decimal1 + decimal2
        return decimal_to_octal(decimal_sum)
    elif base == 'hex':
        decimal1 = hexadecimal_to_decimal(num1)
        decimal2 = hexadecimal_to_decimal(num2)
        decimal_sum = decimal1 + decimal2
        return decimal_to_hexadecimal(decimal_sum)
    elif base == 'dec':
        num1 = float(num1)
        num2 = float(num2)
        return num1 + num2

def subtract(num1, num2, base):
    if base == 'bin':
        decimal1 = binary_to_decimal(num1)
        decimal2 = binary_to_decimal(num2)
        decimal_diff = decimal1 - decimal2
        return decimal_to_binary(decimal_diff)
    elif base == 'oct':
        decimal1 = octal_to_decimal(num1)
        decimal2 = octal_to_decimal(num2)
        decimal_diff = decimal1 - decimal2
        return decimal_to_octal(decimal_diff)
    elif base == 'hex':
        decimal1 = hexadecimal_to_decimal(num1)
        decimal2 = hexadecimal_to_decimal(num2)
        decimal_diff = decimal1 - decimal2
        return decimal_to_hexadecimal(decimal_diff)
    elif base == 'dec':
        num1 = float(num1)
        num2 = float(num2)
        return num1 - num2


def multiply(num1, num2, base):
    if base == 'bin':
        decimal1 = binary_to_decimal(num1)
        decimal2 = binary_to_decimal(num2)
        decimal_product = decimal1 * decimal2
        return decimal_to_binary(decimal_product)
    elif base == 'oct':
        decimal1 = octal_to_decimal(num1)
        decimal2 = octal_to_decimal(num2)
        decimal_product = decimal1 * decimal2
        return decimal_to_octal(decimal_product)
    elif base == 'hex':
        decimal1 = hexadecimal_to_decimal(num1)
        decimal2 = hexadecimal_to_decimal(num2)
        decimal_product = decimal1 * decimal2
        return decimal_to_hexadecimal(decimal_product)
    elif base == 'dec':
        num1 = float(num1)
        num2 = float(num2)
        return num1 * num2


def divide(num1, num2, base):
    if base == 'bin':
        decimal1 = binary_to_decimal(num1)
        decimal2 = binary_to_decimal(num2)
        decimal_quotient = decimal1 / decimal2
        return decimal_to_binary(decimal_quotient)
    elif base == 'oct':
        decimal1 = octal_to_decimal(num1)
        decimal2 = octal_to_decimal(num2)
        decimal_quotient = decimal1 / decimal2
        return decimal_to_octal(decimal_quotient)
    elif base == 'hex':
        decimal1 = hexadecimal_to_decimal(num1)
        decimal2 = hexadecimal_to_decimal(num2)
        decimal_quotient = decimal1 / decimal2
        return decimal_to_hexadecimal(decimal_quotient)
    elif base == 'dec':
        num1 = float(num1)
        num2 = float(num2)
        return num1 / num2


def perform_operation(num1, num2, operation, base):
    if operation == '+':
        return add(num1, num2, base)
    elif operation == '-':
        return subtract(num1, num2, base)
    elif operation == '*':
        return multiply(num1, num2, base)
    elif operation == '/':
        return divide(num1, num2, base)
    elif operation == 'c':
        print("Choose convert type: ")
        print("1)Binary to Decimal")
        print("2)Binary to Octal")
        print("3)Binary to Hexadecimal")
        print("4)Decimal to Binary")
        print("5)Octal to Binary")
        print("6)Hexadecimal to Binary")


if __name__ == '__main__':
    print("Infinite Calculator: Decimal, Binary, Octal and Hexadecimal")
    while True:
        num1 = input("Enter the first number: ")
        base = input("Enter the number system (bin, oct, hex, dec): ").lower()
        operation = input("Enter the operation (+, -, *, /, c): ")
        num2 = input("Enter the second number: ")
        result = perform_operation(num1, num2, operation, base)
        print("Result:", result)
        repeat = input("Do you want to perform another operation? (yes/no) ")
        if repeat.lower() != 'yes':
            break
    print("Exiting Infinite Calculator")