pm = ['+', '-']
td = ['*', '/']
operators = pm+td
triple_bracket_front = '^\([0-9][+*-/][0-9][+*-/][0-9]\)[+*-/][0-9]$'
triple_bracket_back = '^[0-9][+*-/]\([0-9][+*-/][0-9][+*-/][0-9]\)$'
double_bracket_back = '^[0-9][+*-/][0-9][+*-/]\([0-9][+*-/][0-9]\)$'
double_bracket_front = '^\([0-9][+*-/][0-9]\)[+*-/][0-9][+*-/][0-9]$'
two_bracket = '^\([0-9][+*-/][0-9]\)[+*-/]\([0-9][+*-/][0-9]\)$'
middle_bracket = '^[0-9][+*-/]\([0-9][+*-/][0-9]\)[+*-/][0-9]$'

import re

def op_sorted(operator, seq):
    return f'{operator}'.join(sorted(seq.split(operator)))

def add_brackets(seq):
    return [f'({seq[0:5]}){seq[5:]}', f'{seq[:2]}({seq[2:]})', f'({seq[0:3]}){seq[3]}({seq[4:]})', 
            f'{seq[0:4]}({seq[4:]})', f'({seq[0:3]}){seq[3:]}', f'{seq[0:2]}({seq[2:5]}){seq[5:]}']

def remove_brackets(seq) -> list[str]:
    if re.search(triple_bracket_front, seq):
        if seq[7] in pm:
            return seq[1:6]+seq[7:]
    elif re.search(triple_bracket_back, seq):
        if seq[1] == '-':
            seq2 = seq[3:8].replace('-', 'p').replace('+', '-').replace('p', '+')
            return seq[0:2]+seq2
        elif seq[1] == '+':
            return seq[0:2]+seq[3:8]
    elif re.search(double_bracket_back, seq):
        if seq[3] == '-':
            seq2 = seq[5:8]
            seq2 = seq2.replace('-', 'p').replace('+', '-').replace('p', '+')
            return seq[0:4]+seq2
        elif seq[3] == '+':
            return seq[0:4]+seq[5:8]
    elif re.search(double_bracket_front, seq):
        if seq[5] in pm:
            return seq[1:4]+seq[5]+seq[6:10]
    elif re.search(two_bracket, seq):
        if seq[5] in pm:
           return seq[1:4]+seq[5]+seq[7:10] 
    elif re.search(middle_bracket, seq):
        if seq[1] in pm and seq[7] in pm:
            if seq[1] == '-':
                if seq[4] == '-':
                    return seq[0:2]+seq[3]+'+'+seq[5]+seq[7:]
                elif seq[4] == '+':
                    return seq[0:2]+seq[3]+'-'+seq[5]+seq[7:]
                else:
                    return seq[0:2]+seq[3:6]+seq[7:]
            elif seq[1] == '+':
                return seq[0:2]+seq[3:6]+seq[7:]
    return seq