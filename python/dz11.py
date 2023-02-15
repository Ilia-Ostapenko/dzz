from random import *
#1
#sps = [1,66,34,99,12,56,70,38,64]
#def f(sps = [1,66,34,99,12,56,70,38,64]):
    #return 
#sps = [1,66,34,99,12,56,70,38,64]
#a = max(sps)
#print(a)
sps = []
for i in range(10):
    sps.append(randint(0, 99))
print(sps)

def large():
    maximum = max(sps)
    return maximum

print(large())