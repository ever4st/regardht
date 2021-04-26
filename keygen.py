from pyperclip import copy
from random import choice

'''это как раз тот самый скрипт, которая даёт тебе ключ доступа к самой программе.
он одноразовый, и, когда я доведу это до ума, получить его будет довольно-таки сложно.
кстати, тут реализован алоритм копирования. в плане, программа копирует ключ в буфер обмена, и при запуске главного приложения, ты можешь его просто вставить.
тоже возьми на заметку:
import pyperclip as pp
pp.copy(#строка, которая скопируется)'''
key = ''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTQVWXYZ1234567890-=!@#$%^&*():""\'\'|/?.>,<'

for k in range(128):
    key += choice(chars)

passw = open('keys.txt', 'w')

copy(key)
passw.write(key)
passw.close()