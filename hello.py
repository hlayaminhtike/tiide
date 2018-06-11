from flask import Flask
app=Flask(_name_)
@app.route("/")
def hello():
    return "Hello Hla Yamin Htike"
@app.route("/tiide")
def tiide():
    return "Welcome to TIIDE World"
