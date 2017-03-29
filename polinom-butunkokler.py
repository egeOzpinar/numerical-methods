#!/usr/bin/python3
# -*- coding: utf-8 -*-
def f(x):
    return(1*x**5-7*x**4-3*x**3+79*x**2-46*x-120)

def f(dizi,x):
    toplam=0
    index=0
    for i in range(len(dizi)-1,-1,-1):
        toplam=toplam+(dizi[index])*pow(x,i)
        index=index+1
    return(toplam)

def fi(dizi,x):
    toplam=0
    index=0
    for i in range(len(dizi)-1,-1,-1):
        if(i==0):
            break
        toplam=toplam+(dizi[index])*pow(x,i-1)*i
        index=index+1
    return(toplam)

def fonk(dizi,xi):
    x1=xi
    for i in range(450):
        x2=x1-(f(dizi,x1)/fi(dizi,x1))
        x1=x2
    return(x1)


denklem=[]

a=int(input("kaçıncı dereceden denklem girmek istersiniz?:"))
for i in range(a+1):
    if(i==a):
        d=float(input("sabit terimin katsayısını gir:"))
        denklem.append(d)
        continue
    d=float(input("x üzeri %d'nin katsayısını gir:"%(a-i)))
    denklem.append(d)
    
xi = float(input("bir başlangıç değeri girin: "))

cozum=[]

while(len(denklem)!=2):
    kok=fonk(denklem,xi)
    xi=kok
    cozum.append(kok)
    for i in range(len(denklem)):
        if(i==0):
            continue
        denklem[i]=kok*(denklem[i-1])+denklem[i]
        
    denklem=denklem[:len(denklem)-1]
    
    if(len(denklem)==2):
        ek=-denklem[1]/denklem[0]
        cozum.append(ek)
        
print(x1,x2,x3,x4,x5)

for i in range(a):
    print("%d. kok="%(i+1),cozum[i])
