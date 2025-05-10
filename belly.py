class Belly:
    def __init__(self):
        self.cukes = 0
        self.hours = 0

    def eat(self, cukes):
        self.cukes += cukes

    def wait(self, hours):
        if hours > 0:
            self.hours += hours

    def growls(self):
        return self.cukes > 10 and self.hours >= 2
