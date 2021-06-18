import csv


def getkey(item):
    return item[1]


command_data = []
with open("command_data.csv", "r", encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",", quotechar='"')
    for row in spamreader:
        command_data.append(row)


command_counter = {}
for data in command_data:
    if data[1] in command_counter.keys():
        command_counter[data[1]] += 1
    else:
        command_counter[data[1]] = 1

# print(sorted(command_counter, key = command_counter.get, reverse = True))
print(sorted(command_counter.items(), key = lambda x : x[1], reverse = True))