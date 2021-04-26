from colorama import Fore
from random import choice
from time import sleep
from global_procedures import mail, close

import datetime

#тут описанны функции, т.е. те алгоритмы, которые что-то возвращают.

def read(path, num):
    '''эта функция просто считывает строки с файла.
    довольно-таки просто, но я - не я, если бы упустил возможность выпендриться.
    так вот, функция readlines - глобальная и возвращает строку, как весь текст, а в качестве перехода использует '\n'.
    я придумал с помощью метода split разбить файл через этот самы '\n' и каждая строка - элемент списка.
    таким образом, если мы знаем, какая строка из какого файла нам нужна, то без проблем вызываем функцию, передаемнужные аргументы, и получаем эту строку.
    '''
    file = open(path, 'r')
    if num == None:
        try:
            arr = ''.join(open('users/1.txt').readlines()).split('\n')
            for k in range(arr.count('')):
                arr.remove('')
                
            return arr
        except:
            return []
    else:
        return file.readlines()[num - 1].split('\n')[0]

def confirm():
    '''это функия отдельно для подтверждения пароля.
    почти все они похожи и я понятия не имею, зачем сделал их отдельно, но пока оставлю так'''
    print( Fore.GREEN, '[' + datetime.datetime.now().strftime('%d.%m.%Y %H:%M%S') + ']', 'sy$tem: confirm clearance level\n', Fore.BLUE )
    bar = False
    while bar == False:
        foo = input('you: ')
        key = open('keys.txt', 'r')
        if foo == key.read():
            bar = True
        else:
            print(Fore.RED + 'ERROR | UNCORRECT KEY' + Fore.BLUE)
            bar = False
        
    return True

def passgen(x):
    #это простейший генератор паролей. х - длина пароля. да, в этой программе, ты не придумаваешь пароль, тебе его генерирует эта функция.
    string = ''
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTQVWXYZ1234567890-=!@#$%^&*():""\'\'|/?.\>,<'

    for k in range(x):
        string += choice(chars)

    return string

def checkbd():
    '''оооо, над этим дерьмом я постарался.
    хотя, тут всё просто - функция проверяет введённую пользователем дату рождения при регистрации на достоверность, и, естественно не пропускает, если ему меньше 18.
    но, при этом, это был первый алгоритм проверки такого типа, так что я долго думал над ним'''
    bar = False
    while bar == False:
        foo = input('you: ').split('/')

        try:
            for k in foo:
                n = int(k)
        except:
            print(Fore.RED + 'ERROR | UNCORRECT DATA' + Fore.BLUE)
            bar =  False

        if len(foo) == 3 and len(foo[0]) == 4 and int(foo[0]) <= int(datetime.datetime.today().strftime('%Y')) and int(foo[1]) <= 12 and int(foo[2]) <= 31:
            if int(foo[1]) == 2 and int(foo[2]) <= 28 or int(foo[1]) % 2 == 1 and int(foo[2]) <= 31 or int(foo[1]) != 2 and int(foo[1]) % 2 == 0 and int(foo[2]) <= 30:
                if int(datetime.datetime.today().strftime('%Y')) - int(foo[0]) >= 18:
                    bar = True
                else:
                    close('ACCESS DENIED | USER NO 18')
            else:
                print(Fore.RED + 'ERROR | UNCORRECT DATA' + Fore.BLUE)
                bar =  False
        else:
            print(Fore.RED + 'ERROR | UNCORRECT DATA' + Fore.BLUE)
            bar =  False
    
    return '/'.join(foo)

def checkn():
    '''здесь всё тоже самое, как и с checkbd.
    только тут мы проверяем имя на корректность.'''
    bar = False
    while bar == False:
        foo = input('you: ').split()
        if len(foo) == 2 and foo[0].isalpha() and foo[1].isalpha():
            foo[0].capitalize()
            foo[1].capitalize()

            bar = True

        else:
            bar = False
            print(Fore.RED + 'ERROR | THE INPUT CONTAINS FORBIDDEN CHARACTERS' + Fore.BLUE)
    return ' '.join(foo)     

def checka():
    '''тут всё тоже довольно просто. в отдельном файле содержатся ники  всех пользователей.
    если пользователь введёт уже указанный ник, то программа ему об этом сообщит, и заставит ввести другой.'''
    bar = False
    while bar == False:
        foo = input('you: ')
        nicks = read('users/all.txt', None)
        if foo in nicks:
            print(Fore.RED + 'ERROR | THIS NICK IS ALREADY IN USE' + Fore.BLUE)
            bar = False
        else:
            bar = True
    
    return foo

def checkin(arr):
    '''тоже простенько.
    цикл выполняется, пока на вход не поступит один из варианиов ответа, переданного в списке, как аргумент.
    а, когда ответ будет положительный, функция его вернёт.'''
    bar = False
    while bar == False:
        foo = input('you: ')
        if foo not in arr:
            print(Fore.RED + 'ERROR | UNEXPECTED INPUT' + Fore.BLUE)
        else:
            bar = True
        
    return foo

def checkfor(x, y):
    bar = False
    while bar == False:
        foo = input('you: ')
        if foo == x: #если пароль верный, то мы просто выходим из цикла и возвращем True и ник.
            bar = True
        else:
            print(Fore.RED + 'ERROR | INVALID PASSWORD\n' + Fore.GREEN + '[' + datetime.datetime.now().strftime('%d.%m.%Y %H:%M%S') + ']', 'sy$tem: forgot password?(y/n)' + Fore.BLUE)
            rel = checkin(['y', 'n'])
            if rel == 'y': #если пароль неверный, то отправляем его пользователю на почту, указанную при регистрации и закрываем программу.
                print(Fore.GREEN +  '[' + datetime.datetime.now().strftime('%d.%m.%Y %H:%M%S') + ']', 'sy$tem: the password has been sent to your mail.')
                mail(read(y, 4), read(y, 9))

                close(None)

            else:
                pass

    return [bar, read(y, 1)]


