class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

class Drug(Date):
    def __init__(self, day, month, year, drug_name, company_name):
        super().__init__(day, month, year)
        self.drug_name = drug_name
        self.company_name = company_name

def days_from_creation(drug):
    today = Date(26, 9, 2023)
    days_from_creation = (today.year - drug.year) * 365 + (today.month - drug.month) * 30 + (today.day - drug.day)
    return days_from_creation

day = int(input("Dori chiqarilgan kunni kiriting: "))
month = int(input("Dori chiqarilgan oyni kiriting: "))
year = int(input("Dori chiqarilgan yilni kiriting: "))
drug_name = input("Dorini nomini kiriting: ")
company_name = input("Ishlab chiqaruvchini kiriting: ")

drug = Drug(day, month, year, drug_name, company_name)

days_from_creation = days_from_creation(drug)

print(f"{drug.drug_name} nomli dori {days_from_creation} kun oldin ishlab chiqarilgan.")
