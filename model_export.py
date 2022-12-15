import csv
import re
import view

def export_data_now():
    with open('data.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        find = str(view.inp_search())
        for row in reader:
            some_str = str(row)
            if re.search(find, some_str):
                print(row)

