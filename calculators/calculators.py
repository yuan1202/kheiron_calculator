import argparse
import re


# basic pattern search function
search_pattern = lambda string: re.findall(r'[+\-\*/](?:\s\-?\d+){2}|\-?\d+|[+\-*/](?=\s)', string)

# high level pattern search using recursion
def prefix_op(string):
    match = search_pattern(string)

    if len(match) == 1 and unit_prefix_op(match[0]) == match[0]:
        # exit condition #1
        return match[0]
    elif len(match) == 0:
        # exit condition #2
        return None
    else:
        # recusion
        next_string = ' '.join([unit_prefix_op(s) for s in match])
        return prefix_op(next_string)
    
# unit level pattern operation execution
def unit_prefix_op(match_unit):
    
    sub_match = re.findall(r'\-?\d+|[+\-*/](?=\s)', match_unit)
    
    if len(sub_match) == 3:
        # unit pattern found
        # quick check
        assert sub_match[0] in ['+', '-', '*', '/']
        # evaludate unit pattern and return
        return str(int(eval(' '.join([sub_match[1], sub_match[0], sub_match[2]]))))

    else:
        # if no unit pattern match, pass through
        return match_unit
    
    
def infix_op(string): return str(int(eval(string)))
    
    
# setup argparse
parser = argparse.ArgumentParser(description='Prefix & Infix Calculator')
parser.add_argument('input', help='input string, use space to seperate beetween digits and operators.', type=str)
parser.add_argument('-m', '--mode', help='calculation mode: prefix or infix.', default='prefix')


def calc():
    args = parser.parse_args()
    
    print('calculation request: {}'.format(args.input))
    
    if args.mode == 'prefix':
        print('calculation result: {}'.format(prefix_op(args.input)))
    elif args.mode == 'infix':
        print('calculation result: {}'.format(infix_op(args.input)))
    else:
        print('incorrect calculation mode!')