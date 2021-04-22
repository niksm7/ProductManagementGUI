from pickle import *
from first import Product

def addnew(lst,k,pname,pprice,pstock,pcompany):
    flag = 1
    for i in lst:
        if i.pid==k:
            flag-=1
            break
    if flag==1:
        p1 = Product(k,pname,pprice,pstock,pcompany)
        lst.append(p1)
        return True
    else:
        return False

def update(lst,k,pname,pprice,pstock,pcompany):
    for i in lst:
        if i.pid==k:
            Product.setpname(i,pname)
            Product.setpprice(i,pprice)
            Product.setpstock(i,pstock)
            Product.setpcompany(i,pcompany)

def delete(lst,k):
    for i in lst:
        if i.pid == k :
            lst.remove(i)
            return True
    else:
        return False



def readList(f):
    with open(f,'rb') as f2:
        f4 = load(f2)
    return f4

def saveList(f,lst):
    with open(f,'wb') as f1:
        dump(lst,f1)
