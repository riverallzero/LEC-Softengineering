import tkinter as tk
from tkinter import simpledialog

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
    dan = input_dan((gui_input('몇 단?: ')))
    for i in range(9):
        print(f'{dan} * {i + 1} = {dan * (i + 1)}')


if __name__ == '__main__':
    main()