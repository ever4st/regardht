from functions import checkin
from aps import client

rel = checkin(['1', '2'])

if rel == '1':
    client()
elif rel == '2':
    print('ok.')
else:
    print('how?!')