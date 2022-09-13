import tkinter as tk
from tkinter import simpledialog
from rich import print

root = tk.Tk()
root.withdraw()


def gui_input(text):
    return simpledialog.askstring(title='구구단', prompt=text)


def input_dan(prompt):
    while True:
        try:
            return int(gui_input(prompt))
        except ValueError as e:
            print(e)
            print('정수를 입력하세요.')


def main():
    dan = int(gui_input('몇 단?: '))
    for i in range(9):
        print('{} * {} = [bold magenta]{}[/bold magenta]'.format(dan, i + 1, dan * (i + 1)))

    from rich.panel import Panel
    print(Panel.fit(f'구구단 [red]{dan}단!', border_style='red'))
    print(Panel.fit('\n'.join(['{} * {} = {}'.format(dan, i + 1, dan * (i + 1)) for i in range(9)])))


if __name__ == '__main__':
    main()