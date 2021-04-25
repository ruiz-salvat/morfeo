from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from Controllers.BotPoolController import bot_pool_controller
from Controllers.InstanceDetailsController import instance_details_controller
from Controllers.InstancesController import instances_controller
from Controllers.TradesController import trades_controller
from Database.DatabaseInitializer import DatabaseInitializer
from Net.DataRetrieverPool import DataRetrieverPool

database_initializer = DatabaseInitializer(is_test=False)
database_initializer.initialize_database()

data_retriever_pool = DataRetrieverPool(is_test=False)  # TODO: controller for data retriever?
data_retriever_pool.start_retrievers()

app = Flask(__name__)
app.register_blueprint(instance_details_controller)
app.register_blueprint(trades_controller)
app.register_blueprint(instances_controller)
app.register_blueprint(bot_pool_controller)
api = Api(app)
CORS(app)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
