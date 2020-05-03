class Product:
    def __init__(self,p,pname,pprice,pstock,pcompany):
        self.pid = p
        self.name = pname
        self.price = pprice
        self.stock = pstock
        self.company = pcompany
    def setpname(self,pname):
        self.name = pname
    def setpprice(self,pprice):
        self.price = pprice
    def setpstock(self,pstock):
        self.stock = pstock
    def setpcompany(self,pcompany):
        self.company = pcompany
