#!/usr/bin/python3

def main():
    """Conduct the mystic ritual of arithmetic enchantment."""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Mystic Incantation: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    arcane_symbols = {"+": add, "-": sub, "*": mul, "/": div}
    operator = sys.argv[2]
    
    if operator not in arcane_symbols:
        print("Unknown operator. The mystical symbols are: +, -, *, and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    
    result = arcane_symbols[operator](a, b)
    print("Arithmancy reveals: {} {} {} = {}".format(a, operator, b, result))

if __name__ == "__main__":
    main()

