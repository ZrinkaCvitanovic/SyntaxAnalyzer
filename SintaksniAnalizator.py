space_counter = 0
tree = open("../tree.txt", "w")


def increment(value):
    global space_counter
    space_counter = space_counter + value


def iskeyword(line):
    return line.startswith("KR")


def define_command(line):
    found = False
    if not line or len(line[0]) < 1:
        tree.write(" " * space_counter + "$" + "\n")
        return False

    for current_command in line:
        command = current_command.split()[0]
        if command == "OP_PRIDRUZI":
            found = assign_operator(line)
            return found
        elif command == "OP_PLUS":
            found = plus_operator(line)
        elif command == "OP_MINUS":
            found = minus_operator(line)
        elif command == "OP_PUTA":
            found = multiply_operator(line)
        elif command == "OP_DIJELI":
            found = divide_operator(line)
        elif command == "KR_ZA":
            found = for_loop(line)

    # if no operator is found
    if not found and line:
        err_msg = line[0].split()
        # write the information about a previously read character (hence the 0)
        print("err", err_msg[0], err_msg[1], err_msg[2])
    return found


def assign_operator(line):
    if len(line) < 3:
        err_msg = line[0].split()
        print("err", err_msg[0], err_msg[1], err_msg[2])
        return False
    tree.write(" " * space_counter + "<naredba>" + "\n")
    tree.write(" " * space_counter + " <naredba_pridruzivanja>" + "\n")
    increment(2)
    prefix = " " * space_counter
    tree.write(prefix + line[0] + "\n")
    tree.write(prefix + line[1] + "\n")
    if line[2]:
        tree.write(prefix + "<E>" + "\n")
        tree.write(prefix + " <T>" + "\n")
        tree.write(prefix + "  <P>" + "\n")
        increment(2)
        prefix =" " * space_counter
        tree.write(prefix + " " + line[2] + "\n")
        tree.write(prefix + "<T_lista>" + "\n")
        if len(line) <= 3:
            tree.write(prefix + " $" + "\n")
            increment(-1)
            prefix = " "*space_counter
            tree.write(prefix + "<E_lista>" + "\n")
            tree.write(prefix + " $" + "\n")
        increment(-4)

        return True


def plus_operator(line):
    increment(1)


def minus_operator(line):
    increment(1)


def multiply_operator(line):
    increment(1)


def divide_operator(line):
    increment(1)


def for_loop(line):
    increment(1)


def main():
    tree.write("<program>" + "\n")
    line_counter = 1
    line_num = 1
    current_line = list()
    finished = False
    while True:
        if finished:
            break
        while line_counter == line_num:
            next_line = list()
            try:
                line = input()
                if not line or line.isspace():
                    finished = True
                    break
                if len(line.split()) < 1:
                    print("err")
                    return
                else:
                    line_num = int(line.split()[1])
                if line_num == line_counter:
                    current_line.append(line)
                else:  # finished reading the entire line
                    line_counter += 1
                    next_line.append(line)
                    increment(1)
                    tree.write(" " * space_counter + "<lista_naredbi>\n")
                    increment(1)
                    comm = define_command(current_line)
                    if not comm:
                        return
                    current_line = next_line  # in order to remember the last line I read
            except EOFError:
                break

    #if current_line:
    increment(1)
    tree.write(" "*space_counter + "<lista_naredbi>\n")
    increment(1)
    one_more = define_command(current_line)
    current_line = list()
    while one_more:
        increment(1)
        tree.write(" " * space_counter + "<lista_naredbi>\n")
        increment(1)
        one_more = define_command(current_line)
    tree.close()

    with open("../tree.txt", "r") as print_tree:
        lines = print_tree.readlines()
        for line in lines:
            print(line, end="")
        print("\n")


if __name__ == "__main__":
    main()

