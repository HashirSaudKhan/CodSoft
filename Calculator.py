import tkinter
from tkinter import *
from tkinter import messagebox


# Global variables
val = ""
A = 0
operator = " "

# Functions to show value in Label


def btn_1_is_clicked():
    global val
    val = val + "1"
    data.set(val)


def btn_2_is_clicked():
    global val
    val = val + "2"
    data.set(val)


def btn_3_is_clicked():
    global val
    val = val + "3"
    data.set(val)


def btn_4_is_clicked():
    global val
    val = val + "4"
    data.set(val)


def btn_5_is_clicked():
    global val
    val = val + "5"
    data.set(val)


def btn_6_is_clicked():
    global val
    val = val + "6"
    data.set(val)


def btn_7_is_clicked():
    global val
    val = val + "7"
    data.set(val)


def btn_8_is_clicked():
    global val
    val = val + "8"
    data.set(val)


def btn_9_is_clicked():
    global val
    val = val + "9"
    data.set(val)


def btn_0_is_clicked():
    global val
    val = val + "0"
    data.set(val)


def btn_plus_is_clicked():
    global val
    global A
    global operator
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)


def btn_minus_is_clicked():
    global val
    global A
    global operator
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)


def btn_multiplyer_is_clicked():
    global val
    global A
    global operator
    A = int(val)
    operator = "x"
    val = val + "x"
    data.set(val)


def btn_divide_is_clicked():
    global val
    global A
    global operator
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)


def btn_clear_clicked():
    global A
    global val
    global operator
    val = ""
    A = 0
    operator = ""
    data.set(val)

# Backend result function
def btn_equal_clicked():
    global A
    global val
    global operator
    new_val = val
    if operator == "+":
        # e.g -> new_val = "12+3" -> second_value = int(new_val.split("+")[1]) -> second_value = 3
        second_value = int(new_val.split("+")[1])
        add = A + second_value
        data.set(add)
        val = str(add)

    elif operator == "-":
        # e.g -> new_val = "12+3" -> second_value = int(new_val.split("+")[1]) -> second_value = 3
        second_value = int(new_val.split("-")[1])
        minus = A - second_value
        data.set(minus)
        val = str(minus)

    elif operator == "x":
        # e.g -> new_val = "12+3" -> second_value = int(new_val.split("+")[1]) -> second_value = 3
        second_value = int(new_val.split("x")[1])
        multiplyer = A * second_value
        data.set(multiplyer)
        val = str(multiplyer)

    elif operator == "/":
        # e.g -> new_val = "12+3" -> second_value = int(new_val.split("+")[1]) -> second_value = 3
        second_value = int(new_val.split("/")[1])
        if second_value == 0:
            A = 0
            val = " "
            data.set(val)
            messagebox.showerror("Error", "Division by zero not support")

        else:
            divide = (A / second_value)
            d = float("{:.2f}".format(divide))
            data.set(d)
            val = str(d)


# Window Design
root = tkinter.Tk()
root.geometry("250x400+550+175")  # Use to open a window in mid
root.resizable(0, 0)  # Use for not resizing
root.title("Calculator")  # Window Title


# EVENTS
# Cursor Entered
def cursor_entered_btn1(event):
    btn1.config(
        bg="white"
    )


def cursor_entered_btn2(event):
    btn2.config(
        bg="white"
    )


def cursor_entered_btn3(event):
    btn3.config(
        bg="white"
    )


def cursor_entered_btn_plus(event):
    btn_plus.config(
        bg="white"
    )


def cursor_entered_btn4(event):
    btn4.config(
        bg="white"
    )


def cursor_entered_btn5(event):
    btn5.config(
        bg="white"
    )


def cursor_entered_btn6(event):
    btn6.config(
        bg="white"
    )


def cursor_entered_btn7(event):
    btn7.config(
        bg="white"
    )


def cursor_entered_btn8(event):
    btn8.config(
        bg="white"
    )


def cursor_entered_btn9(event):
    btn9.config(
        bg="white"
    )


def cursor_entered_btn_minus(event):
    btn_minus.config(
        bg="white"
    )


def cursor_entered_btn_multiply(event):
    btn_multiplyer.config(
        bg="white"
    )


