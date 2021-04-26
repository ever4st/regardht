from time import sleep
from colorama import Fore

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib


#я немного не понял, как это работает. раньше, эти методы были в methods.py, но это вызывало ошибку, скорее всего, из-за парадокса импортов. поэтому я вынес их в отдельный файл
def close(x):
    if x == None:
        '''тоже просто.
        прниаем аргумент, если он есть None, то закрываем программу по шаблону.
         если он есть - выводим, как сообщение и всё равно закрываем программу.'''
        print(Fore.GREEN + '[PROGRAM WILL CLOSED AT...]')

        for i in range(1, 6):
            print('{' + str(6 - i) + 's}')
            sleep(1)
            raise SystemExit
    else:
        print(Fore.RED + str(x) + '\n' + Fore.GREEN + '[PROGRAM WILL CLOSED AT...]')

        for i in range(1, 6):
            print('{' + str(6 - i) + 's}')
            sleep(1)

        print('{ BYE :) }')
        raise SystemExit

def mail(email, text):
    '''этот алгоритм я откопал на просторах интернета, правда там он был на 40+ строк, я его сократил.
    если надо - пользуйся, это я распишу подробно.'''
    msg = MIMEMultipart('alternative') #хз, так надо(очень подробно, не так ли?)
    msg['Subject'] = 'password' #тема письма
    msg['From'] = 'unknown_user <' + 'noreply2515@inbox.ru' + '>' #uknown_user - имя, от котрого будет отправлено сообщение. noreply2515@inbox.ru - почта, с которой это сообщение отправитья. для этого я создал отдельный ящик, можешь использовать его. с недавних пор, google и яндекс прекратилу поддержку такой рассылки, поэтому я использоал mail.ru, ты - как хочешь.
    msg['To'] = email #почта, на которую будет отправлено письмо.

    part_html = MIMEText(text, 'html') #текст письма, второй аргумент так и оставь. кстати, первый аргумент можно оформить как html-код, и он реально обработается и отправится.

    msg.attach(part_html) #понятия не имею, так и оставь

    mail = smtplib.SMTP_SSL('smtp.mail.ru') #тут тебе нужно указать сервер, через который будешь отпралять. я не совсем понял, как это работает, но ты должен про взять 'smtp.' и добавить адрес своей почты, который идёт после @. но не все ящики поддержывают реализацию smtp, и это надо смотреть в документации, крч гемора много. лично я писал наугад, можкшь попробовать также.
    mail.login('noreply2515@inbox.ru', '6auSpTeU$aI2') #твои почта и пароль
    mail.sendmail('noreply2515@inbox.ru', email, msg.as_string()) #первый аргумент - тоя почта(как ни странно), второй - почта получателя(как ни странно(снова)), третий - так и оставь
    mail.quit() #закрытие smtp сервера.