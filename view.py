def inp_metod():
    metod = input('Введите режим (inp/exp) ')
    return metod

def inp_data():
    user_data = input('Введите данные через запятую\nфамилия,имя,номер,описание: ')\
    .split(',')
    surname = user_data[0]
    name = user_data[1]
    number = user_data[2]
    description = user_data[3]

    return surname, name, number, description

def inp_search():
    find = input('Что хотите найти? ')
    return find

