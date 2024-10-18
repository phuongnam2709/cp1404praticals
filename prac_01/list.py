names = ["Ada", "Alan", "Bill", "John"]
print(", ".join(names))
name_to_remove = input("Who do you want to remove? ")

while name_to_remove != "":
    try:
        names.remove(name_to_remove)
    except ValueError:
        print(f"Name not in the list.")
    print(names)
    name_to_remove = input("Who do you want to remove? ")

print(f"Program ended.")

#########

things = [True, 1.2, "Good", [1, 10]]
print([len(str(t)) for t in things])