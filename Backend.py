from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250))
    due_date = db.Column(db.Date)
    status = db.Column(db.String(20), default='Incomplete')


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    # Validate and extract data from the request
    # Create a new task using the extracted data
    # Save the task to the database
    # Return the created task as a JSON response


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # Retrieve the task from the database based on the given task_id
    # Return the task as a JSON response


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    # Validate and extract data from the request
    # Retrieve the task from the database based on the given task_id
    # Update the task with the extracted data
    # Save the updated task to the database
    # Return the updated task as a JSON response


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    # Retrieve the task from the database based on the given task_id
    # Delete the task from the database
    # Return a success message as a JSON response


@app.route('/tasks', methods=['GET'])
def list_tasks():
    # Retrieve all tasks from the database
    # Return the list of tasks as a JSON response


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
