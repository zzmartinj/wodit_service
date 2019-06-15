from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route("/")
def index():
    return 'Jeremy is the best!'

@app.route("/workouts", methods=['GET'])
def returnWorkouts():
    workouts=open('./workouts.json')
    workoutlist=json.load(workouts)    
    workouts.close()
    return json.dumps(workoutlist)

@app.route("/workouts", methods=['POST'])
def addWorkout():    
    workout=json.loads(request.args['workout'])
    workoutFile=open('./workouts.json','r')
    workoutlist=json.load(workoutFile)
    workoutFile.close()
    workoutFile=open('./workouts.json','w')
    workoutlist['workouts'].append(workout)
    workoutFile.write(json.dumps(workoutlist))
    workoutFile.close()
    return Response("Processed", status=201, mimetype='application/json')
    

