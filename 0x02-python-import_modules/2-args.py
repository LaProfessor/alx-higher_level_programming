#!/usr/bin/python3

def main():
    """Unravel the mysteries of command-line arguments."""
    import sys

    num_arguments = len(sys.argv) - 1

    if num_arguments == 0:
        print("Ahoy, explorer! You've embarked on a journey with no maps—no arguments to guide you.")
    elif num_arguments == 1:
        print("A lone artifact lies before you—the mystical argument:")
    else:
        print("You stand amidst a collection of {} artifacts, each holding a unique story:".format(num_arguments))

    for idx, argument in enumerate(sys.argv[1:], start=1):
        print("Artifact #{}: '{}'".format(idx, argument))

if __name__ == "__main__":
    main()

