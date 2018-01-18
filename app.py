import argparse
import sys
import json
import numpy as np
import indicator
import benchmark
#from terminaltables import AsciiTable


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


def get_code(arg):
    """Determines the insee code of the user's input arguement 
    """
    try:
        if int(arg) >= 1000 and int(arg) < 99000:
            return arg
        #solution temporaire, on pourra utiliser un autre dico pour matcher les noms et code
    except BaseException:
        reader = open('static_dic/activite2014.json', 'r')
        dico = json.load(reader)
        for key in dico:
            if dico[key]["nom"]==arg:
                return key


class InputError(Exception):
    pass


def process(function, argument):
    code = get_code(argument)
    if code == None:
        raise InputError
    if function == 'indicator':
        print(indicator.main(code))
    elif function == 'benchmark':
        print(benchmark.main(code))
        # pour un rendu propre dans la console 
        #table_data = benchmark.main(code)
        #table = AsciiTable([table_data[i][:4] for i in range(len(table_data))])
        #print(table.table)

if __name__ == '__main__':
    main()