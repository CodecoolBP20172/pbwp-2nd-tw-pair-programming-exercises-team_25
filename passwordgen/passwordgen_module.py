import random


def passwordgen():
    string = ''
    spec_char = '!@#$%^&*()?'
    for i in range(random.randint(8, 16)):
        if i % 4 == 0:
            string += chr(random.randint(97, 122))
        elif i % 4 == 1:
            string += chr(random.randint(65, 90))
        elif i % 4 == 2:
            string += str(random.randint(0, 9))
        elif i % 4 == 3:
            string += spec_char[random.randint(0, len(spec_char) - 1)]
    print(string)
    return string


def main():
    # for i in range(10):
    #     passwordgen()
    return


if __name__ == '__main__':
    main()
