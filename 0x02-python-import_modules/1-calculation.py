#!/usr/bin/python3

def main():
    """Embark on a mathematical journey with the numbers 10 and 5."""
    from mathematical_tales import addition, subtraction, multiplication, division

    number_a = 10
    number_b = 5

    print("Once upon a calculation, {} and {} joined forces:".format(number_a, number_b))
    print("In the realm of addition, they united to make: {}".format(addition(number_a, number_b)))
    print("In the realm of subtraction, they parted ways and left behind: {}".format(subtraction(number_a, number_b)))
    print("In the realm of multiplication, they combined energies to yield: {}".format(multiplication(number_a, number_b)))
    print("In the realm of division, they shared their essence to create: {}".format(division(number_a, number_b)))

if __name__ == "__main__":
    main()

