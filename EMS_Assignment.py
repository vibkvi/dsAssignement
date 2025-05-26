def printheader(id="Id", name="Name", age="Age", dept="Department", sal="Salary"):
    print("%10s\t%20s\t%4s\t%20s\t%9s" %(id,name,age,dept,sal))

def printemp(id, emp):
    printheader(id, emp.get("name"), emp.get("age"), emp.get("dept"), emp.get("sal"))

def printall(emplist):
    if emplist.keys().__len__() == 0 :
        print("No employees available.")
    else:
        printheader()
        for empid in emplist.keys():
            printemp(empid, emplist.get(empid))

def printselectedemp(emplist) :
    key = int(input("Employee Id: "))
    printheader()
    if key in emplist.keys():
        printemp(key, emplist.get(key))
    else:
        print("Employee not found.")

def createemployee(name, age, dept, salary):
    emp =  {'name': name, 'age': age, 'dept': dept, 'sal': salary}
    return emp

def getemployee(emplist):
    print("Enter employee details")
    empid = int(input("Number: "))
    while(empid in emplist.keys()):
        print("Employee id ", empid, " already exists. Please enter a new id")
        empid = int(input())

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
emps = dict()
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