

def _bool():
    print("bool(None) :", bool(None))
    print("bool('0') :", bool("0"))
    print("bool(0) :", bool(0))
    print("bool('') :", bool(""))
    print("bool([]) :", bool([]))
    print("bool({}) :", bool({}))
    print("bool({''}) :", bool({''}))
    print("bool(()) :", bool(()))


def str_judge():
    print("'' == None :", "" == None)
    print("not '' :", not "")
    pass


def list_judge():
    print("[] == None :", [] == None)
    print("not [] :", not [])
    pass


def dict_judge():
    print("{} == None :", {} == None)
    print("not {} :", not {})
    pass
def main():
    print('main')
    # _bool()
    # str_judge()
    # list_judge()
    dict_judge()
    pass


if __name__ == '__main__':
    main()
