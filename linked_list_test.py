from linked_list import LinkedList

def main():
    my_list = LinkedList()

    for x in range(10, 200, 10):
        my_list.append(x)

    my_list.info()

    index = 1
    print(f'Element present at index {index}: {my_list.get(index)}')
    print(f'Value of element present at index {index}: {my_list.get_value(index)}')

    print('Adding elements to the list')
    my_list.insert(30, 1)
    my_list.insert(33, 0)
    my_list.insert(4567, 0)
    my_list.info()
    print()

    print('Removing elements from the list')
    my_list.remove(0)
    my_list.remove(13)

    my_list.info()

if _name_ == '_main_':
    main()