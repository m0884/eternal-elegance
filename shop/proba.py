from flask import Flask,render_template,request

app = Flask(__name__)

 
@app.route("/", methods=["post","get"])
def integer():
    messege = ""
    if request.method == "POST":
       user = request.fprm.get("user")
       password = request.form.get("password")
       messege = messege + user + " " + password
    return render_template("proba.html", messege = messege)

    сreturn render_template("proba.html",messege = "Форма готова принимать данные ")

if __name__ == "__main__":
    print("run server")
    app.run()