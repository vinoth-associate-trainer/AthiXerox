from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/sign_up")
def signup():
    return render_template('signup.html')

@app.route("/forgot_password")
def forgotpassword():
    return render_template('forgot_password.html')
    
if __name__ == '__main__':
    app.run(debug=True)