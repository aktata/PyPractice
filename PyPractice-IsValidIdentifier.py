import keyword
import string


def is_valid_identifier(s):
    keywords = keyword.kwlist
    if s in keywords:
        return False
    elif s[0] == '_' or s[0] in string.ascii_letters:
        for i in s:
            if i == '_' or i in string.ascii_letters or i in string.digits:
                pass
            else:
                return False
        return True
    else:
        return False


def main():
    s = input()
    while True:
        print(is_valid_identifier(s))


if __name__ == '__main__':
    main()
