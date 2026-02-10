import csv

names = []
ages = []
countries = []
statuses = []

with open("data/users.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        names.append(row["name"])
        ages.append(int(row["age"]))
        countries.append(row["country"])
        statuses.append(row["status"])

print("Total users:", len(names))
print("Average age:", sum(ages) / len(ages))
