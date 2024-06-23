import sys

def convert(string):
    whitespace = ""
    binary_values = [bin(ord(char))[2:] for char in string]

    for binary in binary_values:
        whitespace += "   "
        for bit in binary:
            if bit == '1':
                whitespace += "\t"
            else:
                whitespace += " "
        whitespace += "\n\t\n  "

    whitespace += "\n\n"
    return whitespace


with open('config.ws', 'w') as file:
    file.write(convert(sys.argv[1]))