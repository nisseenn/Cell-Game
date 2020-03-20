class Celle:
# Konstruktør
    def __init__(self):
        self.status = False
    # Endre status
    def settDoed(self):
        self.status = False
    def settLevende(self):
        self.status = True
    # Hente status
    def erLevende(self):
        return self.status
    def hentStatusTegn(self):
        if self.status == True:
            return "O"
        else:
            return "."
# test = Celle()
# test.hentStatusTegn()
# test.erLevende()
