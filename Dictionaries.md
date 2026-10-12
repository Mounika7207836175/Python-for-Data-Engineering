# Python for Data Engineering — Learning Notes

These notes cover the Python concepts practised so far. They are designed for revision and GitHub.

## 1. Dictionaries and nested data

A dictionary stores values using keys.

```python
employee = {
    "id": 101,
    "name": "Monica",
    "skills": ["Python", "SQL", "Snowflake"],
    "experience": {"company": "Cognizant", "years": 1}
}

print(employee["name"])                    # Monica
print(employee["skills"][1])               # SQL
print(employee["experience"]["company"])   # Cognizant
print(employee["experience"]["years"])     # 1
```

Use `dictionary["key"]`, not `dictionary.key`. For nested dictionaries, keep following the keys. For a list inside a dictionary, use an index such as `employee["skills"][2]` for `Snowflake`.

## 2. Lists containing dictionaries

```python
orders = [
    {"id": 101, "customer": "Ravi", "amount": 500},
    {"id": 102, "customer": "Priya", "amount": 750},
    {"id": 103, "customer": "Arun", "amount": 300}
]

print(orders[1]["customer"])  # Priya
```

List indexes start at `0`, so index `1` means the second item.

Loop through each order:

```python
for order in orders:
    print(order["amount"])
```

Calculate a total:

```python
total = 0
for order in orders:
    total += order["amount"]
print(total)  # 1550
```

Python is case-sensitive: `total` and `Total` are different names.

## 3. JSON and Python objects

JSON is commonly used to exchange data through APIs. JSON text resembles a Python dictionary, but it is not automatically a Python dictionary.

```python
import json

json_data = '''
{
    "employee": "Monica",
    "skills": ["Python", "SQL", "Snowflake"]
}
'''

data = json.loads(json_data)
print(data["employee"])   # Monica
print(data["skills"][2])  # Snowflake
```

- `json.loads(json_text)`: JSON string → Python object.
- `json.dumps(python_object)`: Python object → JSON-formatted string.

## 4. Opening and reading files

Suppose `orders.txt` contains:

```text
101,Ravi,500
102,Priya,750
103,Arun,300
```

Open and read the entire file:

```python
file = open("orders.txt", "r")
data = file.read()
print(data)
file.close()
```

### File modes

| Mode | Purpose |
|---|---|
| `"r"` | Read an existing file |
| `"w"` | Write; creates a file or overwrites existing contents |
| `"a"` | Append to the end; creates the file if needed |
| `"r+"` | Read and write without automatically truncating existing contents |

Be careful: `"w"` clears an existing file's contents when opened.

### Reading methods and file position

| Method | Purpose |
|---|---|
| `file.read()` | Reads all remaining content as one string |
| `file.readline()` | Reads the next line |
| `file.readlines()` | Reads all remaining lines into a list |
| `file.seek(0)` | Moves the file position to the beginning |

```python
file = open("orders.txt", "r")
print(file.readline())  # First line
print(file.readline())  # Second line
file.close()
```

A file has a current reading position. After `file.read()` reaches the end, further reads return no more content until you move the position. `file.seek(0)` resets it to the beginning.

## 5. Prefer `with open(...)`

`with open(...)` automatically closes the file when its indented block ends, even if an exception occurs inside the block.

```python
with open("orders.txt", "r") as file:
    data = file.read()
    print(data)
```

You don't need `file.close()` manually with this pattern. This doesn't prevent all errors: opening a missing file in read mode can still raise `FileNotFoundError`.

## 6. Writing text to a file

```python
customer = "Monica"
amount = 750

with open("customer.txt", "w") as file:
    file.write(f"Customer name: {customer}\n")
    file.write(f"Amount: {amount}\n")
```

File contents:

```text
Customer name: Monica
Amount: 750
```

An f-string inserts variable values into text: `f"Customer: {customer}"`. By contrast, `"customer"` is literal text. `\n` starts a new line, and `\t` inserts a tab.

## 7. Append instead of overwriting

Use `"a"` to keep existing content and add more:

```python
customer = "Priya"
amount = 800

with open("orders2.txt", "a") as file:
    file.write(f"Customer: {customer}\n")
    file.write(f"Amount: {amount}\n")
```

Use `"w"` to replace file contents and `"a"` to append.

## 8. Process a file one line at a time

For a large file, iterating over the file can use less memory than loading all content into one large string.

```python
with open("orders.txt", "r") as file:
    for line in file:
        print(line.strip())
```

`for line in file` reads one line at a time. `strip()` removes whitespace at both ends, including the newline at the end of a line.

## 9. Split a simple record into fields

For this line:

```text
102,Priya,750
```

```python
line = "102,Priya,750"
values = line.split(",")

print(values)     # ['102', 'Priya', '750']
print(values[0])  # '102' — order ID
print(values[1])  # 'Priya' — customer
print(values[2])  # '750' — amount
```

`split(",")` returns a list of strings. Convert the amount to an integer before numeric comparison:

```python
amount = int(values[2])
if amount > 500:
    print("Amount is greater than 500")
```

Comparing a string directly with an integer using `>` raises a `TypeError` in Python 3.

### Filter records by amount

Given `orders.txt`:

```text
101,Ravi,500
102,Priya,750
103,Arun,300
```

```python
with open("orders.txt", "r") as file:
    for line in file:
        values = line.strip().split(",")
        amount = int(values[2])

        if amount > 500:
            print(line.strip())
```

Output:

```text
102,Priya,750
```

- `strip()` removes the trailing newline.
- `split(",")` separates fields.
- `int()` converts the amount to a number.
- `if amount > 500` filters the records.

**Limitation:** `split(",")` is suitable for simple comma-separated rows. It can fail when a quoted field contains a comma, such as `"Priya, Sharma"`. Python's `csv` module handles proper CSV formatting; that is the next topic.

## 10. Common mistakes

1. Use `print()`, not `Print()`.
2. Access dictionary values with `employee["name"]`, not `employee.name`.
3. After `data = file.read()`, `data` is a string. Call `file.readline()` on the file object, not `data`.
4. Reading methods use the current file position. Use `seek(0)` to return to the beginning.
5. Values returned by `split()` are strings; use `int()` for numeric comparisons.
6. `"w"` overwrites existing file contents.
7. The file must be in the working directory (or use the correct path) when opening it with `"r"`.

## 11. Practice exercises

1. Print the company and years from a nested `experience` dictionary.
2. Loop through a list of order dictionaries and calculate the total amount.
3. Convert JSON text with `json.loads()` and print a nested value.
4. Read only the first line of a text file.
5. Write a customer's name and order amount to a file using an f-string.
6. Append another order without removing existing contents.
7. Read a text file line by line and print only records where the amount is greater than 500.

## Progress checklist

- [x] Nested dictionaries and lists
- [x] Lists of dictionaries and loops
- [x] JSON conversion with `json`
- [x] Reading files and understanding file position
- [x] `with open(...)` and automatic closing
- [x] Writing and appending text files
- [x] Processing simple comma-separated records with `split()`
- [ ] Python `csv` module — next topic
