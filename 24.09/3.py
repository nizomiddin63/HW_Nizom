import os
class printer():
    def __init__(self) -> None:
        self.printers=[]
        self.model=""
        self.speed=0
        self.price=0
        self.type=""
    def input(self,m,s,p,t):
        self.model=m
        self.speed=s
        self.price=p
        self.type=t
        self.printers.append((self.model,self.speed,self.price,self.type))

    def show(self):
        for x in self.printers:
            print("{:15s} {:-15d} {:-15d} {:15s}".format(x[0],x[1],x[2],x[3]))

    def sortlash(self):
        res=sorted(self.printers,key=lambda x: x[2])
        for x in res:
            print("{:15s} {:-15d} {:-15d} {:15s}".format(x[0],x[1],x[2],x[3]))

    def show_input(self,typ):
        for x in self.printers:
            if x[3]==typ:
                print("{:15s} {:-15d} {:-15d} {:15s}".format(x[0],x[1],x[2],x[3]))
                break
os.system("cls")
object=printer()
for x in range(5):
    md=input(f"{x+1} ning modelini kiriting!--> ")
    sp=int(input("Tezligini kiriting-->  "))
    pr=int(input("Narxini kiriting-->  "))
    ty=input("Turini kiriting-->  ")
    object.input(md,sp,pr,ty)
object.show()
print("\n****Narxiga ko'ra sortlangan holatdagi ro'yxat!*****\n")
object.sortlash()
turi=input("Qidirayotgan printer turini kiriting-->  ")
object.show_input(turi)


