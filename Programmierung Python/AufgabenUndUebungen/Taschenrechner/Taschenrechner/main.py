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
    labelWarnings.config(text="")


def change_label_clear():
    label1.config(text="0")
    clear_last_3_labels()


def change_label_clear_with_text(text):
    label1.config(text=text)
    clear_last_3_labels()


def clear_last_3_labels():
    label2.config(text="")
    label3.config(text="")
    labelWarnings.config(text="")


def command_on_click(text):
    label1_text = label1.cget("text")  # get current text of all lables
    label2_text = label2.cget("text")
    label3_text = label3.cget("text")
    labelWarnings_text = labelWarnings.cget("text")

    if labelWarnings_text == "not possible":
        change_label_clear_with_text(label1_text)
        return
    # with this check first number will be overwriten if it's 0
    if len(label2_text) == 0 and label1_text == "0" and containing_numbers(text):
        # there is no possibility to write something like 01 or 003
        label1.config(text=text)
        # the zero in the beginning will be ignored and not shown on the screen
        return
    # the same with the second operand
    if len(label2_text) > 0 and label3_text == "0" and containing_numbers(text):
        label3.config(text=text)
        return

    # Check if allreagy has a operator and set or replace it if not
    if len(label3_text) == 0 and (text == u"\u00F7" or text == u"\u00D7" or text == u"\u002D" or text == u"\u002B"):
        label2.config(text=text)
        return

    if text == u"\u00B1":  # -/+
        if len(label2_text) != 0:
            # check if there is a text in the field and if not did not let to take negative sign
            if label3_text == "":          
                return
            # check if there is a number equal to zero in the field end if did not let to take negative sign
            if Fraction(label3_text) == 0:
                return
            if len(label3_text) > 0 and label3_text[0] == '-':
                label3_text = label3_text[1:]
                label3.config(text=label3_text)
            else:
                label3.config(text="-" + label3_text)
        else:
            if label1_text == "":
                return
            if Fraction(label1_text) == 0:
                return
            if len(label1_text) > 0 and label1_text[0] == '-':
                label1_text = label1_text[1:]
                label1.config(text=label1_text)
            else:
                label1.config(text="-" + label1_text)
        return

# Result =
    if text == u"\u003D" or ((text == u"\u00F7" or text == u"\u00D7" or text == u"\u002D" or text == u"\u002B")
                             and (len(label2_text) > 0 and len(label3_text) > 0)):

        if not containing_numbers(label3_text):
            return
        # both of the operants are parsed in floating point data type of Fraction
        num1 = Fraction(label1_text)
        num2 = Fraction(label3_text)

        if label2_text == u"\u00F7":  # /
            if Fraction(label3_text) == 0:
                labelWarnings.config(
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


labelsFrame = tk.Frame(window, bg="white")
labelsFrame.pack(side=tk.TOP, pady=15)

# Text Label 1
label1 = tk.Label(labelsFrame, text="0",
                  width=30, font=("Arial", 20), anchor="e", bg="#dadde3")
label1.pack(anchor=tk.N, pady=0, padx=20)

# Text Label 2 operator
label2 = tk.Label(labelsFrame, text="",
                  width=30, font=("Arial", 20), anchor="e", bg="#dadde3")
label2.pack(anchor=tk.N, pady=0, padx=20)

# Text Label 3
label3 = tk.Label(labelsFrame, text="",
                  width=30, font=("Arial", 20), anchor="e", bg="#dadde3")
label3.pack(anchor=tk.N, pady=0, padx=20)

# Text Label Warnings
labelWarnings = tk.Label(labelsFrame, text="",
                         width=30, font=("Arial", 20), anchor="e", bg="#dadde3")
labelWarnings.pack(anchor=tk.N, pady=0, padx=20)

# Buttons Grid
buttonsFrame = tk.Frame(window)
buttonsFrame.pack(side=tk.TOP, pady=10, anchor="ne", padx=20)

# Button 1
button1 = tk.Button(buttonsFrame, text="1", **Constant.number_button_options, command=lambda: command_on_click("1"))
button1.grid(row=2, column=0)

# Button 2
button2 = tk.Button(buttonsFrame, text="2", **Constant.number_button_options, command=lambda: command_on_click("2"))
button2.grid(row=2, column=1)

# Button 3
button3 = tk.Button(buttonsFrame, text="3", **Constant.number_button_options, command=lambda: command_on_click("3"))
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
button4 = tk.Button(buttonsFrame, text="4", **Constant.number_button_options, command=lambda: command_on_click("4"))
button4.grid(row=1, column=0)

# Button 5
button5 = tk.Button(buttonsFrame, text="5", **Constant.number_button_options, command=lambda: command_on_click("5"))
button5.grid(row=1, column=1)

# Button 6
button6 = tk.Button(buttonsFrame, text="6", **Constant.number_button_options, command=lambda: command_on_click("6"))
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
button7 = tk.Button(buttonsFrame, text="7", **Constant.number_button_options, command=lambda: command_on_click("7"))
button7.grid(row=0, column=0)

# Button 8
button8 = tk.Button(buttonsFrame, text="8", **Constant.number_button_options, command=lambda: command_on_click("8"))
button8.grid(row=0, column=1)

# Button 9
button9 = tk.Button(buttonsFrame, text="9", **Constant.number_button_options, command=lambda: command_on_click("9"))
button9.grid(row=0, column=2)

# Button -
buttonMinus = tk.Button(buttonsFrame, text=u"\u002D", command=lambda: command_on_click(
    u"\u002D"), width=Constant.button_width(), bg=Constant.operatorsColor(), font=("Arial", 20), height=Constant.button_height())
buttonMinus.grid(row=2, column=3)

# Button -/+
buttonChange = tk.Button(buttonsFrame, text="+/-", command=lambda: command_on_click(
    u"\u00B1"), width=Constant.button_width(), bg=Constant.operatorsColor(), font=("Arial", 20), height=Constant.button_height())
buttonChange.grid(row=3, column=0)

# Button 0
button0 = tk.Button(buttonsFrame, text="0", **Constant.number_button_options, command=lambda: command_on_click("0"))
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