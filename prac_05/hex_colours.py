COLOR_CODES = {
    "absolute zero": "#0048ba",
    "acid green": "#b0bf1a",
    "aliceblue": "#f0f8ff",
    "alizarin crimson": "#e32636",
    "amaranth": "#e52b50",
    "amber": "#ffbf00",
    "amethyst": "#9966cc",
    "antiquewhite": "#faebd7",
    "antiquewhite1": "#ffefdb",
    "antiquewhite2": "#eedfcc"
}


def main():
    print("Welcome to the Hexadecimal Color Code Lookup!")

    color_name = input("Enter a color name: ").lower()
    while color_name != "":
        try:
            print(f"The color code for '{color_name}' is {COLOR_CODES[color_name]}")
        except KeyError:
            print("Invalid color name. Please try again.")

        color_name = input("Enter a color name: ").lower()

    print("Goodbye!")


main()
