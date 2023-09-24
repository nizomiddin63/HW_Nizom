
class animal:
    def __init__(self) -> None:
        pass
    def eat(self):
        print("Eat methodi yaratildi! ")
    def is_uy_hayvoni(self):
        print("Uy hayvoni methodi yaratildi! ")
    def examples_for_meals(self):
        print("Yeyishi mumkin bo'lgan narsalar!  ")
   
class yirtqichlar(animal):
    def __init__(self,name,is_live_home=False) -> None:
       self.name=name
       self.is_live_home=is_live_home
    def eat(self,name):
            print(f"{name} goshtxor hayvon!\t")
    def is_uy_hayvoni(self,name,is_live_home):
        if is_live_home == False:
            print(f"{name} yovvoyi hayvon uy hayvoni emas!\t")
        else:
            print(f"{name} uy hayvoni! ")
    def examples_for_meals(self,name,is_live_home):
            if is_live_home==False:
                print(f"{name} goshtxor hayvon bolganligi sababli odatda otxor hayvonlarni ov qilib yeydi! ")
            else:
                 print(f"{name} odatda uy egalari bergan narsalar bilan oziqlanadi!  ")
    
class otxorlar(animal):
    def __init__(self,name,is_live_home=False) -> None:
       self.name=name
       self.is_live_home=is_live_home
    def eat(self,name):
            print(f"{name} otxor hayvon!  ")
    def is_uy_hayvoni(self,name,is_live_home):
        if is_live_home==False:
            print(f"{name} yovvoyi hayvon uy hayvoni emas!  ")
        else:
            print(f"{name} uy hayvoni! ")
    def examples_for_meals(self,name):
            print(f"{name} otxor hayvon bo'lganligi sababli ot va shunga o'xshash ovqatlar bilan oziqlanadi! ")
       
os.system("cls")
hayvon=animal()
hayvon.eat()
hayvon.examples_for_meals()
hayvon.is_uy_hayvoni()
print("\n")
hayvon1=yirtqichlar("It",True)
hayvon1.eat("It")
hayvon1.examples_for_meals("It",True)
hayvon1.is_uy_hayvoni("It",True)
print("\n")
hayvon2=otxorlar("Qo'y")
hayvon2.eat("Qo'y")
hayvon2.examples_for_meals("Qo'y")
hayvon2.is_uy_hayvoni("Q'oy",True)


