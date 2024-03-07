def get_lowest_score_names(get_data, lowest_value):
    names = []
    for sublist in get_data:
        if sublist[1] == lowest_value:
            names.append(sublist[0])
    return '\n'.join(sorted(names))


data = []
for i in range(int(input())):

    name = input()
    score = float(input())

    data.append([name, score])


second_min_value = sorted(set([sl[1] for sl in data]))[1]
names_with_lowest_value = get_lowest_score_names(data, second_min_value)
print(names_with_lowest_value) 