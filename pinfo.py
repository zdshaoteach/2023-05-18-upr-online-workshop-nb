import sys

name = 'Doris'

def get_name():
    return name


def change_name(new_name):
    global name
    name = new_name

if __name__ == '__main__':
    print(sys.argv)
    for i in sys.argv[1:]:
        print(i)
    print(name)