class Remote:
    def power_on(self):
        return 'device is powered on'
    def power_off(self):
        return 'device is powered off'
class TV:
    def __init__(self):
        self.remote = Remote()
    def turn_on(self):
        return self.remote.power_on()
    def turn_off(self):
        return self.remote.power_off()


obj = TV()
print(obj.turn_off())