# Python for Data Engineering — Part 3

A beginner-friendly guide to reading CSV data, validating it, saving rejected rows, and writing useful outputs.

## What you will build

A small transaction processor that reads `transactions.csv`, keeps valid rows, records rejected rows in `rejected.json`, and writes a text summary to `summary.txt`.

## 1. Read CSV rows as dictionaries

A CSV file stores values as text in rows and columns. `csv.DictReader` uses the header row as keys, so each row behaves like a dictionary.

```python
import csv

with open("transactions.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
```

For a file such as:

```csv
transaction_id,customer,amount
T001,Ana,25.50
```

`row` looks like `{"transaction_id": "T001", "customer": "Ana", "amount": "25.50"}`. CSV values are strings, even when they look like numbers.

Use `newline=""` when opening CSV files. It lets Python's CSV module handle line endings correctly, including on Windows, and helps avoid extra blank lines in some situations.

## 2. Add useful keys to a row

A dictionary row can be extended like any other dictionary:

```python
row["amount"] = float(row["amount"])
row["source"] = "transactions.csv"
```

Do this only after checking and converting the original value. In the project below, the amount is converted to a number and saved in a separate `amount_value` key; the original CSV text remains available for rejected-row details.

## 3. Validate input safely

For each row, check that required fields exist and are not blank. Then convert the amount with `float()`. A blank or non-numeric amount causes `ValueError`, which you can catch. A numeric amount below zero is also invalid, even though conversion succeeded.

```python
amount_text = row.get("amount", "").strip()
if not amount_text:
    reason = "missing amount"
else:
    try:
        amount = float(amount_text)
    except ValueError:
        reason = "amount is not numeric"
    else:
        if amount < 0:
            reason = "amount cannot be negative"
        else:
            row["amount_value"] = amount
```

Use `.get()` so a missing column returns a default instead of causing a `KeyError`. Use `.strip()` to treat spaces-only values as blank.

## 4. Handle a bad row and continue

Put risky work inside `try`, and catch the specific error you expect. `continue` skips the rest of the current loop iteration and moves to the next row. It does not stop the whole program.

```python
try:
    amount = float(row["amount"])
except (KeyError, ValueError):
    rejected.append({"row": row, "reason": "missing or non-numeric amount"})
    continue
```

For validation with several possible reasons, it is often clearer to set a `reason` and then decide whether to reject the row, as in the complete example below. Avoid a broad bare `except:` because it can hide programming mistakes.

## 5. Save rejected rows as JSON

JSON is a convenient format for structured data such as a list of rejected rows. `json.dump()` writes a Python object to an open file. `indent=2` makes the file readable; `ensure_ascii=False` preserves ordinary non-English text.

```python
import json

with open("rejected.json", "w", encoding="utf-8") as file:
    json.dump(rejected, file, indent=2, ensure_ascii=False)
```

## 6. Read JSON with `json.load`

Use `json.load()` to read JSON from a file and turn it back into Python values. A JSON array becomes a Python list, and JSON objects become dictionaries.

```python
with open("rejected.json", "r", encoding="utf-8") as file:
    saved_rejections = json.load(file)

print(f"Rejected rows saved: {len(saved_rejections)}")
```

The JSON file must already exist and contain valid JSON. In the mini-project, it is written before it is read.

## 7. Write a text file

Use `open(..., "w")` to create or replace a text file. `\n` starts a new line. The `with` block closes the file automatically.

```python
with open("summary.txt", "w", encoding="utf-8") as file:
    file.write("Processing complete\n")
```

## 8. Mini-project: process transactions end to end

Create a folder and put these two files in it. The sample CSV includes valid rows and examples of missing, non-numeric, and negative amounts.

**transactions.csv**

```csv
transaction_id,customer,amount
T001,Ana,25.50
T002,Bo,
T003,Cam,unknown
T004,Dee,-4
T005,Eli,12
```

**process_transactions.py**

```python
import csv
import json

valid_rows = []
rejected_rows = []

with open("transactions.csv", "r", newline="", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        transaction_id = row.get("transaction_id", "").strip()
        customer = row.get("customer", "").strip()
        amount_text = row.get("amount", "").strip()

        # Check required text fields first.
        if not transaction_id:
            rejected_rows.append({"row": row, "reason": "missing transaction_id"})
            continue
        if not customer:
            rejected_rows.append({"row": row, "reason": "missing customer"})
            continue
        if not amount_text:
            rejected_rows.append({"row": row, "reason": "missing amount"})
            continue

        # A bad numeric value rejects this row, but processing continues.
        try:
            amount = float(amount_text)
        except ValueError:
            rejected_rows.append({"row": row, "reason": "amount is not numeric"})
            continue

        if amount < 0:
            rejected_rows.append({"row": row, "reason": "amount cannot be negative"})
            continue

        # Add a numeric value for later calculations; keep original CSV fields too.
        row["amount_value"] = amount
        valid_rows.append(row)

with open("rejected.json", "w", encoding="utf-8") as json_file:
    json.dump(rejected_rows, json_file, indent=2, ensure_ascii=False)

# Read the saved JSON back to demonstrate json.load().
with open("rejected.json", "r", encoding="utf-8") as json_file:
    saved_rejections = json.load(json_file)

valid_total = sum(row["amount_value"] for row in valid_rows)

with open("summary.txt", "w", encoding="utf-8") as text_file:
    text_file.write("Transaction processing summary\n")
    text_file.write(f"Valid rows: {len(valid_rows)}\n")
    text_file.write(f"Rejected rows: {len(saved_rejections)}\n")
    text_file.write(f"Total valid amount: {valid_total:.2f}\n")

print("Done. See summary.txt and rejected.json.")
```

Run the script from the folder containing both files:

```text
python process_transactions.py
```

With the sample data, there are **2 valid rows**, **3 rejected rows**, and a total valid amount of **37.50**. `rejected.json` records each original row and its reason; `summary.txt` contains the counts and total.

## Key ideas to remember

- `csv.DictReader` maps each CSV row to a dictionary using the header names.
- CSV fields start as strings; convert and validate before doing calculations.
- `newline=""` is the recommended CSV file-opening pattern.
- `try`/`except` handles expected conversion errors; `continue` moves on after a rejected row.
- `json.dump()` saves Python data as JSON; `json.load()` reads it back.
- `with open(...)` closes files reliably, and text output uses `\n` for line breaks.
