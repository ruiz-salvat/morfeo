from flask import Blueprint, request
from Logger.LoggerService import LoggerService
from Util.Constants import error_log_type, service_log_type, bot_instance_log_type, data_retriever_log_type, \
    other_log_type

logger_controller = Blueprint('LoggerController', __name__, template_folder='Logger')

logger_service = LoggerService(is_test=False)


@logger_controller.route('/get_all_logs', methods=['GET'])
def get_all_logs():
    return logger_service.get_all_logs()


@logger_controller.route('/get_filtered_logs', methods=['GET'])
def get_filtered_logs():
    log_type = request.headers.get('log_type')

    if log_type is error_log_type:
        return logger_service.get_error_logs()
    elif log_type is service_log_type:
        service_name = request.headers.get('service_name')
        return logger_service.get_service_logs(service_name)
    elif log_type is bot_instance_log_type:
        instance_id = request.headers.get('instance_id')
        process = request.headers.get('process')
        return logger_service.get_bot_instance_logs(instance_id, process)
    elif log_type is data_retriever_log_type:
        is_thread = request.headers.get('is_thread')
        return logger_service.get_data_retriever_logs(is_thread)
    elif log_type is other_log_type:
        return {'0': 'Not implemented yet'}
    else:
        return {'0': 'Error: the log type could not be identified'}
