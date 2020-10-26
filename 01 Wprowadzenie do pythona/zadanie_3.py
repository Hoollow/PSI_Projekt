from datetime import datetime
#Basic formatting
print('{} {}'.format('jeden', 'dwa'))
#Padding and aligning strings
print('{:^10}'.format('teścik')) #mamy 10 miejsc od początku do końca, bo jest :^10 no i format to nasz tekst
#Truncating long strings
print('{:.5}'.format('Malarz')) #ucinamy tekst .5 oznacza, że ma pokazać tylko pierwsze 5, reszty nie ma
#Signed numbers
print('{: d}'.format((- 23))) #wypisuje ujemną liczbe, a bardziej po prostu pokazuje xd
print('{: d}'.format((55)))
#Datetime
print('{:%Y-%m-%d %H:%M}'.format(datetime(2020, 10, 26, 12, 23))) # trzeba na początku dodać from datetime import datetime