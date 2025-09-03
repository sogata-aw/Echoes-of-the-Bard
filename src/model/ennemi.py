class Ennemi:
    def __init__(self):
        self.pv = 30
        self.difficulte = 0
    def getPv(self):
        return self.pv
    def setPv(self, pv):
        self.pv = pv
    def getDifficulte(self):
        return self.difficulte
    def setDifficulte(self, difficulte):
        self.difficulte = difficulte

def main():
    print('MODE TEST/DEBUG')
    ennemi1 = Ennemi()
    print(ennemi1.getPv())
    print(ennemi1.setPv(ennemi1.getPv() - 5))
    print(ennemi1.getPv())

if __name__ == "__main__":
    main()