from time import sleep
from random import randint
from colorama import Fore
from functions import passgen, checkbd, checkn, checka, read, checkin
from global_procedures import mail

import datetime


'''если в functions.py находятся функции, которые хоть что-то возвращают, то тут находятся процедуры, которые просто что-то делают.
вообще, правильно было бы назвать этот файл procedures.py, но это же я :)'''

def record(name):
    '''это должно было быть блоком кода процедуры регистрации, которая тут последняя.
    но это вызвало ошибку. так что я вынес этот алгоритм отдельно.
    он добавляет ник пользоватля в список ников, которые уже есть, чтобы его не смогли указать повторно.'''
    file = open('users/all.txt')
    users = file.read()
    file.close()
    users += name + '\n'
    file = open('users/all.txt', 'w')
    file.write(users)
    file.close()

def run():
    '''самое простое в этом проекте.
    скрипт запуска программы.
    его задача - делать вид, что программа реально что-то делает, что, конечно же, не так.'''
    print(Fore.GREEN + '[STARTING PROGRAM]')
    sleep(1)
    print('[...]')
    sleep(randint(1, 5))
    print('[REALTIME ENCRIPTOIN STARTED]')
    sleep(1)
    print('[...]')
    sleep(randint(1, 5))
    print('[THE FORMS GOT READY]')
    sleep(1)
    print('[DOUBLE METHOD: GET/POST]')
    sleep(1)
    print('[...]')
    sleep(randint(1, 5))
    print('[PROXY IS RUNNING]')
    sleep(1)
    print('[...]')
    sleep(randint(1, 5))
    print('[SSL GOT OFF]')
    sleep(1)
    print('[...]')
    sleep(randint(1, 5))
    print('[PROGRAM IS RUNNING]')
    print("""
              ===================PROGRAM: REGARD HACK TOOL=======================
            || CREATED BY TILER BERNEM                                           ||
              --------------------------ATTENTION:-------------------------------
            || AUTOR ISN'T RESPONSIBLE FOR ANY USER ACTIONS                      ||
            || ALL MATERIAL IS PROVIDED FOR INFORMATIONAL PURPOSES ONLY          ||
              ===================================================================""")

def register():
    '''процедура регистрации.
    тоже банально, но я всё закомментировал. special for 'u, stupid baby :)'''
    data = '' #строка, которая в последствии и запишется в отдельный файл
    inp = [] #не помню уже. что-то для сбора данных о пользователе. только вот зачем?

    print(Fore.GREEN + "j1mm1: Hello, I'm your helper, Jimmi.\nSo, how can i call you?(enter nick)" + Fore.BLUE)
    inp.append(checka()) #водим ник и сразу же проверяем
    data += inp[0] + '\n' #после проверки добавляем ник в запись

    print(Fore.GREEN + 'j1mm1: Alright, now enter your first name & last name.' + Fore.BLUE)
    data += checkn() + '\n' #имя. тоже самое. вводим. проверяем. записываем.

    print(Fore.GREEN + 'j1mm1: OK. One more time :). Entel your birthday(yyyy/mm/dd).' + Fore.BLUE)
    data += checkbd() + '\n' #дата рождения. аналогично.

    print(Fore.GREEN + 'j1mm1: So, all be fine. And the last. Enter your e-mail so wa can send you a password.' + Fore.BLUE)
    inp.append(input('you: ')) #почта пользователя. её можно было бы тоже проверить, но в этом нет смысла, ибо, если он указал неккоректную почту, то он не узнает свой пароль и не восстановит его.
    data += inp[1] + '\n\n' #записываем почту
    data += str(datetime.datetime.now().strftime("%Y/%m/%d")) + '\n' #также записываем дату и время на локальных часах юзера на момент регистрации
    data += str(datetime.datetime.now().strftime("%H:%M:%S")) + '\n\n'
    inp.append(passgen(16)) #генерируем пароль и тоже записываем.
    data += inp[2]

    record(inp[0]) #см methods.py - record()
    #это можно было сделать проще, но мы не ищем лёгких путей. крч, этот блок просто инкрементирует лог.
    # лог - отднльный файл, пока что так, потом посмотрим.
    # чтобы знать, сколько пользователей зарегестрировалось и какой id у следующего, без него никак.
    temp = open('log.txt', 'r')
    ttid = int(temp.read())
    temp.close()
    temp = open('log.txt', 'w')
    temp.write(str(ttid + 1))
    temp.close()
    root = 'users/' + str(ttid + 1) + '.txt'
    rn = open(root, 'w')
    rn.write(data)
    rn.close()

    mail(inp[1], inp[2])

    del data

    print(Fore.GREEN + 'j1mm1: oh, yeah +1(you are', ttid + 1,')! An email with your password has already been sent to your mail, check your inbox :).\nJimmi hope you enjoy it here! For the changes to take effect, the PC will close the program at')

    for i in range(1, 6): #после регистрации выходим из программы
        print('{' + str(6 - i) + 's}' )
        sleep(1)
    raise SystemExit(0)
