def main():
    total = 0
    for i in range(1, 101):
        if i % 2 == 0:
            total += i
    print(f'1부터 100까지의 합 : {total}')

    print(f'1부터 100까지의 합 : {sum([i for i in range(1, 101) if i % 2 == 0])}')


if __name__ == '__main__':
    main()