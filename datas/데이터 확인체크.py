
datas = []

with open("2022-07-26-data-log", "r", encoding="utf-8") as f:
    v = f.read().split("\n")
    for k in v:
        datas.append(k.split(","))

print(len(datas))
print(datas[:2])


