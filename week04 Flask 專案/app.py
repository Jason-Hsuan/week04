from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session

app=Flask(__name__, static_folder="public", static_url_path="/")
app.secret_key="jjhome"
#使用GET方法，處理路徑/的對應函式
@app.route("/", methods=["GET"])
def home_page():
    if "account" in session:
        return redirect("/member")
    else:
        return render_template("home_page.html")
#使用POST方法，處理路徑/的對應函式
@app.route("/signin", methods=["POST"])
def signin_function():
    account_data=request.form["account"]
    secret_data=request.form["secret"]
    if account_data=="test" and secret_data=="test":
        session["account"]=account_data
        return redirect("/member")
    else: 
        return redirect("/error")
#登出系統並刪去使用者後台資料
@app.route("/signout")
def delete_function():
    session.pop('account',None) 
    return redirect("/")  
#會員頁面
@app.route("/member")
def member_function():
    return render_template("member.html")  
#密碼錯誤頁面
@app.route("/error")
def fail_function():  
    return render_template("error.html")  

app.run(port=3000)