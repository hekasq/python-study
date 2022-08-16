def add_numbers_int(num1, num2):
    print(num1 + num2)


def add_numbers_float(num1, num2, num3):
    print(num1 + num2)


# Why doesn't 0.1+0.2-0.3 equal 0.0 ? floating point accuracy and computer's abilities to represent numbers in
# memory; https://docs.python.org/2/tutorial/floatingpoint.html
def add_numbers_float(num1, num2, num3):
    print(num1 + num2 + num3)


def check_modulus(num1, num2):
    print(num1 % num2)


if __name__ == '__main__':
    add_numbers_int(2, 3)
    add_numbers_float(2.5, 3.5, 0)
    add_numbers_float(0.1, 0.2, -0.3)
    check_modulus(10, 3)
