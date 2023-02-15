from random import randint
#1
family = {
"Ilia": {'Name = Ilia ; age = 13; birhday = 28.08.2009 ;Phone = 111 '},
'Katya': { 'Name = Katya ; age = 45 ; birhday = 22.07.1977 ;Phone = 222 '},
'Taras' : {'Name = Taras ; age = 48 ; birhday = 28.10.1974 ;Phone = 333 '},
'Liza': {'Name = Liza ; age = 17; birhday = 07.09.2005 ;Phone = 444 '},
'Zoya' : {'Name = Zoya ; age = 73 ; birhday = 01.01.1950 ;Phone = 555 ' }}

#2
for element in family:
    print(element)
#2.1
print(family)

#3
print('Whats the key,Enter plz here: ')
k = input()
if k in family:
   print(family[k])
else:
   print('ERROR (PYER.wRKg) WRONG KEY GIVEN.')

#4

sps = []
for i in range(20):
    sps.append(randint(0, 100))

for i in enumerate(sps):
    print(i)
