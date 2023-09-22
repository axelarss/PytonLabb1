def input_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Felaktig inmatning, ange ett reellt tal.")

""" "input_float" felhanterar användarens input"""

def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 2147483647:
                return value
            else:
                print("Värdet var för stort! Ange ett värde under 2147483648")
        except ValueError:
            print("Felaktig inmatning, ange ett heltal.")

""" "input_int" felhanterar användarens input"""