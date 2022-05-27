# написать программу с пустым классом Counrty. Описать наследуемые от класса Counrty классы Bulgaria,
# Germany, Canada. Дабавить каждому классу поле population и описать метод setPopulation(задать 
# обьекту свойство population) и getPopulation(получить из обьекта сво-во population)..
class Country:
    def __init__(self, population, name):
        self.population = population
        self.name = name
    
    def setPopulation(self, population, name):
        self.population = population
        self.name = name
        return self.population
        return self.name

    def getPopulation(self):
        #return self.population
        #return self.name
        print(f"Население {self.name} составляет {self.population} миллионов")


class Bulgaria(Country):
    population = 75
    name = "Bulgaria"
    pass


class Canada(Country):
    population = 100
    #self.name = name????
    pass


class Germany(Country):
    population = 120
    pass


canada_country = Canada(population=100, name=Canada)

# print(canada_country.setPopulation)
print(canada_country.getPopulation)
# print(Germany.getPopulation)
print(Bulgaria.getPopulation)
