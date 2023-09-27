""" Denna fil hanterar alla våra felhanteringar för Laboration 3 """
def float_input(prompt):
    """ Felhanterar angivna värden för float tal.
     Anges en bokstav bes användren skriva in ett positivt tal """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Felaktig inmatning, ange ett reellt tal.")

def kvot_input(prompt):
    """ Felhanterar de värden som användaren lägger in som kvot.
         Då vi inte kan dela med 0 får man inte ange 1 som kvot på geometriska_summan. 
         Och anges något annat än ett positivt heltal skickas frågan igen """
    while True:
        try:
            value = float(input(prompt))
            if value != 1: #Får ej vara 1 då (1 - 1) = 0 i geometrisk_summa
                return value
            else:
                print("Kvot värdet får inte vara 1: ")
        except ValueError:
            print("Felaktig inmatning, ange ett reellt tal.")

def int_input(prompt):
    """ Felhanterar värden för heltalen och ber användaren
        ange ett postivt heltal som antal element istället för 0, bokstäver eller andra symboler """
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Du måste använda ett positivt värde till antalet element: ")
        except ValueError:
            print("Felaktig inmatning, ange ett heltal.")
