from tools import *
import datetime
output = "timeofday.csv"

times = {}
from copy import deepcopy as copy

chats = get_chat_list()
names = {}

for chat in chats:
    name = chat["name"]
    if not name in names:
        if name:
            names[name] = 0

minutes = 10
for i in range((24*60)//minutes):
    t = (datetime.datetime(2000,1,1,0,0) + ((datetime.timedelta(minutes = minutes) * i))).time()
    times[t] = copy(names)

total_per_name = copy(names)

for chat in chats:
    for message in chat["messages"]:
        if message["type"] == "message":
            dt = datetime.datetime.fromtimestamp(int(message["date_unixtime"]))
            if dt > datetime.datetime(2022,1,1):
                for t in times.keys():
                    if dt.time() < t:
                        break
                    time = t

                name = chat["name"]
                if name:
                    text = ""
                    for entiy in message["text_entities"]:
                        if entiy["type"] == "plain":
                            text += " " + entiy["text"]
                    words = len(text.split())
                    times[time][name] += words
                    total_per_name[name] += words

print(times)
print(total_per_name)

to_remove = []
for name, n in total_per_name.items():
    if n < 10000:
        to_remove.append(name)

for time, nam in times.items():
    for name in to_remove:
        nam.pop(name)

for name in to_remove:
    names.pop(name)

csv_str = "time," + ",".join(names.keys())
for time in sorted(times):
    csv_str += "\n{},".format(time)
    csv_str += ",".join(map(str,times[time].values()))

#print(csv_str)
with open(output, "w") as f:
    f.write(csv_str)

