import model_export
import model_import
import view

def button_click():
    inp = view.inp_metod()
    if inp == 'inp':
        model_import.import_in_csv()
    elif inp == 'exp':
        model_export.export_data_now()
    else:
        print('Введен некорректный режим!')
