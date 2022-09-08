def cal_factorial1(num):
    result = 1
    for i in range(1, num+1):
        result *= i

    return result


def cal_factorial2(num):
    if num == 1:
        return 1

    return num * cal_factorial1(num-1)


def main():
    num = 5
    print(f'{num}! = {cal_factorial1(num)}')
    print(f'{num}! = {cal_factorial2(num)}')


if __name__ == '__main__':
    main()