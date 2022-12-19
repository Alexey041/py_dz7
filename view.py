def inp_metod():
    metod = input('Введите режим (inp/exp) ')
    return metod

def inp_data():
    user_data = input('Введите данные через запятую или звездочки\nфамилия,имя,номер,описание: ')\
    .split(',')
    if len(user_data) == 1:
        user_str = str(user_data).split('*')
        surname = ''
        description = ''
        surname1 = user_str[0]
        for i in range(2, len(surname1)):
            surname += surname1[i]
        name = user_str[1]
        number = user_str[2]
        description1 = user_str[3]
        for j in range(len(description1) - 2):
            description += description1[j]
    else:
        surname = user_data[0]
        name = user_data[1]
        number = user_data[2]
        description = user_data[3]

    return surname, name, number, description

def inp_search():
    find = input('Что хотите найти? ')
    return find

