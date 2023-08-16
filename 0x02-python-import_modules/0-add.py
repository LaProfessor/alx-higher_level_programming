#!/usr/bin/python3

def main():
    """Calculate and showcase a numeric harmony."""
    from math_operations import custom_add

    num1 = 1
    num2 = 2
    sum_result = custom_add(num1, num2)

    print("In the symphony of numbers, {} and {} create a harmonious sum: {}".format(num1, num2, sum_result))

if __name__ == "__main__":

    main()

