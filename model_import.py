import view
import csv

def import_in_csv():
    with open('data.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(view.inp_data())

