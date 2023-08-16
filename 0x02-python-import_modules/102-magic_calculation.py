#!/usr/bin/python3

def magic_potion(a, b):
    """Embark on a mystical potion-making quest."""
    from magic_calculation_102 import add, sub

    if a < b:
        potion = add(a, b)
        for ingredient in range(4, 6):
            potion = add(potion, ingredient)
        return potion

    else:
        return sub(a, b)

