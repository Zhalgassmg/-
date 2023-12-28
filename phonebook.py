def show_menu():
    print('1. Распечатать справочник' 
    '2. Найти телефон по фамилии'
    '3. Изменить номер телефона'
    '4. Удалить запись'
    '5. Найти абонента по номеру телефона'
    '6. Добавить абонента в справочник'
    '7. Копировать в другой файл'
    '8. Закончить работу', sep = '\n')
    choice=int(input('введите номер меню'))
    return choice

def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt ('phonebook.csv')
    while (choice!=8):
        if choice==1:
            print (phone_book)

        elif choice==2:
            last_name=input ('lastname ')
            print (find_by_lastname(phone_book, last_name))

        elif choice==3:
            last_name=input ('lastname ')
            new_number=input ('new number ')
            print (change_number(phone_book,last_name,new_number))

        elif choice==4:
            last_name=input ('lastname ')
            print(delete_by_lastname(phone_book,last_name))

        elif choice==5:
            number=input ('number ')
            print (find_by_number (phone_book,number))

        elif choice==6:
            user_data=input ('new data ') 
            add_user(phone_book,user_data)
            write_txt ('phonebook.csv', phone_book)
        
        elif choice==7:
            str_num = int(input('line number '))
            new_file=input ('new file ') 
            copy_to_file (new_file, str_num, phone_book)

        choice=show_menu()

def read_txt(filename):
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание' ]

    with open(filename, 'r' ,encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)

    return phone_book


def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')

def find_by_lastname(phone_book, last_name):
    for i in range(len(phone_book)): 
        for k,v in phone_book[i].items():
            if v == last_name:
                return phone_book[i]['Телефон']

def change_number(phone_book,last_name,new_number):
    for i in range(len(phone_book)): 
        for k,v in phone_book[i].items():
            if v == last_name:
                phone_book[i]['Телефон'] = new_number
    return phone_book

def delete_by_lastname(phone_book,last_name):
    list1 = []
    for i in range(len(phone_book)): 
        for k,v in phone_book[i].items():
            if v == last_name:
                list1.append(phone_book[i])
    phone_book = list(filter(lambda x: x not in list1, phone_book))            
    
    return phone_book

def find_by_number (phone_book,number):
    for i in range(len(phone_book)): 
        for k,v in phone_book[i].items():
            if v == number:
                return phone_book[i]['Фамилия'],  phone_book[i]['Имя']

def add_user(phone_book,user_data):
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание' ]
    new_record = dict(zip(fields, user_data.split(',')))
    phone_book.append(new_record)

def copy_to_file (new_file, str_num, phone_book):
    with open(new_file, 'w', encoding='utf-8') as phb2:
        phb2.write(','.join(phone_book[str_num-1].values()))


work_with_phonebook()