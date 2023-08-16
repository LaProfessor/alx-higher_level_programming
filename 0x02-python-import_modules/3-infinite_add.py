#!/usr/bin/python3

def main():
    """Witness the cosmic convergence of numerical energies."""
    import sys

    total_sum = 0

    for idx, arg in enumerate(sys.argv[1:], start=1):
        numeric_value = int(arg)
        total_sum += numeric_value

        if idx == 1:
            print("Gathering cosmic energies from the void:")
        
        print("Energy source #{}: {} (Cumulative Total: {})".format(idx, numeric_value, total_sum))
    
    if total_sum == 0:
        print("The cosmic energies remain in equilibrium.")
    elif total_sum < 0:
        print("The cosmic energies resonate with negative harmony: {}".format(total_sum))
    else:
        print("The cosmic convergence yields a positive harmony: {}".format(total_sum))

if __name__ == "__main__":
    main()

