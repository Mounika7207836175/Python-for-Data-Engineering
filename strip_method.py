print(("    data engineering####").strip())
print(("    data engineering####").strip("#"))
#Task: read the file line by line and print only the order records where the amount is greater than 500.
with open("orders.txt","r") as file:
    # line=file.readline().strip(",")
    # print(line)
    #When you call split(), Python searches through your string,
    # and cuts it wherever it finds your specified separator, and returns a Python List [...] containing the pieces.
    for line in file:
        # values=line.split(",")
        # one improvement, use strip() to remove new line characters here
        values=line.strip().split(",")
        if(int(values[2])>500):
            print(values)


