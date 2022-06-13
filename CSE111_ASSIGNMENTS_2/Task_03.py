# Solution to Task 4

class Joker:
    def __init__(self, name, power, is_he_psycho):
        self.name = name
        self.power = power
        self.is_he_psycho = is_he_psycho


if __name__ == "__main__":

    j1 = Joker('Heath Ledger', 'Mind Game', False)
    print(j1.name)
    print(j1.power)
    print(j1.is_he_psycho)
    print(" == == == == == == == == == == =")
    j2 = Joker('Joaquin Phoenix', 'Laughing out Loud', True)
    print(j2.name)
    print(j2.power)
    print(j2.is_he_psycho)
    print("== == == == == == == == == == =")

    if j1 == j2:
        print('same')
    else:
        print('different')

    # the value of j1 and j2 is not same also they are in different memory locations

    j2.name = 'Heath Ledger'

    if j1.name == j2.name:
        print('same')
    else:
        print('different')

    # the value of j1 and j2 is same though they are in different memory locations
