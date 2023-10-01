import os
import random as ran
from abc import*
class Counter_strike(ABC):
    def __init__(self):
        self.name1=""
        self.name2=""
        self.part_of_body=0
    @abstractmethod
    def otish(self):
        pass
    def show_winner(self):
        pass
    @abstractmethod
    def get_name(self):
        pass

class Terrorist(Counter_strike):
    def __init__(self):
        super().__init__()
        self.name1="Terrorist"
    def otish(self,soul1):
        self.soul1=soul1
        foiz=ran.randint(1,3)
        if foiz==1:
            self.soul1-=60
        elif foiz==2:
            self.soul1-=25
        elif foiz==3:
            self.soul1-=15
        return self.soul1
    def show_winner(self,count1,count2):
        print(f"Terrorist yutdi:     \t\tHisob:      \tTerrorist {count1}:{count2} Counter_Terrorist")
    def get_name(self):
        return self.name1

class Counter_Terrorist(Counter_strike):
    def __init__(self):
        super().__init__()
        self.name2="Counter_Terrorist"
    def otish(self,soul2):
        self.soul2=soul2
        foiz=ran.randint(1,3)
        if foiz==1:
            self.soul2-=60
        elif foiz==2:
            self.soul2-=25
        elif foiz==3:
            self.soul2-=15
        return self.soul2
    def show_winner(self,count1,count2):
        print(f"Counter_Terrorist yutdi:     \tHisob:    \t Terrorist {count1}:{count2} Counter_Terrorist")
    def get_name(self):
        return self.name2
    
os.system("cls")
terros=Terrorist()
counterchi=Counter_Terrorist()
counter_of_terrorist=0
counter_of_counterchi=0
print("\n\t\t********Start game********\t\t\n")
for x in range(15):
    soul1=100
    soul2=100
    while 1:
        navbat=ran.randint(0,1)
        if navbat==1:
            terros.otish(soul1)
            soul1= terros.otish(soul1)
        else:
            counterchi.otish(soul2)
            soul2= counterchi.otish(soul2)
        if terros.otish(soul1)<=0:
            counter_of_counterchi+=1
            counterchi.show_winner(counter_of_terrorist,counter_of_counterchi)
            break
        elif counterchi.otish(soul2)<=0:
            counter_of_terrorist+=1
            terros.show_winner(counter_of_terrorist,counter_of_counterchi)
            break
        
            
print(f"\nYakuniy hisob:  [{terros.get_name()}] {counter_of_terrorist}:{counter_of_counterchi} [{counterchi.get_name()}]\n")
