"""Här importerar vi en fil som heter "typed_input" vars funktionere vi kan nyttja senare"""
import typed_input



def aritmetisk_summa(a_1, d, n):
    return (n * (2 * a_1 + (n - 1) * d)) // 2

def geometrisk_summa(g_1, r, n):
    if r == 1:
        return g_1 * n
    else:
        return g_1 * (1 - r**n) // (1 - r)
    
""" "Main()" funktionen hanterar och kontrollerar användarens inputs och bestämmer med hjälp av def1 och def2 vilket alternativ som är korrekt i sista if delen"""

def main():

    a1 = typed_input.float_input("Skriv in värdet på a1: ")
    d = typed_input.float_input("Skriv in värdet på d: ")
    n = typed_input.int_input("Skriv in värdet på n: ")

    while n <= 0:
        n = typed_input.input_int("Skriv in värdet på n: ")

    aritmetisk = aritmetisk_summa(a1, d, n)

    g1 = typed_input.float_input("Skriv in värdet på g1: ")
    q = typed_input.float_input("Skriv in värdet på q: ")

    while q <= 0:
        q = typed_input.float_input("Skriv in värdet på q: ")

    geometrisk = geometrisk_summa(g1, q, n)

    if geometrisk < aritmetisk:
        print("Din aritmetiska summa är större än din geometriska summa")
    elif geometrisk == aritmetisk:
        print("Din aritmetiska och geometriska summa är lika stora")
    else:
        print("Din geometriska summa är större än din aritmetiska summa")

main()
