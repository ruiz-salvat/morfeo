from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from Controllers.BotInstanceController import bot_instance_controller
from Controllers.InstanceDetailsController import instance_details_controller
from Controllers.TradesController import trades_controller
from Database.DatabaseInitializer import DatabaseInitializer


database_initializer = DatabaseInitializer(is_test=False)
database_initializer.initialize_database()

app = Flask(__name__)
app.register_blueprint(instance_details_controller)
app.register_blueprint(trades_controller)
app.register_blueprint(bot_instance_controller)
api = Api(app)
CORS(app)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
