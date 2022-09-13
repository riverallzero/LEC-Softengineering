def gugudan_print(dan):
    for i in range(9):
        print(f'{dan} * {i+1} = {dan * (i + 1)}')


def main():
    dan = int(input())
    gugudan_print(dan)


if __name__ == '__main__':
    main()
