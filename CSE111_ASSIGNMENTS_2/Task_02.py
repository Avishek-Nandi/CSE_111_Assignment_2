# Solution to Task 2

class Flower:
    def __init__(self, name="New_ful", color="Janina vai", num_of_petal=0):
        self.name = name
        self.color = color
        self.num_of_petal = num_of_petal


if __name__ == "__main__":

    flower1 = Flower()
    flower1.name = "Rose"
    flower1.color = "Red"
    flower1.num_of_petal = 6
    print("Name of this flower:", flower1.name)
    print("Color of this flower:", flower1.color)
    print("Number of petal:", flower1.num_of_petal)
    print(" == == == == == == == == == == =")
    flower2 = Flower()
    flower2.name = "Orchid"
    flower2.color = "Purple"
    flower2.num_of_petal = 4
    print("Name of this flower:", flower2.name)
    print("Color of this flower:", flower2.color)
    print("Number of petal:", flower2.num_of_petal)

    print(" == == == == == == == == == == =")
    print(flower1)
    print(flower2)

    if flower1 is flower2:
        print("They are same")
    else:
        print("They are different")


