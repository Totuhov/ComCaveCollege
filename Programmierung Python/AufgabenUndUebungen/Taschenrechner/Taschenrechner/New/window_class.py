import tkinter as tk
import os
from tkinter import Menu
from constant_class import Constant


# 1.1 Get the path to the directory containing the script
dir_path = os.path.dirname(os.path.realpath(__file__))

# 1.2 Set the path to the file in the same directory
file_path = os.path.join(dir_path, "icon.ico")


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Taschenrechner v1.0")
        screen_width = self.winfo_screenwidth()
        screen_heigth = self.winfo_screenheight()
        center_x = int(screen_width / 2 - 330 / 2)
        center_y = int(screen_heigth / 2 - 450 / 2)
        self.geometry(f"330x450+{center_x}+{center_y}")
        self.resizable(False, False)
        self.iconbitmap(file_path)  # 1.3 insert the path to the file as string
        self.configure(background="white")
        

        self.labelsFrame = tk.Frame(self, bg="white")
        self.labelsFrame.pack(side=tk.TOP, pady=15)

        # Text Label 1
        self.label1 = tk.Label(self.labelsFrame, text="0",
                          width=30, font=("Arial", 20), anchor="e", bg="#dadde3")
        self.label1.pack(anchor=tk.N, pady=0, padx=20)
        # Text Label 2 operator
        label2 = tk.Label(self.labelsFrame, text="",
                          width=30, font=("Arial", 20), anchor="e", bg="#dadde3")
        label2.pack(anchor=tk.N, pady=0, padx=20)
        # Text Label 3
        label3 = tk.Label(self.labelsFrame, text="",
                          width=30, font=("Arial", 20), anchor="e", bg="#dadde3")
        label3.pack(anchor=tk.N, pady=0, padx=20)
        # Text Label Warnings
        labelWarnings = tk.Label(self.labelsFrame, text="",
                                 width=30, font=("Arial", 20), anchor="e", bg="#dadde3")
        labelWarnings.pack(anchor=tk.N, pady=0, padx=20)

        # Buttons Grid
        self.buttonsFrame = tk.Frame(self)
        self.buttonsFrame.pack(side=tk.TOP, pady=10, anchor="ne", padx=20)

        # Button 1
        button1 = tk.Button(self.buttonsFrame, text="1", **
                            Constant.number_button_options)
        button1.grid(row=2, column=0)

        # Button 2
        button2 = tk.Button(self.buttonsFrame, text="2", **
                            Constant.number_button_options)
        button2.grid(row=2, column=1)

        # Button 3
        button3 = tk.Button(self.buttonsFrame, text="3", **
                            Constant.number_button_options)
        button3.grid(row=2, column=2)

        # Button /
        buttonDivide = tk.Button(self.buttonsFrame, text=u"\u00F7",
                                 width=Constant.button_width(), bg=Constant.operatorsColor(), font=("Arial", 20), height=Constant.button_height())
        buttonDivide.grid(row=0, column=3)

        # Button C
        buttonC = tk.Button(self.buttonsFrame, text="C",
                            width=Constant.button_width(), bg=Constant.button_C_colotr(), font=("Arial", 20), height=Constant.button_height())
        buttonC.grid(row=0, column=4)

        # Button 4
        button4 = tk.Button(self.buttonsFrame, text="4", **
                            Constant.number_button_options)
        button4.grid(row=1, column=0)

        # Button 5
        button5 = tk.Button(self.buttonsFrame, text="5", **
                            Constant.number_button_options)
        button5.grid(row=1, column=1)

        # Button 6
        button6 = tk.Button(self.buttonsFrame, text="6", **
                            Constant.number_button_options)
        button6.grid(row=1, column=2)

        # Button X
        buttonMulti = tk.Button(self.buttonsFrame, text=u"\u00D7", width=Constant.button_width(
        ), bg=Constant.operatorsColor(), font=("Arial", 20), height=Constant.button_height())
        buttonMulti.grid(row=1, column=3)

        # Button =
        buttonResult = tk.Button(self.buttonsFrame, text=u"\u003D", width=Constant.button_width(
        ), bg=Constant.operatorsColor(), font=("Arial", 20), height=2)
        buttonResult.grid(row=1, column=4, rowspan=3, ipady=40)

        # Button 7
        button7 = tk.Button(self.buttonsFrame, text="7", **
                            Constant.number_button_options)
        button7.grid(row=0, column=0)

        # Button 8
        button8 = tk.Button(self.buttonsFrame, text="8", **
                            Constant.number_button_options)
        button8.grid(row=0, column=1)

        # Button 9
        button9 = tk.Button(self.buttonsFrame, text="9", **
                            Constant.number_button_options)
        button9.grid(row=0, column=2)

        # Button -
        buttonMinus = tk.Button(self.buttonsFrame, text=u"\u002D", width=Constant.button_width(
        ), bg=Constant.operatorsColor(), font=("Arial", 20), height=Constant.button_height())
        buttonMinus.grid(row=2, column=3)

        # Button 0
        button0 = tk.Button(self.buttonsFrame, text="0", **
                            Constant.number_button_options)
        button0.grid(row=3, column=1)

        # Button +
        buttonplus = tk.Button(self.buttonsFrame, text=u"\u002B", width=Constant.button_width(
        ), bg=Constant.plusColor(), font=("Arial", 20), height=Constant.button_height())
        buttonplus.grid(row=3, column=3)

    def add_buttons_for_calculator(self):
        self.buttonChange = tk.Button(self.buttonsFrame, text="+/-", width=Constant.button_width(
        ), bg=Constant.operatorsColor(), font=("Arial", 20), height=Constant.button_height())

        self.buttonPoint = tk.Button(self.buttonsFrame, text=".", width=Constant.button_width(
        ), bg=Constant.operatorsColor(), font=("Arial", 20), height=Constant.button_height())

        self.buttonChange.grid(row=3, column=0)

        self.buttonPoint.grid(row=3, column=2)

    def add_buttons_for_convertor(self):
        self.buttonChange = tk.Button(self.buttonsFrame, text="dec", width=Constant.button_width(
        ), bg=Constant.operatorsColor(), font=("Arial", 20), height=Constant.button_height())

        self.buttonPoint = tk.Button(self.buttonsFrame, text="bin", width=Constant.button_width(
        ), bg=Constant.operatorsColor(), font=("Arial", 20), height=Constant.button_height())

        self.buttonChange.grid(row=3, column=0)

        self.buttonPoint.grid(row=3, column=2)

    def command_on_click(self, text):
        label1_text = self.label1.cget("text")  # get current text of all lables
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
