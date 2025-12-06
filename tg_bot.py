class Talaba:
    def __init__(self,ism,yosh,kurs):
        self.ism=ism
        self.yosh=yosh
        self.kurs=kurs
    def get_info(self):
        return f"Ismi:{self.ism} Yoshi:{self.yosh} Kursi:{self.kurs}"

    def get_ism(self):
        return self.ism

    def set_yosh(self,yosh):
        if yosh>0:
            self.__yosh=yosh
        else:
            print("Xato! Yosh manfiy bulmasligi kerak:")

    def set_kurs(self,kurs):
        self.__kurs=kurs

class Shchoolship(Talaba):
    def __init__(self,ism,yosh,kurs,stipendiya):
        super().__init__(ism,yosh,kurs)
        self.__stipendiya=stipendiya
    def get_info(self):
        asosiy=super().get_info()
        return f"{asosiy}, Stipendiya:{self.__stipendiya}"

talabalar=[]
def add_talaba():
    tur=input("Normal yoki Schoolship talaba?  (n/s):")
    ism=input("Ism:")
    yosh=int(input("Yosh:"))
    kurs=int(input("Kurs:"))
    if tur.lower()=="s":
        stipendiya=int(input("Stipendiya:"))
        t=Shchoolship(ism,yosh,kurs,stipendiya)
    else:
        t=Talaba(ism,yosh,kurs)
    talabalar.append(t)
    print("Talabalar qushildi:")

def show_talaba():
    if not talabalar:
        print("Talabalar yuq:")
        return
    for t in talabalar:
        print(t.get_info())

def search_talaba():
    ism=input("Qidiriladigan ism:")
    for t in talabalar:
        if t.get_ism().lower()==ism.lower():
            print(t.get_info())
            return
        print("Talaba topilmadi:")
def delete_talaba():
    ism=input("O'chiriladigan ism:")
    for t in talabalar:
        if t.get_ism().lower()==ism.lower():
            talabalar.remove(t)
            print("Talaba o'chirildi:")
            return
    print("Talaba topilmadi:")

def update_talaba():
    ism=input("Update qilinadigan ism:")

    for t in talabalar:
        if t.get_ism().lower()==ism.lower():
            yangi_yosh=int(input("Yanagi yosh:"))
            yangi_kurs=int(input("Yangi kurs:"))
            t.set_yosh(yangi_yosh)
            t.set_kurs(yangi_kurs)

            print("Talaba yangilandi:")
    print("Talaba topilmadi:")

while True:
    print("""
    n\----Talaba boshqaruvi
    1. Talaba qushish
    2. Talabani kursatish
    3. Talabani qidirish
    4. Talabani o'chirish
    5. Talabani update qilish
    0. chiqish""")

    choice=input("Tanlang:")
    if choice=='1':
        add_talaba()
    elif choice=='2':
        show_talaba()
    elif choice=='3':
        search_talaba()
    elif choice=='4':
        delete_talaba()
    elif choice=='5':
        update_talaba()
    elif choice=='0':
        print("dastur tugadi:")
        break
    else:
        print("Xato! qayta urinib kuring.")

