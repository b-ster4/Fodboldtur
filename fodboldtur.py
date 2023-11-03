##---------- Libraries ----------##

import pickle



##---------- External files ----------##

filename = '/Users/buster/PycharmProjects/Fodboldtur/betalinger.pk'

fodboldtur = {}



##---------- Variables ----------##

antal = 0



##---------- Functions ----------##

def afslut():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    print("Programmet er afsluttet!")



def printliste():
    for item in fodboldtur.items():
         print(item)
    menu()



def person():
    navn = input("Navn: ")
    if navn in fodboldtur.keys():
        print(f'{navn} {fodboldtur[navn]}')
        valg = input("Indsæt beløb? (Y/N) : ")
        if (valg == 'Y') or (valg == 'y'):
            beløb = input("Beløb: ")
            try:
                fodboldtur[navn] += float(beløb)
                print(f'{navn} {fodboldtur[navn]}')
                menu()
            except:
                print("not a number")
                person()
        elif (valg == 'N') or (valg == 'n'):
            person()
        else:
            menu()
    else:
        menu()



def reset():
    valg = input("Reset alle(1) indbetalinger eller enkelte(2) indbetalinger: ")
    if (valg == '1'):
        for name in fodboldtur.keys():
            fodboldtur[name] = 0
        for item in fodboldtur.items():
            print(item)
        menu()
    elif (valg == '2'):
        navn = input("Navn: ")
        if navn in fodboldtur.keys():
            fodboldtur[navn] = 0
            print(f'{navn} {fodboldtur[navn]}')
            menu()
        else:
            reset()
    else:
        menu()



def menu():
    print("MENU")
    print("1: Print liste")
    print("2: Find person og indbetal beløb")
    print("3: Reset indsat beløb")
    print("4: Afslut program")
    valg = input("Indtast dit valg: ")
    if (valg == '1'):
        printliste()
    elif (valg == '2'):
        person()
    elif (valg == '3'):
        reset()
    elif (valg == '4'):
        afslut()
    elif (valg == 'antal'):
        print(antal)
        menu()
    else:
        menu()



##---------- Startup code ----------##

infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()

for item in fodboldtur.items():
    antal = antal + 1

menu()

