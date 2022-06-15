# Solution to Task 9

class buttons:

    def __init__(self, word, spaces, border):
        self.word = word
        self.spaces = spaces
        self.border = border

        print(f"{self.word} Button Specifications:")
        print(f"Button Name: {self.word}")
        print(f"Number of the border characters for the top and the bottom: {len(self.word) + 2 * (1 + self.spaces)}")
        print(f"Number of spaces between the left side border and the first character of the button: {self.spaces}")
        print(f"Number of spaces between the right side border and the first character of the button: {self.spaces}")
        print(f"Characters representing the border {self.border}")
        print()
        print((len(self.word) + 2 * (1 + self.spaces)) * self.border)
        print(f"{self.border}{self.spaces*' '}{self.word}{self.spaces*' '}{self.border}")
        print((len(self.word) + 2 * (1 + self.spaces)) * self.border)


if __name__ == "__main__":

    word = "CANCEL"
    spaces = 10
    border = 'x'

    b1 = buttons(word, spaces, border)
    print("=======================================================")
    b2 = buttons("Notify", 3, '!')
    print("=======================================================")
    b3 = buttons('SAVE PROGRESS', 5, '$')

