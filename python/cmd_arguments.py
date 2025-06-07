customer = [
    {
        "uid": 1,
        "name": "Alice",
    },
    {
        "uid": 2,
        "name": "Bob",
    }

]

print(customer)
for x in customer:
    print(x["uid"], ":", x["name"])