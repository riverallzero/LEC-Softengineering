import os


def main():
    output_dir = '../Output/HW04/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    dan = 5
    color = 'blue'

    with open(os.path.join(output_dir, 'gugu.html'), 'w') as f:
        f.write('<html>\n')
        f.write('<body>\n')
        for i in range(9):
            f.write(f'<p>{dan} * {i + 1} = <font color={color}>{dan * (i + 1)}</font></p>\n')
        f.write('</body>\n')
        f.write('</html>')


if __name__ == '__main__':
    main()