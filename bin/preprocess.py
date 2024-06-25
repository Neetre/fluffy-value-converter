'''
Neetre 2024
'''

def pre():
    """
    Creates the input file from a txt.
    """
    with open("../data/new.txt", "r", encoding="utf-8") as file:
        with open("../data/currencies.csv", "w", encoding="utf-8") as file_csv:
            lines = file.readlines()
            for line in lines:
                line = line.replace("\t", ",")
                file_csv.write(line)
