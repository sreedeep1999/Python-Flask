from flask import Flask,render_template,request
import pymongo
connection=pymongo.MongoClient("mongodb://localhost:27017")
mydb=connection["empDbs"]
myemployee=mydb["employees"]

app = Flask(__name__)

@app.route("/read",methods=["POST"])
def hello():
    if(request.method=="POST"):
        empCode=request.form.get("ecode")
        empName=request.form.get("ename")
        empDesignation=request.form.get("edesig")
        data={"empCode":empCode,"empName":empName,"empDesig":empDesignation}
        print(data)
        myemployee.insert_one(data)
        return render_template("display.html")
        

@app.route("/view")
def view():
    result=myemployee.find({},{"_id":0}).sort("empName",-1)
    datalist=[]
    for i in result:
        datalist.append(i)
        
    
    return render_template("display.html",data=datalist)

@app.route("/")
def hello_world():
    return render_template("index.html")
app.run()
