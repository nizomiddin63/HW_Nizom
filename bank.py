import os
os.system("cls")
class bank:
    def __init__(self,f_i_sh,yosh,jinsi,telefon,email,parol_yaratish,yashash_manzili,pasport_raqami_seriyasi,pochta_indexi):
        self.f_i_sh=f_i_sh
        self.yosh=yosh
        self.jinsi=jinsi
        self.telefon=telefon
        self.email=email
        self.parol_yaratish=parol_yaratish
        self.yashash_manzili=yashash_manzili
        self.pasport_raqami_seriyasi=pasport_raqami_seriyasi
        self.pochta_indexi=pochta_indexi
        self.kredit_summa=0
        self.qolgan_summa=0
    def kirish(self,email,parol):
        if email==self.email and parol==self.parol_yaratish:
           return True
        else:
            return False
    def show(self):
        print(f"Ism: {self.f_i_sh} \tYosh: {self.yosh} \tJins: {self.jinsi} \tTelefon: {self.telefon} \tEmail: {self.email} \nParol: {self.parol_yaratish}    Manzil: {self.parol_yaratish}    Pasport_raqam_seriyasi: {self.pasport_raqami_seriyasi} \tPochta_indexi: {self.pochta_indexi}\n")
        print(70*"*")
    def menu(self):
        print("\t1.Kredit olish  ")
        print("\t2.Kredit hisoblash kalkulyatori  ")
        print("\t3.Parol o'zgartirish  ")
        choose=int(input())
        if choose==1:
            kredit=int(input("Qancha miqdorda kredit olmoqchisiz: "))
            foiz=int(input("Kredit foizini kiriting: "))
            yil=int(input("Necha yilga olmoqchisiz: "))
            print("\n")
            print(f"Siz uchun 1 oylik summa {(kredit*(foiz//100))//(12*yil)+kredit//(yil*12)} ni tashkil etadi.")
            self.kredit_summa=kredit
            self.qolgan_summa=kredit
        elif choose==2:
            print("1.Kredit to'lash ")
            print("2.Qolgan kredit summa ")
            choose2=int(input())
            if choose2==1:
                tolash=int(input("To'lov miqdorini kiriting: "))
                qolgan_summa=kredit-tolash
                print("To'lov muvaffaqiyatli amalga oshirildi! ")
                print(f"Qolgan kredit summasi:\t\t{qolgan_summa}")
            elif choose2==2:
                print(f"Qolgan kredit summa: \t {qolgan_summa}")
        elif choose==3:
            eski_email=input("Email kiriting:\t")
            eski_parol=int(input("Eski parolni kiriting:\t"))
            if self.email==eski_email and self.parol_yaratish==eski_parol:
                new_parol=int(input("Yangi parolni kiriting:\t"))
                self.parol_yaratish=new_parol
                print("Parol muvaffaqiyatli o'zgartirildi!\t")
class user:
    odamlar=[]
    while 1:
        human=int(input("Agar ro'yxatdan o'tmoqchi bo'lsangiz 1 ni bosing! \nTizimga kirish uchun 2 ni bosing! \nDasturdan chiqmochi bo'lsangiz 0 ni bosing! "))
        if human==1:
            os.system("cls")
            fi=input("Foydalanuvchi FISH sini kiriting (M: Abror Aliyev Alimurodovich):  ")
            yo=int(input("Yosh:  "))
            ji=input("Jins:  ")
            te=int(input("Telefon raqam:  "))
            em=input("Email pochta:  ")
            pr=int(input("Parol:  "))
            ysh=input("Yashash manzil:  ")
            ps_r_s=input("Pasport raqam seriya:  ")
            pch_in=input("Pochta index:  ")
            odam=bank(fi,yo,ji,te,em,pr,ysh,ps_r_s,pch_in)
            odamlar.append(odam)
            print("Foydalanuvchi ma'lumotlari muvaffaqiyatli kiritildi!\n")
        elif human==2:
            em=input("Email kiriting! ")
            prl=int(input("Parol kiriting! "))
            for x in odamlar:
                if x.kirish(em,prl)==True:
                    x.menu()
        elif human==0:
            break
    print("\n")
    print("Foydalanuvchilar ma'lumotlari!")
    print(45*"*-")
    for x in odamlar:
        x.show()
