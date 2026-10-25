import csv
import json

accepted_rows=[]
rejected_rows=[]

with open("orders.csv","r",newline='') as csv_file:
    reader=csv.DictReader(csv_file)
    for row in reader:
        # print(row)
        amount_text=row["amount"].strip()

        if amount_text=="":#handling empty amount
            row['reason']="Amount is empty"
            rejected_rows.append(row)
        try:
            amount=int(amount_text)
            accepted_rows.append(row)
        except ValueError:
            row["reason"]="Amount is not a number"
            rejected_rows.append(row)
            continue
        accepted_rows.append(row)
#save rejected rows into a json
with open("rejected.json","w") as rej_file:
    json.dump(rejected_rows, rej_file, indent=4)

#writing a processing summary into a text file
with open('summary.txt','w') as summary_file:
    summary_file.write(f"Total rows processed: {len(accepted_rows)+len(rejected_rows)}\n")
    summary_file.write(f"Total rows accepted: {len(accepted_rows)}\n")
    summary_file.write(f"Total rows rejected: {len(rejected_rows)}\n")  

print(f"processed rows ${accepted_rows}\n")
print(f"rejected rows ${ rejected_rows}\n")
print("Summary written to summary.txt")

