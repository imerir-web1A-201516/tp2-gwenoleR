# -*- coding: utf-8 -*-
import json
from flask import Flask, make_response, request
app = Flask(__name__)

students = [
  {"name": "John", "grades": [{"topic": "French", "mark": 12}, {"topic": "Math", "mark": 16}]},
  {"name": "Jane", "grades": [{"topic": "French", "mark": 18}, {"topic": "Math", "mark": 9}]},
  {"name": "Toto", "grades": [{"topic": "French", "mark": 8}, {"topic": "Math", "mark": 5}]}
]


@app.route("/")
def hello():
  return "Hello world!"

@app.route("/students/")
def students_list():
    name = []
    for i in range(0, len(students)):
        name.append(students[i]['name'])
    resp = make_response(json.dumps(name), 200)
    resp.headers['Content-Type'] = 'application/json'
    return  resp

@app.route("/students/<path:name>")
def grades_list(name):
    grades = []
    for i in range(0, len(students)):
        if students[i]['name'] == name:  
          grades.append(students[i]['grades'])
    resp = make_response(json.dumps(grades), 200)
    resp.headers['Content-Type'] = 'application/json'
    return  resp
    
@app.route("/students/<path:name>/average")
def student_average(name):
    for i in range(0, len(students)):
        if students[i]['name'] == name:  
          average = 0.0
          for j in range(0,len(students[i]['grades'])):
              average = average + students[i]['grades'][j]['mark']
          average = average/len(students[i]['grades'])
    resp = make_response(json.dumps(average), 200)
    resp.headers['Content-Type'] = 'application/json'
    return  resp

@app.route("/topics")
def topics_list():
    topics = []
    for i in range(0,len(students[0]['grades'])):
        topics.append(students[0]['grades'][i]['topic'])
    resp = make_response(json.dumps(topics), 200)
    resp.headers['Content-Type'] = 'application/json'
    return  resp
    
@app.route("/topics/<path:topic>/average")
def topic_average(topic):
    average = 0.0
    for i in range(0, len(students)):
        for j in range(0, len(students[i]['grades'])):
            if students[i]['grades'][j]['topic'] == topic :
                average = average + students[i]['grades'][j]['mark']
    average = average/len(students)
    resp = make_response(json.dumps(average), 200)
    resp.headers['Content-Type'] = 'application/json'
    return  resp

if __name__ == "__main__":
  app.debug=True
  app.run()
