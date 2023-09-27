
def float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Felaktig inmatning, ange ett reellt tal.")

def kvot_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value != 1:
                return value
            else:
                print("Kvot värdet får inte vara 1: ")
        except ValueError:
            print("Felaktig inmatning, ange ett reellt tal.")

def int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Du måste använda ett positivt värde till antalet element: ")
        except ValueError:
            print("Felaktig inmatning, ange ett heltal.")


