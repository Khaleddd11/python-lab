class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity


    @property
    def fuelRate(self):
        return self._fuelRate

    @fuelRate.setter
    def fuelRate(self, value):
        self._fuelRate = max(0, min(100, value))

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self._velocity = max(0, min(200, value))

    def run(self, velocity, distance):
        self.velocity = velocity
        fuel_needed = distance 
        
        if self.fuelRate >= fuel_needed:
            self.fuelRate -= fuel_needed
            self.stop(0)
        else:
            distance_covered = self.fuelRate
            remain_distance = distance - distance_covered
            self.fuelRate = 0
            self.stop(remain_distance)

    def stop(self, remain_distance=0):
        self.velocity = 0
        if remain_distance == 0:
            print("You have arrived at your destination.")
        else:
            print(f"Car stopped. You ran out of fuel. Remaining distance: {remain_distance} km.")


