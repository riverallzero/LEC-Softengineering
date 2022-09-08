def is_primenumber(num):
    for i in range(2, num):
        if num % i == 0:
           return False

    return True


def main():
    # 100 < num < 200에서 소수의 개수 구하기
    primenumber_list = []

    for n in range(100, 200):
        if is_primenumber(n):
            primenumber_list.append(n)

    print('100부터 200까지의 소수 개수 : {}'.format(len(primenumber_list)))


if __name__ == '__main__':
    main()