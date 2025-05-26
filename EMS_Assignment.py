def printall(emplist):
    for empid in emplist.keys():
        printemp(empid, emplist.get(empid))

def printemp(empid, emp):
    print("------------------------------------")
    print("Id: ", empid)
    for key in emp.keys():
        print(key, ": ", emp.get(key))

def printselectedemp(emplist) :
    key = int(input("Employee Id: "))
    if key in emplist.keys():
        printemp(key, emplist.get(key))
    else:
        print("There is no employee with id", key)

def createemployee(name, age, dept, salary):
    emp =  {'name': name, 'age': age, 'department': dept, 'salary': salary}
    return emp

def getemployee(emplist):
    print("Enter employee details")
    empid = int(input("Number: "))
    name = input("Name: ")
    age = int(input("Age: "))
    dept = input("Department: ")
    salary = int(input("Salary: "))
    emplist[empid] = createemployee(name, age, dept, salary)

def getchoice():
    print("--------------------------")
    print("1: Add Employee: ")
    print("2: View All Employee")
    print("3: Search for Employee")
    print("4: Exit")
    ch = int(input("Enter your choice "))
    return ch

choice = 0
emps = {101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}}
while choice < 4 :
    choice = getchoice()
    match choice :
        case 1 :
            getemployee(emps)
        case 2 :
            printall(emps)
        case 3 :
            printselectedemp(emps)
        case 4 :
            print("thank you")
            exit()