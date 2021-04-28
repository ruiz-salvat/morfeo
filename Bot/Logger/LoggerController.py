from flask import Blueprint
from Logger.LoggerService import LoggerService

logger_controller = Blueprint('LoggerController', __name__, template_folder='Logger')

logger_service = LoggerService(is_test=False)


@logger_controller.route('/get_all_logs', methods=['GET'])
def get_all_logs():
    return logger_service.get_all_logs()
