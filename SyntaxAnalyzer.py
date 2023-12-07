import sys


class Pattern:
    def __init__(self, tag, child_nodes, conditions):
        self.tag = tag
        self.child_nodes = child_nodes
        self.conditions = conditions


patterns = [
    Pattern('<program>', ['<command_list>'], ['IDN', 'KW_FOR', '⏊']),
    Pattern('<command_list>', ['<command>', '<command_list>'], ['IDN', 'KW_FOR']),
    Pattern('<command_list>', ['$'], ['KW_ROF', '⏊']),
    Pattern('<command>', ['<assignment_op>'], ['IDN']),
    Pattern('<command>', ['<for-loop>'], ['KW_FOR']),
    Pattern('<assignment_op>', ['IDN', 'OP_ASSIGN', '<E>'], ['IDN']),
    Pattern('<for-loop>', ['KW_FOR', 'IDN', 'KW_FROM', '<E>', 'KW_TO', '<E>', '<command_list>', 'KW_ROF'], ['KW_FOR']),
    Pattern('<E>', ['<T>', '<E_list>'], ['IDN', 'NUM', 'OP_ADD', 'OP_SUB', 'LEFT_P']),
    Pattern('<E_list>', ['OP_ADD', '<E>'], ['OP_ADD']),
    Pattern('<E_list>', ['OP_SUB', '<E>'], ['OP_SUB']),
    Pattern('<E_list>', ['$'], ['IDN', 'KW_FOR', 'KW_TO', 'KW_ROF', 'RIGHT_P', '⏊']),
    Pattern('<T>', ['<P>', '<T_list>'], ['IDN', 'NUM', 'OP_ADD', 'OP_SUB', 'LEFT_P']),
    Pattern('<T_list>', ['OP_MULTIPLY', '<T>'], ['OP_MULTIPLY']),
    Pattern('<T_list>', ['OP_DIVIDE', '<T>'], ['OP_DIVIDE']),
    Pattern('<T_list>', ['$'], ['IDN', 'KW_FOR', 'KW_TO', 'KW_ROF', 'OP_ADD', 'OP_SUB', 'RIGHT_P', '⏊']),
    Pattern('<P>', ['OP_ADD', '<P>'], ['OP_ADD']),
    Pattern('<P>', ['OP_SUB', '<P>'], ['OP_SUB']),
    Pattern('<P>', ['LEFT_P', '<E>', 'RIGHT_P'], ['LEFT_P']),
    Pattern('<P>', ['IDN'], ['IDN']),
    Pattern('<P>', ['NUM'], ['NUM'])
]

tree = list()
lines = list()
space_counter = 0
current_char = ""
finished = False


def increment(value):
    global space_counter
    space_counter += value


def parse_input(target_pattern):
    global tree
    global current_char
    global result

    tree.append(" " * space_counter + target_pattern.tag)
    for child in target_pattern.child_nodes:
        if child[0] != "<":
            if child == "$":
                tree.append(" " * (space_counter + 1) + child)
                return
            else:
                tree.append(" " * (space_counter + 1) + result)
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
                if result == "":
                    print("err end")
                elif target_pattern.tag == "<T>" and len(lines) > 4:
                    print("err " + lines[-2])
                else:
                    print("err " + lines[-1])
                sys.exit()


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

parse_input(patterns[0])

if not finished:
    for line in tree:
        print(line)
