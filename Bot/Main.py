from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from Controllers.InstanceStatesController import instance_states_controller
from Database.DatabaseInitializer import DatabaseInitializer


database_initializer = DatabaseInitializer(is_test=False)
database_initializer.initialize_database()

app = Flask(__name__)
app.register_blueprint(instance_states_controller)
api = Api(app)
CORS(app)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
