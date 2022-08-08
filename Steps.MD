# Steps
### Create a folder for your project  
### Create 3 files  
1. index.html
2. style.css
3. app.py

### Install necessary Packages
In python terminal create a **virtual enviroment** (install if you do not have virtualenv (pip install virtualenv))
1. py -3 -m venv venv
2. venv/Scripts/activate - to activate the virtual environment Set-ExecutionPolicy Unrestricted -Scope Process)
      (if you get error cannot be loaded because running scripts is disabled on this system, use the following command in Terminal)
      (before that check Get-ExecutionPolicy -List to check the policy is Undefined for all)
       Set-ExecutionPolicy Unrestricted -Scope Process
3. pip install flask
4. pip install flask-sqlalchemy
5. pip freeze > requirement.txt (will create a file requirements with details of all the installed packages)

### In app.py  
. import Flask, render_template from flask module and import SQLAlchemy from flask_sqlalchemy  
. initialize the app => app = Flask(__ name __ )  
. create the decorated ( the home page route) => @app.route("/")  
1. create a function to handle the home page, return the html page
. if name is main run app with debug set to True => if __ name __ == "__ main __ ": app.run(debug=True)

### In index.html
. create the html boiler plate  
. change the title  
. add a header 1 with Hello as message => < h1>Hello</h1 >   

### Run the program  
. click the link 127.0.0.1:5000 or localhost:5000  
