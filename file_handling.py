"""file = open("orders.txt", "r")
data=file.read()
print(data)
line=file.readline()
print(line)#here we won't gte anything bcs read read() method reads all the lines present in file, so here nothing left

print(file.readlines())

file.close()"""
#so let's open the file again
"""print("Re opening the file again")
file=open("orders.txt", "r")
print(file.readline())
print(file.readlines())#return the left over lines in the file in the form of list
print(file.read())#nothing left so give empty
print("Resetting the file pointer using seek()")
file.seek(0)
print(file.read())

print("Using with open()")"""
#it avoids error even though if we won't close the file at the end
"""with open("orders.txt", "r") as file:
    data=file.read()
    print(data)
"""
#writing contents to file
"""print()
print("writing to file")
with open("outputs.txt","w") as file:
    file.write("Snowflake\n")
    file.write("Python\n")
    file.write("Data Engineering\n")
"""
"""customer1="pandu"
with open("customers.txt","w") as file:
    # file.write("custoemer = \"Mounika \"")#it is not variable assignment
    file.write("Customer1: "+customer1+"\n")
    file.write(f"Customer1: {customer1}")
"""
"""customer="Mounika"
amount=750
with open("orders2.txt","w") as file:
    file.write(f"customer: {customer}\n")
    file.write(f"amount: {amount}\n")
"""
#appending where w hover writes existing content, but append can add the contents to the existing data
customer2 = "Priya"
amount = 800
with open("orders2.txt","a") as file:
    file.write(f"customer2: {customer2}\t amount:{amount}\n")
