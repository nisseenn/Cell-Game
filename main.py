from spillebrett import Spillebrett

def generateRandomNumber():
    print("Oppgi dimensjon for x-akse: ")
    xakse = input()
    print("Oppgi dimensjon for y-akse: ")
    yakse = input()
    return xakse,yakse

def main():
    x,y = generateRandomNumber()
    brett = Spillebrett(int(x),int(y))

    print("trykk enter for aa fortsette, skriv q og trykk enter for aa avslutte: ")
    userInput = input()
    while userInput == "":
        brett.tegnBrett()
        print("trykk enter for aa fortsette, skriv q og trykk enter for aa avslutte: ")
        userInput = input()
    if "q" in userInput or "Q" in userInput:
        pass
# starte hovedprogrammet
main()
