from DataObjects.Status import Status
from Database.Services.StatusService import StatusService
from Logger.LoggerService import LoggerService
from Util.Constants import status_table_name, insert_status_db_msg


def StatusService_InsertElement_Equal():
    logger_service = LoggerService(is_test=True)
    service = StatusService(is_test=True)
    service.db_connector.drop_database()
    msg = service.insert_element(Status.RUNNING)

    elements = service.db[status_table_name].find({})

    assert msg == insert_status_db_msg, 'the return message should be correct'
    assert elements.count() == 1, 'there should be just one element with id 1 in the collection'
    assert elements[0]['status_name'] == Status.RUNNING.name, 'the status name should be equal as the expected one'
