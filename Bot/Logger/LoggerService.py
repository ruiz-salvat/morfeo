import time
from Database.Services.Service import Service
from Util.Constants import logs_table_name, log_limit


class LoggerService(Service):

    def __init__(self, is_test):
        super().__init__(is_test)

    def log_error(self, msg):
        log_model = {
            'type': 'error',
            'timestamp': time.time(),
            'message': msg
        }
        self.db[logs_table_name].insert_one(log_model)

    def log_service(self, service, msg):
        log_model = {
            'type': 'service',
            'timestamp': time.time(),
            'service': service,
            'message': msg
        }
        self.db[logs_table_name].insert_one(log_model)

    def log_bot_instance(self, instance_id, process, msg):
        log_model = {
            'type': 'bot_instance',
            'timestamp': time.time(),
            'instance_id': instance_id,
            'process': process,
            'message': msg
        }
        self.db[logs_table_name].insert_one(log_model)

    def log_data_retriever(self, is_thread, msg):
        log_model = {
            'type': 'data_retriever',
            'timestamp': time.time(),
            'is_thread': is_thread,
            'message': msg
        }
        self.db[logs_table_name].insert_one(log_model)

    def get_all_logs(self):
        logs = self.db[logs_table_name].find({})
        messages = {}
        count = 0
        x = logs.count()
        for i in range(logs.count()-1, -1, -1):
            messages[count] = logs[i]['message']
            count += 1
            if count > log_limit:
                break
        return messages
