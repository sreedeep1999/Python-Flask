

from multiprocessing import Condition
from flask import render_template, request
import pymongo
connection=pymongo.MongoClient("mongodb://localhost:27017")
mydb=connection["empDbs"]
myemployee=mydb["employees"]

while True:
    print("  MENU  \n")
    print(" 1) Add an employee  \n")
    print(" 2)View all employee  \n")
    print(" 3)Search an employee  \n")
    print(" 4) delete an employe  \n")
    print(" 5)update an employee  \n")
    print(" 6)employee names starting with g \n ")
    print(" 7)exit \n")
    option=int(input("Select an option"))
    if option==1:
        print("  Add an option selected  ")
        empCode=input("enter an employee code")
        empName=input("enter an employee name")
        empDesignation=input("enter an employee designation")
        data={"empCode":empCode,"empName":empName,"empDesig":empDesignation}
        print(data)
        myemployee.insert_one(data)
        print("data added succefully")
        return render_template("display.html")

    elif option==2:
        print("  View all employee option selected ")
        result=myemployee.find({},{"_id":0,"empDesig":0}).sort("empName",-1)
        for i in result:
            print (i)

    elif option==3:
        print("  Search option selected ")
        empCode=input("enter employee code")
        data={"empCode":empCode}
        result=myemployee.find_one(data)
        print(result)
        
    elif option==4:
        print("Delete option selected")
        empCode=input("enter employee code to be deleted")
        data={"empCode":empCode}
        myemployee.delete_one(data)
        print("data deleted successfully")
    elif option==5:
        print("  update option selected  ")
        empCode=input("enter an employee code to be updated")
        empName=input("enter an employee name to be updated")
        empdesig=input("enter an employee designationb to be updated")
        setData={"empCode":empCode}
        newData={"$set":{"empName":empName,"empDesig":empdesig}}
        myemployee.update_one(setData,newData)
        print("data updated successfully")

    elif option==6:
        inp=input("starting name :")
        Condition={"empName":{"$gte":inp}}
        result=myemployee.find(Condition,{"_id":0}).sort("empName",-1)
        for i in result:
            print(i)

    else:
        break
