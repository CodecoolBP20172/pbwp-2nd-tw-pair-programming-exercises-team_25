def palindrome(str):
    pal = ''
    for i in str:
        if i.isalnum():
            pal += i.lower()
    # pal = ''.join([i.lower() for i in str if i.isalnum()])
    # print(pal)
    # print(pal[-2])
    for i in range(len(pal) // 2):
        if pal[i] != pal[-(i + 1)]:
            return False
    return True


def main():
    # palindrome("A nut for a jar of tuna")
    return


if __name__ == '__main__':
    main()
