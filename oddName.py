"""
Mikkel Hansen
"""


def main():
    name = str(input("input your name: "))

    for char in name:
        print(char, char.isalpha())

    if all(x.isalpha() or x.isspace() for x in name):
        print("Only alphabetical letters and spaces: yes")
    else:
        print("Only alphabetical letters and spaces: no")


main()
