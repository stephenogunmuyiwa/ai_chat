from flask import Flask, render_template,request,redirect,jsonify
from gemini_stuffs import get_gemini_response

orange = Flask(__name__)

@orange.route("/")
def home():
    return render_template("sign_in.html")

@orange.route("/submit",methods =["POST"])
def submit():
    userName = request.form.get("username")
    password = request.form.get("password")
    validUsernames = ["stephen","bola","femi"]
    superPasscode = "123456SUPER"
    if (userName.lower() in validUsernames and password == superPasscode):
        return redirect("/chat")
    else:
        return redirect("/")
    
@orange.route("/chat")
def chat():
    return render_template("chat.html")

@orange.route("/response", methods=["POST"])
def AIresponse():
    userInput = request.json.get("message")
    final_response = get_gemini_response(userInput)
    return jsonify({"response": final_response})

if __name__ == "__main__":
    orange.run(host="0.0.0.0", port=8080,debug=True)