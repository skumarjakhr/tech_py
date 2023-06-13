def draw_name(name, spaces_between_chars):
    ascii_art = {
        'A': ["  AA  ", " A  A ", "AAAAA", "A    A", "A    A"],
        'B': ["BBBB ", "B   B", "BBBB ", "B   B", "BBBB "],
        'C': [" CCCC ", "C     ", "C     ", "C     ", " CCCC "],
        'D': ["DDDD ", "D   D", "D   D", "D   D", "DDDD "],
        'E': ["EEEEE", "E    ", "EEEEE", "E    ", "EEEEE"],
        'F': ["FFFFF", "F    ", "FFFF ", "F    ", "F    "],
        'G': [" GGGG ", "G     ", "G  GG ", "G   G ", " GGGG "],
        'H': ["H   H", "H   H", "HHHHH", "H   H", "H   H"],
        'I': ["IIIII", "  I  ", "  I  ", "  I  ", "IIIII"],
        'J': ["   J ", "   J ", "   J ", "J  J ", " JJ  "],
        'K': ["K   K", "K  K ", "KKK  ", "K  K ", "K   K"],
        'L': ["L     ", "L     ", "L     ", "L     ", "LLLLL"],
        'M': ["M   M", "MM MM", "M M M", "M   M", "M   M"],
        'N': ["N   N", "NN  N", "N N N", "N  NN", "N   N"],
        'O': [" OOO ", "O   O", "O   O", "O   O", " OOO "],
        'P': ["PPPP ", "P   P", "PPPP ", "P    ", "P    "],
        'Q': [" QQQ ", "Q   Q", "Q   Q", "Q  Q ", " QQ Q"],
        'R': ["RRRR ", "R   R", "RRRR ", "R R  ", "R  RR"],
        'S': [" SSSS ", "S     ", " SSSS ", "    S ", " SSSS "],
        'T': ["TTTTT", "  T  ", "  T  ", "  T  ", "  T  "],
        'U': ["U   U", "U   U", "U   U", "U   U", " UUU "],
        'V': ["V   V", "V   V", "V   V", " V V ", "  V  "],
        'W': ["W   W", "W   W", "W W W", "WW WW", "W   W"],
        'X': ["X   X", " X X ", "  X  ", " X X ", "X   X"],
        'Y': ["Y   Y", " Y Y ", "  Y  ", "  Y  ", "  Y  "],
        'Z': ["ZZZZZ", "   Z ", "  Z  ", " Z   ", "ZZZZZ"],
    }

    name = name.upper()

    lines = [""] * 5

    for char in name:
        if char.isalpha():
            if char in ascii_art:
                for i, line in enumerate(ascii_art[char]):
                    lines[i] += line + " " * spaces_between_chars
            else:
                for i in range(5):
                    lines[i] += " " * (7 + spaces_between_chars)
        else:
            for i in range(5):
                lines[i] += " " * (7 + spaces_between_chars)

    for line in lines:
        print(line)


# Example usage
name = input("Enter the name: ")
spaces = int(input("Enter the number of spaces between characters: "))
#print('')
#print('')
#print('')

draw_name(name, spaces)
