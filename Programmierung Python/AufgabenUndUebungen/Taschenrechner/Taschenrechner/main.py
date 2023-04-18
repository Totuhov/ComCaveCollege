from fractions import Fraction
import tkinter as tk

import window_class
from constant_class import Constant

window = window_class.Window()

# Method to format output resut to length of 16


def format_result(result):
    number = result
    formatted_number = "%.14f" % number
    truncated_number = formatted_number[:16]
    return truncated_number

# Method to check if the parameter contains any digits


def containing_numbers(number):
    my_string = number
    contains_numbers = False
    for char in my_string:
        if char.isdigit():
            contains_numbers = True
            break
    return contains_numbers

# Method to check if the parameter contains any point - "."


def containing_point(number):
    my_string = number
    contains_point = False
    for char in my_string:
        if char == '.':
            contains_point = True
            break
    return contains_point


def result(num1, num2, operator, secondOperator):
    if operator == u"\u00F7":
        result = num1 / num2
        print_result(result, secondOperator)
    if operator == u"\u00D7":
        result = num1 * num2
        print_result(result, secondOperator)
    if operator == u"\u002D":
        result = num1 - num2
        print_result(result, secondOperator)
    if operator == u"\u002B":
        result = num1 + num2
        print_result(result, secondOperator)


def print_result(result, secondOperator):
    my_float_str = str(format_result(result)).rstrip('0').rstrip('.')
    label1.config(text=my_float_str)
    if secondOperator == u"\u003D":
        secondOperator = ""
    label2.config(text=secondOperator)
    label3.config(text="")


def command_on_click(text):
    global labelMaxLength
    label1_text = label1.cget("text")  # get current text of the label
    label2_text = label2.cget("text")
    label3_text = label3.cget("text")

    #if len(labelResult_text) > 0:
    #    return

    if len(label2_text) == 0:
        if text == u"\u00F7":  # /
            label2.config(text=u"\u00F7")
            if label1_text == "":
                label1.config(text="0")
            return
        if text == u"\u00D7":  # X
            label2.config(text=u"\u00D7")
            if label1_text == "":
                label1.config(text="0")
            return
        if text == u"\u002D":  # -
            label2.config(text=u"\u002D")
            if label1_text == "":
                label1.config(text="0")
            return
        if text == u"\u002B":  # +
            label2.config(text=u"\u002B")
            if label1_text == "":
                label1.config(text="0")
            return

    if text == u"\u00B1":  # -/+
        if len(label2_text) != 0:
            if len(label3_text) > 0 and label3_text[0] == '-':
                label3_text = label3_text[1:]
                label3.config(text=label3_text)
            else:
                label3.config(text="-" + label3_text)
        else:
            if len(label1_text) > 0 and label1_text[0] == '-':
                label1_text = label1_text[1:]
                label1.config(text=label1_text)
            else:
                label1.config(text="-" + label1_text)
        return

# Result =
    if text == u"\u003D" or ((text == u"\u00F7" or text == u"\u00D7" or text == u"\u002D" or text == u"\u002B")  # =
                             and (len(label1_text) > 0 and len(label2_text) > 0 and len(label3_text) > 0)):     # =

        if not containing_numbers(label1_text) or not containing_numbers(label3_text):
            return
        num1 = Fraction(label1_text)
        num2 = Fraction(label3_text)

        if label2_text == u"\u00F7":  # /
            if int(label3_text) == 0:
                labelResult.config(
                    text="not possible")
                return

            label1.config(text=result(num1, num2, label2_text, text))
            return
        if label2_text == u"\u00D7":  # X

            label1.config(text=result(num1, num2, label2_text, text))
            return
        if label2_text == u"\u002D":  # -

            label1.config(text=result(num1, num2, label2_text, text))
            return
        if label2_text == u"\u002B":  # +

            label1.config(text=result(num1, num2, label2_text, text))
            return

    if len(label2_text) > 0:
        if not containing_numbers(text) and not containing_point(text):
            return
        if len(label3_text) == 0 and text == ".":
            label3.config(text="0.")
            return
        if len(label3_text) < 10 and ((text == "." and not containing_point(label3_text)) or text != "."):
            label3.config(text=label3_text + text)

    else:
        if len(label1_text) == 0 and text == ".":
            label1.config(text="0.")
            return
        if len(label1_text) < 10 and ((text == "." and not containing_point(label1_text)) or text != "."):
            # concatenate old text with new text
            label1.config(text=label1_text + text)


def change_label_clear():
    label1.config(text="")
    label2.config(text="")
    label3.config(text="")
    labelResult.config(text="")


labelsFrame = tk.Frame(window)
labelsFrame.pack(side=tk.TOP, pady=5)

# Text Label 1
label1 = tk.Label(window, text="",
                  width=30, font=("Arial", 20), anchor="e")
label1.pack(anchor=tk.N, pady=5, padx=20)

# Text Label 2
label2 = tk.Label(window, text="",
                  width=30, font=("Arial", 20), anchor="e")
label2.pack(anchor=tk.N, pady=5, padx=20)

# Text Label 3
label3 = tk.Label(window, text="",
                  width=30, font=("Arial", 20), anchor="e")
label3.pack(anchor=tk.N, pady=5, padx=20)

# Text Label Result
labelResult = tk.Label(window, text="",
                       width=30, font=("Arial", 20), anchor="e")
