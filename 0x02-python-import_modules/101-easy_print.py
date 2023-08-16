#!/usr/bin/python3

def main():
    """Unleash the cosmic proclamation: #pythoniscool"""
    import os

    cosmic_message = "#pythoniscool\n"
    os.write(1, cosmic_message.encode("UTF-8"))

if __name__ == "__main__":
    main()

