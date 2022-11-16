import string

class Currency:
    name:string = None
    countries = None
    def __init__(self,name:string):
        self.name = name
        self.countries = []

    def __str__(self):
        return self.name

    def add_country(self,country:string):
        self.countries.append(country)

    def get_countries(self):
        return self.countries

    def get_deep_copy(self):
        c = Currency(self.name)
        for country in self.get_countries():
            c.add_country(country)
        return c

gbp = Currency("GBP")
gbp.add_country("England")
gbp.add_country("Scotland")
print(gbp)
print(gbp.get_countries())
print(gbp.get_deep_copy().get_countries())