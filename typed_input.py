def input_float(prompt):
    while True:
        try:
            user_input = input(prompt)
            value = float(user_input)
            return value
        except ValueError:
            print("Felaktig inmatning, ange ett decimaltal.")

def input_int(prompt):
    while True:
        try:
            user_input = input(prompt)
            value = int(user_input)
            return value
        except ValueError:
            print("Felaktig inmatning, ange ett heltal.")