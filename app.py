import argparse
import sys
import numpy as np
#import indicator
#import benchmark


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--function', help='Input function', required=True)
parser.add_argument('-a', '--argument', help='Output argument', required=False)
args = parser.parse_args()


def main():
    """Retrieves and assert user's input
    """
    function = args.function
    if len(sys.argv) >= 4:
        argument = args.argument
    else:
        argument = "None"
    assert function in ['benchmark', 'indicator'], \
        'Function is not one of benchmark or indicator : ' + function
    process(function, argument)


def type(arg):
    """Determines the type of argument :
    Did the user type a department number, city, or postal code?
    """
    try:
        if int(arg) >= 1 and int(arg) <= 98:
            return "dpt"
        elif arg == "None":
            return "None"
        elif int(arg) >= 1000 and int(arg) < 99000:
            return "postal_code"
    except BaseException:
        return "other"


def process(function, argument):
    if function == 'indicator':
        #indicator.main()
        pass
    elif function == 'benchmark':
        #benchmark.main()
        pass

if __name__ == '__main__':
    main()