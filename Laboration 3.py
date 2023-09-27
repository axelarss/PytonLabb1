import typed_input

def aritmetisk_summa(aritmetiskt_startvärde, differens, element):
    return (element * (2 * aritmetiskt_startvärde + (element - 1) * differens)) // 2

def geometrisk_summa(geometriskt_startvärde, kvot, element):
    if kvot == 1:
        return geometriskt_startvärde * element
    else:
        return geometriskt_startvärde * (1 - kvot**element) // (1 - kvot)

""" "Main()" funktionen hanterar och kontrollerar användarens inputs och bestämmer med hjälp av def1 och def2 vilket alternativ som är korrekt i sista if delen"""

def main():

    aritmetiskt_startvärde = typed_input.float_input("Skriv in ett aritmetiskt startvärde: ")
    differens = typed_input.float_input("Skriv in funktionens differens: ")
    element = typed_input.int_input("Skriv in antalet element: ")

    while element <= 0:
        element = typed_input.input_int("Du måste använda ett positivt värde till antalet element: ")

    aritmetisk = aritmetisk_summa(aritmetiskt_startvärde, differens, element)

    geometriskt_startvärde = typed_input.float_input("Skriv in ett geometriskt startvärde: ")
    kvot = typed_input.kvot_input("Skriv in värdet på kvot: ")

    geometrisk = geometrisk_summa(geometriskt_startvärde, kvot, element)

    if geometrisk < aritmetisk:
        print("Din aritmetiska summa är större än din geometriska summa")
    elif geometrisk == aritmetisk:
        print("Din aritmetiska och geometriska summa är lika stora")
    else:
        print("Din geometriska summa är större än din aritmetiska summa")

main()