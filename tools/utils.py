from os import system, name

def clrscr():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def menu(options):
    i = 0
    for option in options:
        print(str(i + 1) + '. ' + option)
        i += 1
    valid = False
    while not valid:
        op = int(input("Choose a valid option: "))
        valid = op > 0 and op <= i
    return op
