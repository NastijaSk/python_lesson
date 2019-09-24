person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}
person4 = {'card': 12345, 'pin': 123, 'money': 150.99}

bank = [person1, person2, person3, person4]


def get_person_by_card(card_number):
    for person in bank:
        if person['card'] == card_number:
            return person


def is_pin_valid(person, pin_code):
    if person['pin'] == pin_code:
        return True
    return False


def check_account(person):
    return round(person['money'], 2)


def withdraw_money(person, money):
    if money > 0:
        if person['money'] - money >= 0:
            person['money'] -= money
            return '�� ����� {} ������.'.format(money)
        else:
            return '�� ����� ����� ������������ �������!'
    else:
        print('�������� �����')

def process_user_choice(choice, person):
    if choice == 1: # �������� ��� int, ���������� � str
        print(check_account(person))
    elif choice == 2:
        while 1==1:
            try:
                count = float(input('����� � ������:'))
                break
            except ValueError:
                print('������� ����� ����� ��� ���������� �����')
        print(withdraw_money(person, count))


def input_user_info():
    #���� ������� ���� ��������, � �� ���
    while 1==1:
        try:
            card_number, pin_code = input('1. ������� ����� ����� � ��� ��� ����� ������:').split()
            #break
            return card_number, pin_code
        except ValueError:
            print('�������� ������, ��������� ����')

def user_info_valid(card_number, pin_code):
    #���� ������ ����� ������ int
    i = 0
    while i < 3: # ����� ������������ 3 �������
        try:
            if i >= 1:
                card_number, pin_code = input('2. ������� ����� ����� � ��� ��� ����� ������:').split()
            card_number = int(card_number)
            pin_code = int(pin_code)
            break
        except ValueError:
            print('������� �����')
            i+=1
    return card_number, pin_code


def start():
    card_number, pin_code = input_user_info()
    print(card_number, pin_code)
    card_number, pin_code = user_info_valid(card_number, pin_code)

    person = get_person_by_card(card_number)
    if person and is_pin_valid(person, pin_code):
        choice = 0
        while True:
            try:
                choice = int(input('�������� �����:\n'
                               '1. ��������� ������\n'
                               '2. ����� ������\n'
                               '3. �����\n'
                               '---------------------\n'
                               '��� �����:'))
            except ValueError:
                choice = 0
                print('������� 1,2 ��� 3')
            if choice == 3:
                break
            process_user_choice(choice, person)
    else:
        print('����� ����� ��� ��� ��� ������� �������!')

start()
