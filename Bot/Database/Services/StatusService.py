from Database.Services.Service import Service
from Util.Constants import status_table_name, status_pk, insert_status_db_error_msg, insert_status_db_msg


class StatusService(Service):

    def __init__(self, is_test):
        super().__init__(is_test)

    def insert_element(self, status):
        elements = self.db[status_table_name].find({status_pk: status.value})
        if elements.count() > 0:
            return insert_status_db_error_msg
        status_dict = {'status_id': status.value,
                       'status_name': status.name}
        self.db[status_table_name].insert_one(status_dict)
        return insert_status_db_msg
