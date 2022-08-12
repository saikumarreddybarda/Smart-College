import pickle

from flask import Flask, redirect, url_for, render_template, request, jsonify,make_response

from SmartCollegeApp import service

from SmartCollegeApp.database import WorkspaceData

from SmartCollegeApp.chatbot2 import finalbot, sent_tokens

import nltk

nltk.warnings.filterwarnings('ignore')
nltk.download('punkt')  # sentence tokenizer funtions
nltk.download('wordnet')

app = Flask(__name__)
db = WorkspaceData()


#db = WorkspaceData()
#db.add('login', [('1602-19-737-089', '123')])
@app.route('/', methods=['GET'])
def welcome():
   return render_template("home.html")

@app.route('/Slogin', methods=['POST','GET'])
def Slogin():
         return  render_template("LoginS.html")
@app.route('/Tlogin', methods=['POST','GET'])
def Tlogin():
         return  render_template("LoginT.html")
@app.route('/VloginS', methods=['POST','GET'])
def VloginS():
    if request.method == 'POST':
            user_name = request.form.get('username')
            password = request.form.get('password')
            print(user_name)
            db = WorkspaceData()

            data = db.get('login', user_name)
            for s in data:
                    if user_name == s['username'] and password == s['password']:
                        return render_template("Student.html")
                    else:
                        a="Entered password is incorrect! please check"
                        return render_template("LoginS.html",incorrect=a)

@app.route('/VloginT', methods=['POST','GET'])
def VloginT():
    if request.method == 'POST':
            user_name = request.form.get('username')
            password = request.form.get('password')
            db = WorkspaceData()
            data = db.get('signup', user_name)
            print(data)
            for s in data:
                if user_name == s['username'] and password == s['password']:
                    return render_template("faculty.html")
                else:
                    a = "Entered password is incorrect! please check"
                    return render_template("LoginT.html", incorrect=a)

@app.route('/signup', methods=['POST','GET'])
def signup():
        return render_template("Sign-Up.html")


@app.route('/faculty', methods=['GET','POST'])
def faculty():
     if request.method == "POST":
       name = request.form.get('name')
       department = request.form.get('number')
       phoneno = request.form.get('number-1')
       address= request.form.get('text')
       password = request.form.get('text-1')
       securityno = request.form.get('number-2')
       #print("name is ", name)
       db = WorkspaceData()
       db.add('signup', [(name, department,phoneno,address,password,securityno)])
       return render_template('faculty.html', retry=True, errorType='registration')


@app.route('/placements', methods=['POST','GET'])
def placements():
        return render_template("placements.html")

@app.route('/placepred', methods=['POST','GET'])
def placepred():
   # if request.method == "POST":
        age= request.form.get('number')
        print(age)
        intern = request.form.get('number-1')
        print(intern)
        cgpa= request.form.get('number-2')
        print(cgpa)
        backlog = request.form.get('number-3')
        print(backlog)
        datas  = request.form.get('number-5')
        print(datas)
        aptitude= request.form.get('number-4')
        print(aptitude)
       # branch=request.form.get('select')
        #gender= request.form.get('text')

      #  if(gender== 'male'):
         #print(age,branch,gender)
        loaded_model = pickle.load(open("placements.pickle", 'rb'))
        res=loaded_model.predict([[age, intern, cgpa,backlog,aptitude,datas,0,1]])
        print(res)
        file1 = open("modRes.txt", "w")

        result=res[0]
        print(result)
        file1.write(str(result))
        file1.close()
        if res==[1]:
                   return render_template("placepredsucc.html")
        else:
                   return render_template("placepredfail.html")

@app.route('/placesuc', methods=['GET','POST'])
def placepredsucc():
    file1 = open("modRes.txt", "r")
    temp = file1.read()
    print(temp)
    file1.close()
    if temp=='1':
        return render_template("placepredsucc.html")
    else:
        return render_template("placepredfail.html")


@app.route('/camera', methods=['GET','POST'])
def cameraa():
    return render_template("camera.html")

@app.route('/capture_img', methods=['POST','GET'])
def capture_img():
    msg = service.save_img(request.form["img"])
    print(msg)
    return make_response(msg)

@app.route('/success', methods=['GET','POST'])
def success():
    print("hello")
    file1 = open("namefile.txt", "r")
    temp=file1.read()
    print(temp)
    file1.close()
    return render_template("success.html",name=temp)
@app.route('/teacherScd', methods=['GET','POST'])
def teacherscd():
    return render_template("TeacherScd.html")

#chatbot
@app.route('/chatbot', methods=['GET'])
def chatbot():
    return render_template("base.html")


@app.route('/predict', methods=['POST'])
def predict():
    text = request.get_json().get("message")
    response = finalbot(text)
    message = {"answer": response}

    if text in sent_tokens:
        sent_tokens.remove(text)

    return jsonify(message)


if __name__ == '__main__':
   app.run(debug=True)

