#!/usr/bin/python3
# A function that prints an integer


def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        stderr.write("Exception: {}\n".format(err))
        return False