labelResult.pack(anchor=tk.N, pady=5, padx=20)

# Buttons Grid
buttonsFrame = tk.Frame(window)
buttonsFrame.pack(side=tk.BOTTOM, pady=25)

# Button 1

button1 = tk.Button(buttonsFrame, text="1", command=lambda: command_on_click(
    "1"), width=Constant.button_width(), bg=Constant.numbersColor(), font=("Arial", 20), height=Constant.button_height())
button1.grid(row=2, column=0)

# Button 2
button2 = tk.Button(buttonsFrame, text="2", command=lambda: command_on_click(
    "2"), width=Constant.button_width(), bg=Constant.numbersColor(), font=("Arial", 20), height=Constant.button_height())
button2.grid(row=2, column=1)

# Button 3
button3 = tk.Button(buttonsFrame, text="3", command=lambda: command_on_click(
    "3"), width=Constant.button_width(), bg=Constant.numbersColor(), font=("Arial", 20), height=Constant.button_height())
button3.grid(row=2, column=2)

# Button /
buttonDivide = tk.Button(buttonsFrame, text=u"\u00F7", command=lambda: command_on_click(u"\u00F7"),
                         width=Constant.button_width(), bg=Constant.operatorsColor(), font=("Arial", 20), height=Constant.button_height())
buttonDivide.grid(row=0, column=3)

# Button C
buttonC = tk.Button(buttonsFrame, text="C", command=change_label_clear,
                    width=Constant.button_width(), bg=Constant.button_C_colotr(), font=("Arial", 20), height=Constant.button_height())
buttonC.grid(row=0, column=4)

# Button 4
button4 = tk.Button(buttonsFrame, text="4", command=lambda: command_on_click(
    "4"), width=Constant.button_width(), bg=Constant.numbersColor(), font=("Arial", 20), height=Constant.button_height())
button4.grid(row=1, column=0)

# Button 5
button5 = tk.Button(buttonsFrame, text="5", command=lambda: command_on_click(
    "5"), width=Constant.button_width(), bg=Constant.numbersColor(), font=("Arial", 20), height=Constant.button_height())
button5.grid(row=1, column=1)

# Button 6
button6 = tk.Button(buttonsFrame, text="6", command=lambda: command_on_click(
    "6"), width=Constant.button_width(), bg=Constant.numbersColor(), font=("Arial", 20), height=Constant.button_height())
button6.grid(row=1, column=2)

# Button X
buttonMulti = tk.Button(buttonsFrame, text=u"\u00D7", command=lambda: command_on_click(
    u"\u00D7"), width=Constant.button_width(), bg=Constant.operatorsColor(), font=("Arial", 20), height=Constant.button_height())
buttonMulti.grid(row=1, column=3)

# Button =
buttonResult = tk.Button(buttonsFrame, text=u"\u003D", command=lambda: command_on_click(
    u"\u003D"), width=Constant.button_width(), bg=Constant.operatorsColor(), font=("Arial", 20), height=2)
buttonResult.grid(row=1, column=4, rowspan=3, ipady=40)

# Button 7
button7 = tk.Button(buttonsFrame, text="7", command=lambda: command_on_click(
    "7"), width=Constant.button_width(), bg=Constant.numbersColor(), font=("Arial", 20), height=Constant.button_height())
button7.grid(row=0, column=0)

# Button 8
button8 = tk.Button(buttonsFrame, text="8", command=lambda: command_on_click(
    "8"), width=Constant.button_width(), bg=Constant.numbersColor(), font=("Arial", 20), height=Constant.button_height())
button8.grid(row=0, column=1)

# Button 9
button9 = tk.Button(buttonsFrame, text="9", command=lambda: command_on_click(
    "9"), width=Constant.button_width(), bg=Constant.numbersColor(), font=("Arial", 20), height=Constant.button_height())
button9.grid(row=0, column=2)

# Button -
buttonMinus = tk.Button(buttonsFrame, text=u"\u002D", command=lambda: command_on_click(
    u"\u002D"), width=Constant.button_width(), bg=Constant.operatorsColor(), font=("Arial", 20), height=Constant.button_height())
buttonMinus.grid(row=2, column=3)

# Button -/+
buttonChange = tk.Button(buttonsFrame, text=u"\u00B1", command=lambda: command_on_click(
    u"\u00B1"), width=Constant.button_width(), bg=Constant.operatorsColor(), font=("Arial", 20), height=Constant.button_height())
buttonChange.grid(row=3, column=0)

# Button 0
button0 = tk.Button(buttonsFrame, text="0", command=lambda: command_on_click(
    "0"), width=Constant.button_width(), bg=Constant.numbersColor(), font=("Arial", 20), height=Constant.button_height())
button0.grid(row=3, column=1)

# Button .
buttonPoint = tk.Button(buttonsFrame, text=".", command=lambda: command_on_click(
    "."), width=Constant.button_width(), bg=Constant.operatorsColor(), font=("Arial", 20), height=Constant.button_height())
buttonPoint.grid(row=3, column=2)

# Button +
buttonplus = tk.Button(buttonsFrame, text=u"\u002B", command=lambda: command_on_click(
    u"\u002B"), width=Constant.button_width(), bg=Constant.plusColor(), font=("Arial", 20), height=Constant.button_height())
buttonplus.grid(row=3, column=3)

window.mainloop()
