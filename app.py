from flask import Flask, render_template, jsonify    #Flask is a class inside flask and render_template is a function inside flask to access the html file, jsonify takes the data and converts it into json format

app = Flask(__name__)      #app is an object of the class Flask

JOBS =[  #JOBS is a list of dictionaries
    {
        "id" : 1,
        "title" : "Data Analyst",
        "location" : "Bengaluru, India",
        "salary" : "Rs. 10,00,000",
    },
    {
        "id" : 2,
        "title" : "Data Scinetist",
        "location" : "Delhi, India",
        "salary" : "Rs. 15,00,000",
    },
    {
        "id" : 3,
        "title" : "Web Devloper",
        "location" : "Noida, India",
        "salary" : "Rs. 20,00,000",
    }
]

#url
@app.route("/")         # @ is called decorator in py
def hello_world():
    return render_template("index.html", jobs = JOBS)  #when the url / is called, it will return this

@app.route("/api/jobs")   #we gonna take the jobs and convert it into json objects
def list_jobs():
    return jsonify(JOBS)
    
# to run the flask file
if __name__ == "__main__":
    app.run(host= "0.0.0.0" ,debug=True)