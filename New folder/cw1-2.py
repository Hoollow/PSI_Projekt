#padding
print('{:>10}'.format('test'))
#Signed numbers
print('{:+d}'.format(42))
#Named placeholders
data = {'first': 'Hodor', 'last': 'Hodor!'}
print('{first} {last}'.format(**data))
#Getitem and Getattr
person = {'first': 'Jean-Luc', 'last': 'Picard'}
print('{p[first]} {p[last]}'.format(p=person))
#Datetime
from datetime import datetime
print('{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5)))