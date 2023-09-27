from tools import *

output = "whowhen.csv"

days = {}
from copy import deepcopy as copy

chats = get_chat_list()
names = {}

for chat in chats:
    name = chat["name"]
    if not name in names:
        if name:
            names[name] = 0

total_per_name = copy(names)

for chat in chats:
    for message in chat["messages"]:
        if message["type"] == "message":
            day = message["date"][:10]
            name = chat["name"]
            if name:
                if not day in days:
                    days[day] = copy(names)

                text = ""
                for entiy in message["text_entities"]:
                    if entiy["type"] == "plain":
                        text += " " + entiy["text"]
                words = len(text.split())
                days[day][name] += words
                total_per_name[name] += words

print(days)
print(total_per_name)

to_remove = []
for name, n in total_per_name.items():
    if n < 10000:
        to_remove.append(name)

for day, nam in days.items():
    for name in to_remove:
        nam.pop(name)

for name in to_remove:
    names.pop(name)

csv_str = "day," + ",".join(names.keys())
for day in sorted(days):
    csv_str += "\n{},".format(day)
    csv_str += ",".join(map(str,days[day].values()))

#print(csv_str)
with open(output, "w") as f:
    f.write(csv_str)

