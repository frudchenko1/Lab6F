def encode_pass(password):
    res = ""

    for i in password:
        res += str(int(i) + 3)

    return res


def main():
    while True:
        print('''\nMenu
-------------
1. Encode
2. Decode
3. Quit
        ''')
        menu_option = int(input('Please enter an option: '))
        if menu_option == 1:
            password = input('Please enter your password to encode: ')
            encoded_pass = encode_pass(password)
            print("Your password has been encoded and stored!")


if __name__ == '__main__':
    main()
