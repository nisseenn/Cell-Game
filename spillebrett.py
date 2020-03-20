from random import randint
from celle import Celle
class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self.versjonsnummer = 0
        self.antallCeller = self._rader*self._kolonner
        self.nabo = []
        celleHolder = []

        for t in range(0, self.antallCeller):
            celleHolder.append(Celle())

        n = self._kolonner
        self.brett = [celleHolder[i:i+n] for i in range(0, len(celleHolder), n)]
        self._generer()

    def tegnBrett(self):
        for row in self.brett:
            for celle in row:
                print(celle.hentStatusTegn(), end=" ")
            print(end="\n")
        print("\n")
        # for u in range(0,10):
        #     print("\n")
        for rad,rader in enumerate(self.brett):
            for kolonne,celle in enumerate(rader):
                naboer = self.finnNabo(rad, kolonne)
                self.nabo.append(naboer)
        levendeCeller = self.finnAntallLevende()
        print("Generasjon: " + repr(self.versjonsnummer) + " - " + "Antall levende celler: " + repr(levendeCeller))
        self.oppdatering()

    def oppdatering(self):
        self.versjonsnummer +=1
        toBeDead = []
        toBeAlive = []
        mergedList = []

        for val,row in enumerate(self.brett):
            for value,celle in enumerate(row):
                mergedList.append([celle])

        for val,celle in enumerate(mergedList):
            mergedList[val].append(self.nabo[val])

        for celler in mergedList:
            celleStatus = celler[0].erLevende()
            celle = celler[0]
            if celleStatus == True:
                dodCount = 0
                aliveCount = 0
                for celler in celler[1]:
                    if celler.erLevende() == True:
                        aliveCount += 1
                    else:
                        dodCount += 1
                if aliveCount < 2:
                    toBeDead.append(celle)
                elif aliveCount == 2 or aliveCount == 3:
                    toBeAlive.append(celle)
                elif aliveCount > 3:
                    toBeDead.append(celle)

            else:
                aliveCount1 = 0
                dodCount1 = 0
                for celler in celler[1]:
                    if celler.erLevende() == True:
                        aliveCount1 += 1
                    else:
                        dodCount1 += 1
                if aliveCount1 == 3:
                    toBeAlive.append(celle)
                else:
                    toBeDead.append(celle)

        for celle in toBeDead:
            celle.settDoed()
        for celle in toBeAlive:
            celle.settLevende()

    def finnAntallLevende(self):
        antallLevende = 0
        antallDode = 0
        for rad in self.brett:
            for celle in rad:
                if celle.erLevende() == True:
                    antallLevende += 1
                else:
                    antallDode += 1

        return antallLevende

    def _generer(self):
        for row in self.brett:
            for celle in row:
                randomNumber = randint(0,2)
                if randomNumber == 1:
                    celle.settLevende()
        self.tegnBrett()
    def finnNabo(self, rad, kolonne):
        mainCoord = [[kolonne+1,rad], [kolonne - 1, rad], [kolonne, rad - 1], [kolonne, rad + 1], [kolonne - 1, rad - 1], [kolonne + 1, rad - 1], [kolonne - 1, rad + 1], [kolonne + 1, rad + 1]]
        filteredCoord = []
        finalList = []
        objectList = []
        for x in mainCoord:
            if x[0] == self._kolonner:
                x.remove(x[0])
            elif x[1] == self._rader:
                x.remove(x[1])
            twoCoord = []
            for t in x:
                if t < 0:
                    x.remove(t)
                else:
                    twoCoord.append(t)
            filteredCoord.append(twoCoord)

        for i in filteredCoord:
            if len(i) < 2:
                pass
            else:
                finalList.append(i)

        for koord in finalList:
            objectList.append(self.brett[int(koord[1])][int(koord[0])])
        return objectList
