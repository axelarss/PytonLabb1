""" "float_input" felhanterar användarens input"""

def float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Felaktig inmatning, ange ett reellt tal.")

""" "int_input" felhanterar användarens input. Eftersom "int" funktionen har ett cap-value så sätts ett if vilkor. "int"s cap-value hämtades från https://learn.microsoft.com/en-us/cpp/cpp/integer-limits?view=msvc-170"""

def int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 2147483647:
                return value
            else:
                print("Värdet var för stort! Ange ett värde under 2147483648") 
        except ValueError:
            print("Felaktig inmatning, ange ett heltal.")
