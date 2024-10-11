from flask import Flask, render_template    #Flask is a class inside flask and render_template is a function inside flask to access the html file

app = Flask(__name__)      #app is an object of the class Flask

#url
@app.route("/")         # @ is called decorator in py
def hello_world():
    return render_template("index.html")  #when the url / is called, it will return this

# to run the flask file
if __name__ == "__main__":
    app.run(host= "0.0.0.0" ,debug=True)