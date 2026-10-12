# Python for Data Engineering --- Learning Notes

These notes cover the Python concepts practised so far. They are written
as a reference for revision and GitHub.

## 1. Dictionaries and nested data

A Python dictionary stores values using **keys**.

``` python
employee = {
    "id": 101,
    "name": "Monica",
    "skills": ["Python", "SQL", "Snowflake"],
    "experience": {
        "company": "Cognizant",
        "years": 1
    }
}
```

Access a value with square brackets:

``` python
print(employee["name"])                    # Monica
print(employee["skills"][1])               # SQL
print(employee["experience"]["company"])   # Cognizant
print(employee["experience"]["years"])     # 1
```

### Nested access

Follow the structure one level at a time:

``` python
dictionary["outer_key"]["inner_key"]
```

For a list inside a dictionary, use the list index too:

``` python
employee["skills"][2]  # Snowflake
```

**Remember:** dictionary keys use `["key"]`; don't use Java-style dot
access such as `employee.name`.

## 2. Lists containing dictionaries

API and application data often contains a list of records, where each
record is a dictionary.

``` python
orders = [
    {"id": 101, "customer": "Ravi", "amount": 500},
    {"id": 102, "customer": "Priya", "amount": 750},
    {"id": 103, "customer": "Arun", "amount": 300}
]
```

Get the second order's customer:

``` python
print(orders[1]["customer"])  # Priya
```

Python list indexes start at `0`, so index `1` is the second item.

### Loop through records

A direct loop is usually clearer than using `range(len(...))` when you
don't need the index.

``` python
for order in orders:
    print(order["amount"])
```

Output:

``` text
500
750
300
```

### Calculate a total

``` python
total = 0

for order in orders:
    total += order["amount"]

print(total)  # 1550
```

Python is case-sensitive: `total` and `Total` are different names.

## 3. JSON and Python objects

JSON is a common format for data exchanged by APIs. JSON objects look
similar to Python dictionaries, but JSON text is not automatically a
Python dictionary.

\`\`\`python import json

json_data =
