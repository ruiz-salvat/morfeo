from DataObjects.Database.Patterns import Patterns
from Database.Services.Service import Service
from Util.Constants import patterns_table_name, patterns_pk, insert_patterns_db_error_msg, insert_patterns_db_msg


class PatternsService(Service):

    def __init__(self, is_test, logger_service):
        super().__init__(is_test)
        self.logger_service = logger_service

    def get_element(self):
        raise Exception('Not yet implemented')

    def insert_element(self, pattern_id, pattern_name):
        elements = self.db[patterns_table_name].find({patterns_pk: pattern_id})
        if elements.count() > 0:
            return insert_patterns_db_error_msg
        patterns = Patterns(pattern_id, pattern_name)
        self.db[patterns_table_name].insert_one(patterns.__dict__)
        return insert_patterns_db_msg

    def update_element(self):
        raise Exception('Not yet implemented')

    def delete_element(self):
        raise Exception('Not yet implemented')
