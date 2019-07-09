# from hard.array_manipulation import SLinkedList
from extreme.intervals_tree import IntTree

LIST_TESTS = [4]
PREFIX = 'array_manipulation_'


def test_array_manipulation():
    for test in LIST_TESTS:
        with open(f'data/{PREFIX}{test}.input') as file:
            tree = IntTree()
  #          llist = SLinkedList()
            count = 0
            for line in file:
                #print('------------------------------------')
                #print(f'--> Count {count} - {line}')
                tree.add_node(*list(map(int, line.rstrip().split())))
#                llist.add_interval(*list(map(int, line.rstrip().split())))
                #tree.print()

                #llist.print()

                #print(count)
                count += 1

  #          max_value = llist.max_value()
            max_value = tree.maximum

            with open(f'data/{PREFIX}{test}.output') as file_out:
                assert int(file_out.readline()) == max_value, 'Max value is incorrect'
