def Invoice(service):
    cost=0
    service=service.lower()
    if(service=="-"):
        print("No service")
    elif(service=="oil change"):
        print("Oil change, $35")
        cost+=35
    elif(service=="tire rotation"):
        print("Tire rotation, $19")
        cost+=19
    elif(service=="car wash"):
        print("Car wash, $7")
        cost+=7
    elif(service=="car wax"):
        print("Car wax, $12")
        cost+=12
    return cost

total=0
print("Davy's auto shop services\nOil change -- $35")
print("Tire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n")
service1=input("Select first service:\n")
service2=input("Select second service:\n")
print("\nDavy's auto shop invoice\n")
print("Service 1: ",end="")
cost=Invoice(service1)
total+=cost
print("Service 2: ",end="")
cost=Invoice(service2)
total+=cost
print("\nTotal: $",total,sep="")