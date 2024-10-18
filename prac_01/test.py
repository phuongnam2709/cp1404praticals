from operator import itemgetter

name_to_score = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelle': 9}
name_width = max((len(name) for name in name_to_score.keys()))
score_width = max((len(str(score)) for score in name_to_score.values()))

for name, score in sorted(name_to_score.items(), key=itemgetter(1), reverse=True):
    print(f"{name:{name_width}} = {score:{score_width}}")

#############################

a = {1, 2, 3, 4}
b = {2, 4, 6}
print(a - b)
print(a ^ b)


