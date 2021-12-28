
"""
Created on Wed Nov 10 13:21:17 2021

@author: Pavel
"""
import random
def F(t):
  w = s 
  for i in range(len(a)):
      w += a[len(a)-i-1]*pow(t,len(a)-i)
  return w

b=[] 
x=[]
y=[] 
s = int(input("Introdu cheia secreta s  = "))
n = int(input('Introdu n (in cite parti va fi divizat secretul): '))
k = int(input('Introdu k (cite bucati sunt necesare pentru restabilirea cheii): '))
a = random.sample(range(1, 100), k)
#a=[12,3,15,7,20,26]
print("Numerele aleatoare generate : ",a)
for i in range (1,n+1):
    b.append(F(i))
print('Perechile de numere in care a fost impartita cheia:')
for i in range (0,n):
    print(i+1," ",b[i])
print('R E S T A B I L I R E A  C H E I I:')
print('Introduceti perechile de numere care participa la restabilirea cheii:')
for i in range(k+1):
    x.append(int(input("Numarul de ordine a perechii :")))
    y.append(b[x[i]-1])
    print(x[i]," ",y[i])
final=0
for g in range(k+1):
    p2=p1=1
    for r in range(k+1):
        if (g != r):
              p2 *= (x[g]-x[r])
              p1 *= x[r]
    final += ((p1*y[g])/p2)
print('C H E I A  R E S T A B I L I T A  E S T E: ',round(final))
