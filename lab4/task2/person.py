class Person:
    moods = ("happy", "tired", "lazy")

    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    @property
    def healthRate(self):
        return self._healthRate

    @healthRate.setter
    def healthRate(self, value):
        self._healthRate = max(0, min(100, value))

    def sleep(self, hours):
        if hours == 7:
            self.mood = Person.moods[0] # happy
        elif hours < 7:
            self.mood = Person.moods[1] # tired
        else:
            self.mood = Person.moods[2] # lazy

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def buy(self, items):
        self.money -= (items * 10)