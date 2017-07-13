import sys
from math import trunc

def convert(args):
    """ Selecteur du convertisseur selon les devises """
    if (set(args[1:]).issubset(["EUR", "USD"])):
        if args[1] == "EUR":
            return convertEURToUSD(args[0], False)
        else: 
            return convertEURToUSD(args[0], True)

    if (set(args[1:]).issubset(["EUR", "GBP"])):
        if args[1] == "EUR":
            return convertEURToGBP(args[0], False)
        else: 
            return convertEURToGBP(args[0], True)

    if (set(args[1:]).issubset(["EUR", "JPY"])):
        if args[1] == "EUR":
            return convertEURToJPY(args[0], False)
        else: 
            return convertEURToJPY(args[0], True)

    if (set(args[1:]).issubset(["EUR", "CHF"])):
        if args[1] == "EUR":
            return convertEURToCHF(args[0], False)
        else: 
            return convertEURToCHF(args[0], True)

    if (set(args[1:]).issubset(["USD", "GBP"])):
        if args[1] == "USD":
            return convertUSDToGBP(args[0], False)
        else: 
            return convertUSDToGBP(args[0], True)

    if (set(args[1:]).issubset(["USD", "JPY"])):
        if args[1] == "USD":
            return convertUSDToJPY(args[0], False)
        else: 
            return convertUSDToJPY(args[0], True)

    if (set(args[1:]).issubset(["CHF", "USD"])):
        if args[1] == "CHF":
            return convertCHFToUSD(args[0], False)
        else: 
            return convertCHFToUSD(args[0], True)

    if (set(args[1:]).issubset(["CHF", "JPY"])):
        if args[1] == "CHF":
            return convertCHFToJPY(args[0], False)
        else: 
            return convertCHFToJPY(args[0], True)

    if (set(args[1:]).issubset(["CHF", "GBP"])):
        if args[1] == "CHF":
            return convertCHFToGBP(args[0], False)
        else: 
            return convertCHFToGBP(args[0], True)

    if (set(args[1:]).issubset(["JPY", "GBP"])):
        if args[1] == "JPY":
            return convertJPYToGBP(args[0], False)
        else: 
            return convertJPYToGBP(args[0], True)


def convertEURToUSD(montant, reverse):
    """ Convertie l'EUR en USD
    1EUR -> 1.14 USD """
    if not reverse:
        resultat = montant * 1.14
    else:
        resultat = montant / 1.14
    return resultat

def convertCHFToJPY(montant, reverse):
    """ Convertie le CHF en JPY 
    1CHF -> 118.1 JPY """
    if not reverse:
        resultat = montant * 118.1
    else:
        resultat = montant / 118.1
    return resultat

def convertUSDToGBP(montant, reverse):
    """    Convertie l'USD en GBP
    1USD -> 0.776 GBP """
    if not reverse:
        resultat = montant * 0.776
    else:
        resultat = montant / 0.776
    return resultat

def convertJPYToGBP(montant, reverse):
    """ Convertie le JPY en GBP
    1JPY -> 0.007 GBP """
    if not reverse:
        resultat = montant * 0.007
    else:
        resultat = montant / 0.007
    return resultat

def convertEURToGBP(montant, reverse):
    """ Convertie l'EUR en GBP """
    if not reverse:
        resultat = convertUSDToGBP(convertEURToUSD(montant, False), False)
    else:
        resultat = convertEURToUSD(convertUSDToGBP(montant, True), True)
    return resultat

def convertEURToCHF(montant, reverse):
    """ Convertie l'EUR en CHF """
    if not reverse:
        resultat = convertCHFToJPY(convertEURToJPY(montant, False), True)
    else:
        resultat = convertEURToJPY(convertCHFToJPY(montant, False), True)
    return resultat

def convertEURToJPY(montant, reverse):
    """ Convertie l'EUR en JPY """
    if not reverse:
        resultat = convertJPYToGBP(convertEURToGBP(montant, False), True)
    else:
        resultat = convertEURToGBP(convertJPYToGBP(montant, False), True)
    return resultat


def convertCHFToUSD(montant, reverse):
    """ Convertie le CHF en USD """
    if not reverse:
        resultat = convertUSDToJPY(convertCHFToJPY(montant, False), True)
    else:
        resultat = convertCHFToJPY(convertUSDToJPY(montant, False), True)
    return resultat

def convertCHFToGBP(montant, reverse):
    """ Convertie le CHF en GBP """
    if not reverse:
        resultat = convertJPYToGBP(convertCHFToJPY(montant, False), False)
    else:
        resultat = convertCHFToJPY(convertJPYToGBP(montant, True), True)
    return resultat


def convertUSDToJPY(montant, reverse):
    """ Convertie l'USD en JPY """
    if not reverse:
        resultat = convertJPYToGBP(convertUSDToGBP(montant, False), True)
    else:
        resultat = convertUSDToGBP(convertJPYToGBP(montant, False), True)
    return resultat


def test():
    """ Méthode pour lancer différents tests """
    print("EURToUSD " + str(convertEURToUSD(3, False)))
    print("USDToEUR " + str(convertEURToUSD(convertEURToUSD(3, False), True)))

    print("EURToGBP " + str(convertEURToGBP(4, False)))
    print("GBPToEUR " + str(convertEURToGBP(convertEURToGBP(4, False), True)))

    print("EURToJPY " + str(convertEURToJPY(5, False)))
    print("JPYToEUR " + str(convertEURToJPY(631.885, True)))

    print("EURToCHF " + str(convertEURToCHF(6, False)))
    print("CHFToEUR " + str(convertEURToCHF(convertEURToCHF(6, False), True)))

    print("USDToGBP " + str(convertUSDToGBP(7, False)))
    print("GBPToUSD " + str(convertUSDToGBP(convertUSDToGBP(7, False), True)))

    print("USDToJPY " + str(convertUSDToJPY(8, False)))
    print("JPYToUSD " + str(convertUSDToJPY(convertUSDToJPY(8, False), True)))

    print("USDToCHF " + str(convertCHFToUSD(9, True)))
    print("CHFToUSD " + str(convertCHFToUSD(convertCHFToUSD(9, True), False)))

    print("CHFToJPY " + str(convertCHFToJPY(10, False)))
    print("JPYToCHF " + str(convertCHFToJPY(convertCHFToJPY(10, False), True)))

    print("CHFToGBP " + str(convertCHFToGBP(11, False)))
    print("GBPToCHF " + str(convertCHFToGBP(convertCHFToGBP(11, False), True)))

    print("JPYToGBP " + str(convertJPYToGBP(12, False)))
    print("GBPToJPY " + str(convertJPYToGBP(convertJPYToGBP(12, False), True)))


if __name__ == "__main__":
    """ Lancement du programme
    il peut prendre des arguments en paramètres, sinon demande les valeurs à l'utilisateur """ 

    if len(sys.argv) == 4:
        args = sys.argv[1:]
        args[0] = float(args[0])
    elif len(sys.argv) == 2 and sys.argv[1] in "Test":
        test()
        exit()
    else:
        montant = input("Montant : ")
        devorg = input("Devise d'origine : ")
        devdest = input("Devise de destination : ")
        args = [float(montant), devorg, devdest]
    
    args[1:] = [item.upper() for item in args[1:]]

    if(set(args[1:]).issubset(["EUR", "JPY", "USD", "GBP", "CHF"])):
        print (trunc(convert(args)*1000) /1000)
    else:
        print("conversion impossible")
