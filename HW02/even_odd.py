def check_num(num):
    if num % 2 == 0:
        result = f'{num}은 짝수입니다.'
    else:
        result = f'{num}은 홀수입니다.'

    return result


def main():
    num = int(input('값을 입력하세요. : '))
    print(check_num(num))


if __name__ == '__main__':
    main()