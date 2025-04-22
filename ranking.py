def percentage(person):
    tot = sum(person["marks"])
    return tot / 4

a = [
    {"name": "raju", "age": 23, "marks": [45, 50, 40, 60]},
    {"name": "rose", "age": 12, "marks": [75, 85, 80, 90]},
    {"name": "pooja", "age": 21, "marks": [65, 70, 60, 80]},
    {"name": "lucky", "age": 24, "marks": [55, 65, 75, 70]}
]

pos = ["first", "second", "third", "fourth"]

b = sorted(a, key=percentage, reverse=True)

for i in range(len(b)):
    print(f"{b[i]['name'].capitalize()} has scored {percentage(b[i]):.2f}% and stands {pos[i]}")
