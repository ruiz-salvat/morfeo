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

    if log_type == error_log_type:
        return logger_service.get_error_logs()
    elif log_type == service_log_type:
        service_name = request.headers.get('service_name')
        return logger_service.get_service_logs(service_name)
    elif log_type == bot_instance_log_type:
        instance_id = request.headers.get('instance_id')
        process = request.headers.get('process')
        return logger_service.get_bot_instance_logs(instance_id, process)
    elif log_type == data_retriever_log_type:
        is_thread = request.headers.get('is_thread')
        is_thread_bool = False
        if is_thread == 'True' or is_thread == 'true':
            is_thread_bool = True
        elif is_thread == 'False' or is_thread == 'false':
            is_thread_bool = False
        else:
            return {'-1': 'Error in parameter: is_thread (should be \'true\' or \'false\')'}
        return logger_service.get_data_retriever_logs(is_thread_bool)
    elif log_type == other_log_type:
        return {'-1': 'Not implemented yet'}
    else:
        return {'-1': 'Error: the log type could not be identified'}
