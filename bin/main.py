'''
The program 

Neetre 2024
'''

import customtkinter
import csv
from icecream import ic

ic.disable()

class Currency:
    def __init__(self, name: str, value: float, inv: float):
        self.name = name
        self.value = value
        self.inv = inv

    def __str__(self) -> str:
        return f"Name: {self.name} - Value (over USD): {str(self.value)}  - Inv: {str(self.inv)}"


class Currency_manager:
    def __init__(self):
        self.values = []

    def see_curr(self, name_curr):
        curr = [value.name for value in self.values if value.name == name_curr][0]
        return curr

    def estraz(self, f_csv):
        with open(f_csv, "r") as file:
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
    def __init__(self, master, title, cur):
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
    def __init__(self, master, title, cur, value):
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


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.result = ''
        self.curr_manager = Currency_manager()
        f_csv = "../data/currencies.csv"
        self.curr_manager.estraz(f_csv)
        
        self.title("Convertor")
        self.geometry("640x480")
        self.grid_columnconfigure((0, 2), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.from_frame = FromFrame(self, "From", self.curr_manager.values)
        self.from_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.label = customtkinter.CTkLabel(self, text="=")
        self.label.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="nsew")

        self.to_frame = ToFrame(self, "To", self.curr_manager.values, self.result)
        self.to_frame.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=3)

        self.button = customtkinter.CTkButton(self, text="Convert", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=3)

    def button_callback(self):
        print(f"1: {self.from_frame.get_choice()[0]} ; {self.from_frame.get_choice()[1]}")
        print(f"2: {self.to_frame.get_choice()}")
        self.elabor()
        self.to_frame = ToFrame(self, "To", self.curr_manager.values, self.result)
        self.to_frame.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="nsew")
    
    def app_get(self):
        name_values = (self.from_frame.get_choice()[0], self.to_frame.get_choice())
        value_to_convert = self.from_frame.get_choice()[1]
        return name_values, value_to_convert

    def elabor(self):
        name_values, value_to_convert = self.app_get()
        value_to_convert = int(value_to_convert.replace("\n", ""))
        self.result = self.curr_manager.elab(name_values[0], name_values[1], value_to_convert)

'''
def main():
    f_csv = "../data/currencies.csv"
    from_="US Dollar"
    to_ = "Brazilian Real"
    value = float(5)
    print(f"Conversion from {from_} to {to_}, value {value}. Result:")
    curr_manager = Currency_manager()
    curr_manager.estraz(f_csv)
    result = curr_manager.conversion(from_, to_, value)
    print("Conversion: ", result)
'''

def main():
    app = App()
    app.mainloop()
    return

if __name__ == "__main__":
    main()
