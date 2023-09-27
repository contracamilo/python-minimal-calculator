import tkinter
from tkinter import *
from operations import Calculator


def py_calculator():
    global equation
    equation = ""
    root = tkinter.Tk()

    def clear():
        global equation
        equation = ""
        result_box.config(text=equation)

    def type_text(button_text):
        global equation
        equation += button_text
        result_box.config(text=equation)

    def calculate():
        global equation
        calc = Calculator(equation)
        result = calc.evaluate()
        result_box.config(text=result)

    root.title("calculadora")
    root.geometry("500x710+100+200")
    root.resizable(False, False)
    root.configure(bg="#3e3a79")

    # fields
    result_box = Label(root, width=100, height=2, text=equation, font=("helvetica", 40), bg="#fff", fg="#3e3a79")
    result_box.pack()

    c_button = Button(root, width=5, height=3, text="C", font=("helvetica", 30, "bold"), bd=1, fg="#3e3a79",
                      bg="#ef9556", command=lambda: clear())
    c_button.place(x=10, y=120)

    slash_button = Button(root, width=5, height=3, text="/", font=("helvetica", 30, "bold"), bd=1, fg="#3e3a79",
                          bg="#e78baf", command=lambda: type_text("/"))
    slash_button.place(x=130, y=120)

    module_button = Button(root, width=5, height=3, text="%", font=("helvetica", 30, "bold"), bd=1, fg="#3e3a79",
                           bg="#e78baf", command=lambda: type_text("%"))
    module_button.place(x=250, y=120)

    factorial_button = Button(root, width=5, height=3, text="!", font=("helvetica", 30, "bold"), bd=1, fg="#3e3a79",
                              bg="#e78baf", command=lambda: type_text("!"))
    factorial_button.place(x=370, y=120)

    seven_button = Button(root, width=5, height=3, text="7", font=("helvetica", 30, "bold"), bd=1, fg="#3e3a79",
                          bg="#ef9556", command=lambda: type_text("7"))
    seven_button.place(x=10, y=238)

    eight_button = Button(root, width=5, height=3, text="8", font=("helvetica", 30, "bold"), bd=1, fg="#3e3a79",
                          bg="#e78baf", command=lambda: type_text("8"))
    eight_button.place(x=130, y=238)

    nine_button = Button(root, width=5, height=3, text="9", font=("helvetica", 30, "bold"), bd=1, fg="#3e3a79",
                         bg="#e78baf", command=lambda: type_text("9"))
    nine_button.place(x=250, y=238)

    mult_button = Button(root, width=5, height=3, text="X", font=("helvetica", 30, "bold"), bd=1, fg="#3e3a79",
                         bg="#e78baf", command=lambda: type_text("*"))
    mult_button.place(x=370, y=238)

    four_button = Button(root, width=5, height=3, text="4", font=("helvetica", 30, "bold"), bd=1, fg="#3e3a79",
                         bg="#ef9556", command=lambda: type_text("4"))
    four_button.place(x=10, y=355)

    five_button = Button(root, width=5, height=3, text="5", font=("helvetica", 30, "bold"), bd=1, fg="#3e3a79",
                         bg="#e78baf", command=lambda: type_text("5"))
    five_button.place(x=130, y=355)

    six_button = Button(root, width=5, height=3, text="6", font=("helvetica", 30, "bold"), bd=1, fg="#3e3a79",
                        bg="#e78baf", command=lambda: type_text("6"))
    six_button.place(x=250, y=355)

    minus_button = Button(root, width=5, height=3, text="-", font=("helvetica", 30, "bold"), bd=1, fg="#3e3a79",
                          bg="#e78baf", command=lambda: type_text("-"))
    minus_button.place(x=370, y=355)

    one_button = Button(root, width=5, height=3, text="1", font=("helvetica", 30, "bold"), bd=1, fg="#3e3a79",
                        bg="#ef9556", command=lambda: type_text("1"))
    one_button.place(x=10, y=472)

    two_button = Button(root, width=5, height=3, text="2", font=("helvetica", 30, "bold"), bd=1, fg="#3e3a79",
                        bg="#e78baf", command=lambda: type_text("2"))
    two_button.place(x=130, y=472)

    three_button = Button(root, width=5, height=3, text="3", font=("helvetica", 30, "bold"), bd=1, fg="#3e3a79",
                          bg="#e78baf", command=lambda: type_text("3"))
    three_button.place(x=250, y=472)

    plus_button = Button(root, width=5, height=3, text="+", font=("helvetica", 30, "bold"), bd=1, fg="#3e3a79",
                         bg="#e78baf", command=lambda: type_text("+"))
    plus_button.place(x=370, y=472)

    zero_button = Button(root, width=12, height=3, text="0", font=("helvetica", 30, "bold"), bd=1, fg="#3e3a79",
                         bg="#ef9556", command=lambda: type_text("0"))
    zero_button.place(x=10, y=590)

    dot_button = Button(root, width=5, height=3, text=".", font=("helvetica", 30, "bold"), bd=1, fg="#3e3a79",
                        bg="#e78baf", command=lambda: type_text("."))
    dot_button.place(x=250, y=590)

    equal_button = Button(root, width=5, height=3, text="=", font=("helvetica", 30, "bold"), bd=1, fg="#3e3a79",
                          bg="#e78baf", command=lambda: calculate())
    equal_button.place(x=370, y=590)

    root.mainloop()
