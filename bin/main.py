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
    

def main():
    f_csv = "../data/currencies.csv"

    curr_manager = Currency_manager()
    curr_manager.estraz(f_csv)
    result = curr_manager.conversion("US Dollar", "Brazilian Real", float(5))
    print("Conversion: ", result)


if __name__ == "__main__":
    main()
