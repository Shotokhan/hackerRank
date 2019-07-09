from hard.array_manipulation import SLinkedList


def run():
    llist = SLinkedList()
    llist.add_interval(2, 6, 8)
    llist.print()

    llist.add_interval(3, 5, 7)
    llist.print()

    llist.add_interval(1, 8, 1)
    llist.print()

    llist.add_interval(5, 9, 15)
    llist.print()

if __name__ == '__main__':
    run()