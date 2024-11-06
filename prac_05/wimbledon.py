def read_champions(filename):
    champions = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                name = parts[0].strip()
                country = parts[1].strip()
                champions.append((name, country))
    return champions


def count_champions(champions):
    champion_count = {}
    for name, country in champions:
        if name in champion_count:
            champion_count[name] += 1
        else:
            champion_count[name] = 1
    return champion_count


def get_unique_countries(champions):
    countries = {country for _, country in champions}
    return countries


def display_results(champion_count, countries):
    print("Wimbledon Champions:")
    for champion, count in sorted(champion_count.items()):
        print(f"{champion} {count}")

    sorted_countries = sorted(countries)
    print("\nThese {} countries have won Wimbledon:".format(len(sorted_countries)))
    print(", ".join(sorted_countries))


def main():
    filename = "wimbledon.csv"
    champions = read_champions(filename)
    champion_count = count_champions(champions)
    countries = get_unique_countries(champions)
    display_results(champion_count, countries)


main()
