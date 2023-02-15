import random
from random import randint
#1
nums = []
for i in range(20):
    nums.append(randint(0, 20))

numss = []
for i in range(20):
    numss.append(randint(0, 20)) 
print(nums)
print(numss)
#1.1
print('#######################1.1######################')
dup = {x for x in nums if nums.count(x) > 1}
print(dup)  
du = {x for x in numss if numss.count(x) > 1}
print(du) 
#1.2
print('############################1.2####################################')
c = [x for x in nums if x in numss]
print(c)
#2
print('####################2####################')
a = []
for i in range(12):
    a.append(randint(50, 100))
print(a)
#2.1
print('####################################2.1######################')
e = 0
while e < len(a):
    print(a[e])
    e+=1

#2.2
print('####################################2.2##############################')
for number in a:
    print(number)

#3
print('############################3#################################')
import random
list_e = [random.randint(10, 100) for value in range(0, 10)] 
print(list_e)

#4
print('############################4#######################')
l3 = list_e
for x,y in enumerate(l3):
    print(x,y)



#5
print('#############################5########################')
#empty_set = set()
empty_set = {random.randint(10, 100) for value in range(0, 10)} 

print(empty_set)

#6 
print('#############################6########################')
import random
pas = ''
for x in range(12) or (8): 
    pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')) 
print(pas)

pass0 = pas
while len(pass0) <= 8:
    print("KOrotenko")
    pass0 = input()
while "123" in pass0:
    print("Prosto")
    pass0 = pas
else:
    print("OK")