from flask import Flask, redirect, url_for, render_template, request, jsonify,make_response

from SmartCollegeApp.chatbot2 import finalbot,sent_tokens
app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
   return render_template("base.html")
@app.route('/predict', methods=['POST'])
def predict():
   text=request.get_json().get("message")
   response=finalbot(text)
   message={"answer":response}

   if text in sent_tokens:

      sent_tokens.remove(text)
 
   return  jsonify(message)

if __name__ == '__main__':
   app.run(debug=True)
#{{url_for('static',filename='style.css')}}
#static/app.js
