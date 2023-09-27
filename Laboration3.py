"""Importerar en fil som felhanterar användarens inmatning"""
import typed_input

def aritmetisk_summa(aritmetiskt_startvärde, differens, element):
    """Funktion som beräknar aritmetisk summa."""
    return (element * (2 * aritmetiskt_startvärde + (element - 1) * differens)) // 2

def geometrisk_summa(geometriskt_startvärde, kvot, element):
    """Funktion som beräknar geometrisk summa."""
    if kvot == 1:
        return geometriskt_startvärde * element
    else:
        return geometriskt_startvärde * (1 - kvot**element) // (1 - kvot)

def main():
    """Main-funktionen hanterar och kontrollerar användarens inputs 
    och bestämmer med hjälp av def1 och def2 vilket alternativ som är korrekt i sista if delen"""

    aritmetiskt_startvärde = typed_input.float_input("Skriv in ett aritmetiskt startvärde:")
    differens = typed_input.float_input("Skriv in funktionens differens:")
    element = typed_input.int_input("Skriv in antalet element:")

    geometriskt_startvärde = typed_input.float_input("Skriv in ett geometriskt startvärde:")
    kvot = typed_input.kvot_input("Skriv in värdet på kvot:")

    aritmetisk = aritmetisk_summa(aritmetiskt_startvärde, differens, element)
    geometrisk = geometrisk_summa(geometriskt_startvärde, kvot, element)

    if geometrisk < aritmetisk:
        print("Din aritmetiska summa är större än din geometriska summa")
    elif geometrisk == aritmetisk:
        print("Din aritmetiska och geometriska summa är lika stora")
    else:
        print("Din geometriska summa är större än din aritmetiska summa")

main()