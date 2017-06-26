import datetime


def years(age):
    year = datetime.datetime.today().year
    return year + (100 - age)


def main():
    while True:
        try:
            name = input("Please give us your name: ")
            age = int(input("Please give us your age: "))
            copies = int(input("Copies of the message: "))
        except ValueError:
            print('Invalid input!')
            continue
        message = '{} will be 100 in {}.'.format(name, years(age))
        print(message * copies)
        print((message + '\n') * copies)
        for i in range(copies):
            print(message)
        break
    return


if __name__ == '__main__':
    main()
