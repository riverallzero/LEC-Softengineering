import tkinter as tk
from tkinter import simpledialog
from HW02 import gugudan as gugu

root = tk.Tk()
root.withdraw()


def gui_input(title, text):
    return simpledialog.askstring(title=title, prompt=text)


def main():
    dan = int(gui_input('구구단', '몇단을 출력할까요?'))
    gugu.gugudan_print(dan)


if __name__ == '__main__':
    main()