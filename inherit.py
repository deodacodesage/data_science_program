from classes import Human

class Swimmer(Human):
    def swim(self):
        print(self.name, "is swimming now")
career = Swimmer("Sola", "28", "African", "Man","Christianity")
career.swim()