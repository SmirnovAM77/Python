#  Фамилия, имя, отчество, номер телефона

def ask_user():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = int(input('Введите номер телефона: '))
    return last_name, first_name, phone_number


def save_to_file(data: tuple, file, mode='a'):
    data_str = ' '.join(map(str, data))
    #data_str = ' '.join(map(str, data))
    # print(data_str)
    # 'cp-1251'
    with open(file, mode, encoding='utf-8') as fd:
        fd.write(f'{data_str}\n')
        
def rewrite_to_file(data, file, mode='w'):
    data_str = ' '.join(map(str, data))
    with open(file, mode, encoding='utf-8') as fd:
        fd.write(f'{data_str}\n')
     
     
def read_file(file):
    with open(file, 'r', encoding='utf-8') as fd:
        lines = fd.readlines()
    headers = ['фамилия', 'имя', 'номер телефона']
    list_contacts = []
    for line in lines:
        line = line.strip().split()
        list_contacts.append(dict(zip(headers, line)))
    return list_contacts

def search_contact(list_contacts: list, param: str, what: str):
    param_dict = {'1': 'фамилия', '2': 'имя', '3': 'номер телефона'}
    found_contacts = []
    for contact in list_contacts:
        if contact[param_dict[param]] == what:
            found_contacts.append(contact)
    return found_contacts


def ask_search():
    print('По какому полю выполнить поиск?')
    search_param = input('1 - по фамилии, 2 - по имени, 3 - по номеру телефона: ')
    what = None
    if search_param == '1':
        what = input('Введите фамилию для поиска: ')
    elif search_param == '2':
        what = input('Введите имя для поиска: ')
    elif search_param == '3':
        what = input('Введите номер для поиска: ')
    return search_param, what
    


def main_menu():
    file_contacts = 'file3.txt'
    while True:
        user_choice = input('1 - добавить новый контакт,\n '
                            '2 - найти контакт,\n 3 - посмотреть весь справочник,\n 4 - удалить контакт,\n 0 - выйти\n')
        if user_choice == '1':
            # print('добавить новый контакт')
            save_to_file(ask_user(), file_contacts)
        elif user_choice == '2':
            # print('найти контакт')
            lst_contacts = read_file(file_contacts)
            search_param, what = ask_search()
            res = search_contact(lst_contacts, search_param, what)
            print(res)
        elif user_choice == '3':
            # print('посмотреть весь справочник')
            print(read_file(file_contacts))
        elif user_choice == '4':
            # print('посмотреть весь справочник').
            lst_contacts = read_file(file_contacts)
            search_param, what = ask_search()
            res = search_contact(lst_contacts, search_param, what)
            res1 = filter(lambda i: i not in res, lst_contacts)
            rewrite_to_file(res1, file_contacts)
            #rewrite_to_file(ask_user(), res1)
            #print(res)
            
            
            print('думаем как удалить')
        elif user_choice == '0':
            print('До свидания')
            break

if __name__ == '__main__':

    main_menu()