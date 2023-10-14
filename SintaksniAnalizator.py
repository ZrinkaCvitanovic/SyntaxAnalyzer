import sys


class Pattern:
    def __init__(self, tag, child_nodes, conditions):
        self.tag = tag
        self.child_nodes = child_nodes
        self.conditions = conditions


patterns = [
    Pattern('<program>', ['<lista_naredbi>'], ['IDN', 'KR_ZA', '⏊']),
    Pattern('<lista_naredbi>', ['<naredba>', '<lista_naredbi>'], ['IDN', 'KR_ZA']),
    Pattern('<lista_naredbi>', ['$'], ['KR_AZ', '⏊']),
    Pattern('<naredba>', ['<naredba_pridruzivanja>'], ['IDN']),
    Pattern('<naredba>', ['<za_petlja>'], ['KR_ZA']),
    Pattern('<naredba_pridruzivanja>', ['IDN', 'OP_PRIDRUZI', '<E>'], ['IDN']),
    Pattern('<za_petlja>', ['KR_ZA', 'IDN', 'KR_OD', '<E>', 'KR_DO', '<E>', '<lista_naredbi>', 'KR_AZ'], ['KR_ZA']),
    Pattern('<E>', ['<T>', '<E_lista>'], ['IDN', 'BROJ', 'OP_PLUS', 'OP_MINUS', 'L_ZAGRADA']),
    Pattern('<E_lista>', ['OP_PLUS', '<E>'], ['OP_PLUS']),
    Pattern('<E_lista>', ['OP_MINUS', '<E>'], ['OP_MINUS']),
    Pattern('<E_lista>', ['$'], ['IDN', 'KR_ZA', 'KR_DO', 'KR_AZ', 'D_ZAGRADA', '⏊']),
    Pattern('<T>', ['<P>', '<T_lista>'], ['IDN', 'BROJ', 'OP_PLUS', 'OP_MINUS', 'L_ZAGRADA']),
    Pattern('<T_lista>', ['OP_PUTA', '<T>'], ['OP_PUTA']),
    Pattern('<T_lista>', ['OP_DIJELI', '<T>'], ['OP_DIJELI']),
    Pattern('<T_lista>', ['$'], ['IDN', 'KR_ZA', 'KR_DO', 'KR_AZ', 'OP_PLUS', 'OP_MINUS', 'D_ZAGRADA', '⏊']),
    Pattern('<P>', ['OP_PLUS', '<P>'], ['OP_PLUS']),
    Pattern('<P>', ['OP_MINUS', '<P>'], ['OP_MINUS']),
    Pattern('<P>', ['L_ZAGRADA', '<E>', 'D_ZAGRADA'], ['L_ZAGRADA']),
    Pattern('<P>', ['IDN'], ['IDN']),
    Pattern('<P>', ['BROJ'], ['BROJ'])
]

tree = list()
lines = list()
space_counter = 0
current_char = ""
decrement = False

def increment(value):
    global space_counter
    space_counter += value

def isdecrement():
    global decrement
    return decrement


def parse_input(target_pattern):
    global tree
    global current_char
    global result


    tree.append(" " * space_counter + target_pattern.tag)
    #print(" " * space_counter + target_pattern.tag)
    for child in target_pattern.child_nodes:
        if child[0] != "<":
            if child == "$":
                tree.append(" " * (space_counter + 1) + child)
                #print(" " * (space_counter + 1) + child)
                return
            else:
                tree.append(" " * (space_counter + 1) + result)
                #print(" " * (space_counter + 1) + result)
            try:
                result = input()
            except EOFError:
                result = ""

            if result != "":
                result_splitted = result.split()
                lines.append(result)
                current_char = result_splitted[0]
            else:
                current_char = "⏊"
        else:
            valid = False
            for p in patterns:
                if p.tag == child:
                    if (current_char in p.child_nodes) or (current_char in p.conditions):
                        valid = True
                        increment(1)
                        parse_input(p)
                        increment(-1)
                        break

            if not valid:
                if result == '':
                    print('err ' + 'kraj')
                else:
                    print('err ' + lines[-1])
                sys.exit()



try:
    result = input()
except EOFError:
    result = ""
    check = isdecrement()
    if not check:
        decrement = True

if result != "":
    result_splitted = result.split()
    lines.append(result)
    current_char = result_splitted[0]
else:
    current_char = "⏊"

parse_input(patterns[0])

for line in tree:
    print(line)
