import time
from Database.Services.Service import Service
from Util.Constants import logs_table_name, log_limit, log_pk, error_log_type, service_log_type, bot_instance_log_type, \
    data_retriever_log_type


def parse_logs(logs):
    messages = {}
    count = 0
    for i in range(logs.count() - 1, -1, -1):
        messages[logs[i]['timestamp']] = logs[i]['message']
        count += 1
        if count > log_limit:  # maximum of 100 returned to avoid latencies
            break
    return messages


class LoggerService(Service):

    def __init__(self, is_test):
        super().__init__(is_test)

    def log_error(self, msg):
        log_model = {
            log_pk: error_log_type,
            'timestamp': time.time(),
            'message': msg
        }
        self.db[logs_table_name].insert_one(log_model)

    def log_service(self, service_name, msg):
        log_model = {
            log_pk: service_log_type,
            'timestamp': time.time(),
            'service': service_name,
            'message': msg
        }
        self.db[logs_table_name].insert_one(log_model)

    def log_bot_instance(self, instance_id, process, msg):
        log_model = {
            log_pk: bot_instance_log_type,
            'timestamp': time.time(),
            'instance_id': instance_id,
            'process': process,
            'message': msg
        }
        self.db[logs_table_name].insert_one(log_model)

    def log_data_retriever(self, is_thread, msg):
        log_model = {
            log_pk: data_retriever_log_type,
            'timestamp': time.time(),
            'is_thread': is_thread,
            'message': msg
        }
        self.db[logs_table_name].insert_one(log_model)

    def get_all_logs(self):
        logs = self.db[logs_table_name].find({})
        return parse_logs(logs)

    def get_error_logs(self):
        logs = self.db[logs_table_name].find({log_pk: error_log_type})
        return parse_logs(logs)

    def get_service_logs(self, service_name):
        logs = self.db[logs_table_name].find({
            log_pk: service_log_type,
            "service": service_name
        })
        return parse_logs(logs)

    def get_bot_instance_logs(self, instance_id, process):
        logs = self.db[logs_table_name].find({
            log_pk: bot_instance_log_type,
            "instance_id": instance_id,
            "process": process
        })
        return parse_logs(logs)

    def get_data_retriever_logs(self, is_thread):
        logs = self.db[logs_table_name].find({
            log_pk: data_retriever_log_type,
            "is_thread": is_thread
        })
        return parse_logs(logs)

    def get_other_logs(self):
        raise Exception('Not implemented yet')
