def extract_name_from_email(email):
    name_part = email.split('@')[0]
    name = name_part.replace('.', ' ').title()
    return name


def main():
    email_name_dict = {}
    continue_input = True

    while continue_input:
        email = input("Email: ")
        if email == "":
            continue_input = False

        name = extract_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").lower()

        if confirmation not in ("y", "yes", ""):
            name = input("Name: ")

        email_name_dict[email] = name

    for email, name in email_name_dict.items():
        print(f"{name} ({email})")


main()