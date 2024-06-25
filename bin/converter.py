'''
This is a Python program for a currency converter with a graphical user interface (GUI).
It uses the customTkinter library to create the GUI.

Neetre 2024
'''

import argparse
import csv
from icecream import ic

import customtkinter
from preprocess import pre

class Currency:
    """
    This class creates a currency object.
    """

    def __init__(self, name: str, value: float, inv: float):
        self.name = name
        self.value = value
        self.inv = inv

    def __str__(self) -> str:
        return f"Name: {self.name} - Value (over USD): {str(self.value)}  - Inv: {str(self.inv)}"


class CurrencyManager:
    """
    This class manages the currencies.
    """
    def __init__(self):
        self.values = []

    def see_curr(self, name_curr):
        curr = [value.name for value in self.values if value.name == name_curr][0]
        return curr

    def retrive_curr(self):
        return [value.name for value in self.values]

    def estraz(self, f_csv):
        with open(f_csv, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                value = row['value']
                inv = row['inv']
                currency = Currency(name, float(value), float(inv))
                self.values.append(currency)

    def conversion(self, from_: str, to_: str, num: float) -> str:
        from_ = [obj for obj in self.values if obj.name == from_][0]
        to_ = [obj for obj in self.values if obj.name == to_][0]
        num = num / from_.value
        num = num * to_.value
        valore = f"{num:.2f}"
        return valore


class FromFrame(customtkinter.CTkFrame):
    """
    This class creates the frame for the "From" section of the application.

    Args:
        customtkinter (class): The customtkinter class.
    """
    def __init__(self, master, title: str, cur: list):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.choice = ""
        self.text = ""

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.combobox = customtkinter.CTkComboBox(self, values=cur, command=self.combobox_callback)
        self.combobox.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        self.textbox = customtkinter.CTkTextbox(master=self, height=1, width=1, border_width=3, corner_radius=6)
        self.textbox.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.textbox.insert("0.0", "")

    def combobox_callback(self, choice):
        print("Combobox dropdown clicked: ", choice)

    def get_choice(self):
        choice = self.combobox.get()
        text = self.textbox.get("0.0", "end")
        return choice, text


class ToFrame(customtkinter.CTkFrame):
    """
    This class creates the frame for the "To" section of the application.

    Args:
        customtkinter (class): The customtkinter class.
    """
    def __init__(self, master, title: str, cur: list, value: float):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.choice = ""
        self.text = ""

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.combobox = customtkinter.CTkComboBox(self, values=cur, command=self.combobox_callback)
        self.combobox.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        self.textbox = customtkinter.CTkTextbox(master=self, height=1, width=1, border_width=3, corner_radius=6)
        self.textbox.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.textbox.insert("0.0", f"{value}")

    def combobox_callback(self, choice):
        print("combobox dropdown clicked: ", choice)

    def get_choice(self):
        choice = self.combobox.get()
        return choice

    def update_result(self, new_result):
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", new_result)


class App(customtkinter.CTk):
    """
    This class creates the main window of the application.

    Args:
        customtkinter (class): The customtkinter class.
    """
    def __init__(self):
        super().__init__()
        self.result = ''

        self.curr_manager = CurrencyManager()
        f_csv = "../data/currencies.csv"
        self.curr_manager.estraz(f_csv)
        self.cur = self.curr_manager.retrive_curr()

        self.title("Convertor")
        self.geometry("400x220")
        self.grid_columnconfigure((0, 2), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.from_frame = FromFrame(self, "From", self.cur)
        self.from_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.label = customtkinter.CTkLabel(self, text="=")
        self.label.grid(row=0, column=1, padx=10, pady=10, sticky="ew", columnspan=1)

        self.to_frame = ToFrame(self, "To", self.cur, self.result)
        self.to_frame.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="nsew")

        self.button = customtkinter.CTkButton(self, text="Convert", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=3)

    def button_callback(self):
        print(f"1: {self.from_frame.get_choice()[0]} ; {self.from_frame.get_choice()[1]}")
        print(f"2: {self.to_frame.get_choice()}")
        self.elabor()
        self.to_frame.update_result(self.result)

    def app_get(self):
        name_values = (self.from_frame.get_choice()[0], self.to_frame.get_choice())
        value_to_convert = self.from_frame.get_choice()[1]
        return name_values, value_to_convert

    def elabor(self):
        name_values, value_to_convert = self.app_get()
        value_to_convert = int(value_to_convert.replace("\n", ""))
        self.result = self.curr_manager.conversion(name_values[0], name_values[1], value_to_convert)


def arg_parser():
    parser = argparse.ArgumentParser(description="Currency converter")
    parser.add_argument("--pre", action="store_true", help="Run the preprocessing.")
    parser.add_argument("--cli", action="store_true", help="Run the program in CLI mode.")
    parser.add_argument("--gui", action="store_true", help="Run the program in GUI mode.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity.")
    args = parser.parse_args()

    return args


def cli():
    f_csv = "../data/currencies.csv"
    curr_manager = CurrencyManager()
    curr_manager.estraz(f_csv)

    print("Available currencies: ", curr_manager.retrive_curr())

    while True:
        from_= input("From: ").strip()
        to_ = input("To: ").strip()
        value = float(input("Value: ").strip())
        print(f"Conversion from {from_} to {to_}, value {value}.")

        result = curr_manager.conversion(from_, to_, value)
        print("Conversion: ", result)

        q = input("Do you want to continue? (y/n): ")
        if q == "n":
            break


def gui():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    args = arg_parser()

    if args.verbose:
        ic.enable()
    else:
        ic.disable()

    if args.pre:
        pre()

    if args.cli:
        cli()
    else:
        gui()
