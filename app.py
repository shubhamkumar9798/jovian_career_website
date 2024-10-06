from flask import Flask    #Flask is a class inside flask 

app = Flask(__name__)      #app is an object of the class Flask

#url
@app.route("/")         # @ is called decorator in py
def hello_world():
    return "<p>Hello, World!</p>"  #when the url / is called, it will return this

# to run the flask file
if __name__ == "__main__":
    app.run(host= "0.0.0.0" ,debug=True)