from email.policy import default
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

# @app.route("/<n1=19><name>")
# def index(n1=10, name='Sountharia'):
#     return render_template("index.html", n1=n1, name=name)

@app.route("/<admins>/")
def admin(admins):
    return render_template("index.html", n1=18, name=admins)

    # return redirect(url_for("/",n1=5,name=f"Hello Admin! {admins} "))

@app.route("/admin/")
def adm():
    return render_template("index.html", n1=18, name='Admin!')
    #return redirect(url_for("index"))
    #return redirect(url_for("/<admins>",admins="Admin!"))

if __name__=="__main__":
    app.run(debug=True)