def cursor_entered_btn_divide(event):
    btn_divide.config(
        bg="white"
    )


def cursor_entered_btn_C(event):
    btn_c.config(
        bg="white"
    )


def cursor_entered_btn_equal(event):
    btn_equal.config(
        bg="white"
    )


def cursor_entered_btn0(event):
    btn_0.config(
        bg="white"
    )

# Cursor LEAVED


def cursor_leaved_btn1(event):
    btn1.config(
        bg="#F0F0F0"
    )


def cursor_leaved_btn2(event):
    btn2.config(
        bg="#F0F0F0"
    )


def cursor_leaved_btn3(event):
    btn3.config(
        bg="#F0F0F0"
    )


def cursor_leaved_btn_plus(event):
    btn_plus.config(
        bg="#F0F0F0"
    )


def cursor_leaved_btn4(event):
    btn4.config(
        bg="#F0F0F0"
    )


def cursor_leaved_btn5(event):
    btn5.config(
        bg="#F0F0F0"
    )


def cursor_leaved_btn6(event):
    btn6.config(
        bg="#F0F0F0"
    )


def cursor_leaved_btn7(event):
    btn7.config(
        bg="#F0F0F0"
    )


def cursor_leaved_btn8(event):
    btn8.config(
        bg="#F0F0F0"
    )


def cursor_leaved_btn9(event):
    btn9.config(
        bg="#F0F0F0"
    )


def cursor_leaved_btn_minus(event):
    btn_minus.config(
        bg="#F0F0F0"
    )


def cursor_leaved_btn_multiply(event):
    btn_multiplyer.config(
        bg="#F0F0F0"
    )


def cursor_leaved_btn_divide(event):
    btn_divide.config(
        bg="#F0F0F0"
    )


def cursor_leaved_btn_C(event):
    btn_c.config(
        bg="#F0F0F0"
    )


def cursor_leaved_btn_equal(event):
    btn_equal.config(
        bg="#F0F0F0"
    )


def cursor_leaved_btn0(event):
    btn_0.config(
        bg="#F0F0F0"
    )


data = StringVar()
lbl = Label(
    root,
    text="Label",
    # ancher defines the location of label, SE means South East (bottom right)
    anchor=SE,
    font=("verdana", 20),
    textvariable=data,
    bg="white",
    fg="#000000",
    height=2,

)
lbl.pack(expand=True, fill="both")

#Dividing calculator window in multiple frames with the help of Frame() method

# Frame for Row 1 all buttons
btnrow1 = Frame(root, bg="Black")
btnrow1.pack(expand=True, fill="both")

# Frame for Row 2 all buttons
btnrow2 = Frame(root, bg="Pink")
btnrow2.pack(expand=True, fill="both")

# Frame for Row 3 all buttons
btnrow3 = Frame(root, bg="Yellow")
btnrow3.pack(expand=True, fill="both")

# Frame for Row 4 all buttons
btnrow4 = Frame(root, bg="Grey")
btnrow4.pack(expand=True, fill="both")


# Frame 1 Button 1 2 3 +
btn1 = Button(
    btnrow1,
    text="1",
    fg="#00BFFF",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_1_is_clicked,
)
btn1.pack(side=LEFT, expand=True, fill="both")
btn1.bind("<Enter>", cursor_entered_btn1)
btn1.bind("<Leave>", cursor_leaved_btn1)

btn2 = Button(
    btnrow1,
    text="2",
    fg="#00BFFF",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_2_is_clicked,
)
btn2.pack(side=LEFT, expand=True, fill="both")
btn2.bind("<Enter>", cursor_entered_btn2)
btn2.bind("<Leave>", cursor_leaved_btn2)

btn3 = Button(
    btnrow1,
    text="3",
    fg="#00BFFF",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_3_is_clicked,
)
btn3.pack(side=LEFT, expand=True, fill="both")
btn3.bind("<Enter>", cursor_entered_btn3)
btn3.bind("<Leave>", cursor_leaved_btn3)

btn_plus = Button(
    btnrow1,
    text="+",
    fg="#9400D3",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_plus_is_clicked,

)
btn_plus.pack(side=LEFT, expand=True, fill="both")
btn_plus.bind("<Enter>", cursor_entered_btn_plus)
btn_plus.bind("<Leave>", cursor_leaved_btn_plus)


