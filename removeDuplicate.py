numbers = [2, 2, 4, 6, 4, 5, 8, 6]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)