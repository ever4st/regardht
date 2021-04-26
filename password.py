from functions import read
from pyperclip import copy

'''ещё один инструмент разработчика.
ты просто вводишь нужный id, а он копирует тебе пароль.
снова, для тесто самое то.'''
copy(read('users/' + input() + '.txt', 9))