# Frame 2 Button 4 5 6 -
btn4 = Button(
    btnrow2,
    text="4",
    fg="#00BFFF",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_4_is_clicked,
)
btn4.pack(side=LEFT, expand=True, fill="both")
btn4.bind("<Enter>", cursor_entered_btn4)
btn4.bind("<Leave>", cursor_leaved_btn4)


btn5 = Button(
    btnrow2,
    text="5",
    fg="#00BFFF",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_5_is_clicked,
)
btn5.pack(side=LEFT, expand=True, fill="both")
btn5.bind("<Enter>", cursor_entered_btn5)
btn5.bind("<Leave>", cursor_leaved_btn5)

btn6 = Button(
    btnrow2,
    text="6",
    fg="#00BFFF",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_6_is_clicked,
)
btn6.pack(side=LEFT, expand=True, fill="both")
btn6.bind("<Enter>", cursor_entered_btn6)
btn6.bind("<Leave>", cursor_leaved_btn6)


btn_minus = Button(
    btnrow2,
    text="-",
    fg="#9400D3",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_minus_is_clicked,

)
btn_minus.pack(side=LEFT, expand=True, fill="both")
btn_minus.bind("<Enter>", cursor_entered_btn_minus)
btn_minus.bind("<Leave>", cursor_leaved_btn_minus)


# Frame 3 Button 7 8 9 X
btn7 = Button(
    btnrow3,
    text="7",
    fg="#00BFFF",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_7_is_clicked,
)
btn7.pack(side=LEFT, expand=True, fill="both")
btn7.bind("<Enter>", cursor_entered_btn7)
btn7.bind("<Leave>", cursor_leaved_btn7)


btn8 = Button(
    btnrow3,
    text="8",
    fg="#00BFFF",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_8_is_clicked,
)
btn8.pack(side=LEFT, expand=True, fill="both")
btn8.bind("<Enter>", cursor_entered_btn8)
btn8.bind("<Leave>", cursor_leaved_btn8)


btn9 = Button(
    btnrow3,
    text="9",
    fg="#00BFFF",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_9_is_clicked,
)
btn9.pack(side=LEFT, expand=True, fill="both")
btn9.bind("<Enter>", cursor_entered_btn9)
btn9.bind("<Leave>", cursor_leaved_btn9)


btn_multiplyer = Button(
    btnrow3,
    text="x",
    fg="#9400D3",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_multiplyer_is_clicked,
)
btn_multiplyer.pack(side=LEFT, expand=True, fill="both")
btn_multiplyer.bind("<Enter>", cursor_entered_btn_multiply)
btn_multiplyer.bind("<Leave>", cursor_leaved_btn_multiply)


# Frame 4 Button C 0 = /
btn_c = Button(
    btnrow4,
    text="C",
    fg="#9400D3",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_clear_clicked

)
btn_c.pack(side=LEFT, expand=True, fill="both")
btn_c.bind("<Enter>", cursor_entered_btn_C)
btn_c.bind("<Leave>", cursor_leaved_btn_C)

btn_0 = Button(
    btnrow4,
    text="0",
    fg="#00BFFF",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_0_is_clicked,
)
btn_0.pack(side=LEFT, expand=True, fill="both")
btn_0.bind("<Enter>", cursor_entered_btn0)
btn_0.bind("<Leave>", cursor_leaved_btn0)


btn_equal = Button(
    btnrow4,
    text="=",
    fg="#9400D3",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_equal_clicked,
)
btn_equal.pack(side=LEFT, expand=True, fill="both")
btn_equal.bind("<Enter>", cursor_entered_btn_equal)
btn_equal.bind("<Leave>", cursor_leaved_btn_equal)

btn_divide = Button(
    btnrow4,
    text="/",
    fg="#9400D3",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_divide_is_clicked,


)
btn_divide.pack(side=LEFT, expand=True, fill="both")
btn_divide.bind("<Enter>", cursor_entered_btn_divide)
btn_divide.bind("<Leave>", cursor_leaved_btn_divide)


root.mainloop()
