class Passport:
    def __init__(self, country, passport_number, owner_name):
        self.country = country
        self.passport_number = passport_number
        self.owner_name = owner_name

    def info(self):
        return f"Owner: {self.owner_name}, Country: {self.country}, Passport No: {self.passport_number}"
    

class ForeignPassport(Passport):
    def __init__(self, country, passport_number, owner_name, foreign_passport_number, visas):
        super().__init__(country, passport_number, owner_name)
        self.foreign_passport_number = foreign_passport_number
        self.visas = visas # lista wiz

    def info(self):
        return (f"{super().info()}, Foreign Passport No: {self.foreign_passport_number}, "
                f"Visas: {', '.join(self.visas)}")
    
fp = ForeignPassport("Poland", "PL123456", "Jan Kowalski", "FR123123", ["USA", "Canada"])
print(fp.info())
