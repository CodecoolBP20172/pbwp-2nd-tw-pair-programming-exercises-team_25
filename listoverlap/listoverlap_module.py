import random


def listoverlap(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 & set2)  # return list(set(list1) & set(list2))


def create_list():
    return [random.randint(1, 100) for i in range(random.randint(10, 20))]


def main():
    list1 = []
    for i in range(random.randint(10, 20)):
        list1.append(random.randint(1, 100))
    # list1 = [random.randint(1, 100) for i in range(random.randint(10, 20))]
    # list1 = create_list
    list2 = []
    for i in range(random.randint(10, 20)):
        list2.append(random.randint(1, 100))
    # list2 = [random.randint(1, 100) for i in range(random.randint(10, 20))]
    # list2 = create_list
    overlap = listoverlap(list1, list2)
    print(list1)
    print(list2)
    print(overlap)
    return


if __name__ == '__main__':
    main()
