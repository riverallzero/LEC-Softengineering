def input_dan_1(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError as e:
            print(e)
            print('정수를 입력하세요.')


def input_dan_2(prompt):
    while True:
        value = input(prompt)
        try:
            value = int(value)
            if 2 <= value <= 9:
                return value

        except ValueError as e:
            print(e)
        print('2~9까지 자연수를 입력하세요.')


def main():
    dan1 = input_dan_1('몇 단?: ')
    for i in range(9):
        print(f'{dan1} * {i+1} = {dan1 * (i + 1)}')

    # dan2 = input_dan_2('몇 단?: ')
    # for r in range(9):
    #     print(f'{dan2} * {r+1} = {dan2 * (r + 1)}')


if __name__ == '__main__':
    main()