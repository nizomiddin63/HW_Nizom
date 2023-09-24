import os
os.system("cls")
class first():
    def __init__(self,ls) -> list:
        self.ls=ls
    def input(self,lss):
        self.ls=lss
        n=int(input("List uzunligini kiriting--> "))
        for x in range(n):
            item=int(input(f"Listning {x+1} chi elementini kiriting--> "))
            lss.append(item)
    def output(self,lss)->list:
        self.ls=lss
        print(f"List elementlari--> {lss}")
class second(first):
    def __init__(self,ls) -> list:
        self.ls=ls
    def input(self,lss):
        self.ls=lss
        n=int(input("List uzunligini kiriting--> "))
        check=int(input("Elementlar int tipida bo'lsa 1 ni kiriting yoki false tipida bo'lsa 0 ni kiriting! "))
        if check==1:
            for x in range(n):
                item=int(input(f"Listning {x+1} chi elementini kiriting--> "))
                lss.append(item)
        elif check==0:
            for x in range(n):
                item=float(input(f"Listning {x+1} chi elementini kiriting--> "))
                lss.append(item)
        else:
            print("Ma'lumot no'to'g'ri kiritildi.Iltimos qayta urinib ko'ring! ")
    def output(self,lss)->list:
        self.ls=lss
        print(f"List elementlari--> {lss}")
class third(first):
    def __init__(self,ls) -> list:
        self.ls=ls
    def input(self,lss):
        self.ls=lss
        n=int(input("List uzunligini kiriting--> "))
        check=int(input("Elementlar int  tipida bo'lsa 1 ni kiriting!\nElementlar float  tipida bo'lsa 2 ni kiriting!\nElementlar bool    tipida bo'lsa 3 ni kiriting!\n"))
        if check==1:
            for x in range(n):
                item=int(input(f"Listning {x+1} chi elementini kiriting--> "))
                lss.append(item)
        elif check==2:
            for x in range(n):
                item=float(input(f"Listning {x+1} chi elementini kiriting--> "))
                lss.append(item)
        elif check==3:
            for x in range(n):
                item=bool(input(f"Listning {x+1} chi elementini kiriting--> "))
                lss.append(item)
        else:
            print("Ma'lumot no'to'g'ri kiritildi.Iltimos qayta urinib ko'ring! ")
    def output(self,lss)->list:
        self.ls=lss
        print(f"List elementlari--> {lss}")
class fourth(first):
    def __init__(self,ls) -> list:
        self.ls=ls
    def input(self,lss):
        self.ls=lss
        n=int(input("List uzunligini kiriting--> "))
        check=int(input("Elementlar int    tipida bo'lsa 1 ni kiriting--> \nElementlar float  tipida bo'lsa 2 ni kiriting!--> \nElementlar bool   tipida bo'lsa 3 ni kiriting!--> \nElementlar str    tipida bo'lsa 4 ni kiriting!--> "))
        if check==1:
            for x in range(n):
                item=int(input(f"Listning {x+1} chi elementini kiriting--> "))
                lss.append(item)
        elif check==2:
            for x in range(n):
                item=float(input(f"Listning {x+1} chi elementini kiriting--> "))
                lss.append(item)
        elif check==3:
            for x in range(n):
                item=bool(input(f"Listning {x+1} chi elementini kiriting--> "))
                lss.append(item)
        elif check==4:
            for x in range(n):
                item=input(f"Listning {x+1} chi elementini kiriting--> ")
                lss.append(item)
        else:
            print("Ma'lumot no'to'g'ri kiritildi.Iltimos qayta urinib ko'ring! ")
    def output(self,lss)->list:
        self.ls=lss
        print(f"List elementlari--> {lss}")
    



l=[]
os.system("cls")
# lss=first(l)
# lss.input(l)
# lss.output(l)

# ls1=second(l)
# ls1.input(l)
# ls1.output(l)

# ls2=third(l)
# ls2.input(l)
# ls2.output(l)

ls3=fourth(l)
ls3.input(l)
ls3.output(l)




