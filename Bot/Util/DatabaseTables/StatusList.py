from DataObjects.Status import Status
from Database.Services.StatusService import StatusService
from Util.Constants import status_service_name

status_list = [Status.NOT_STARTED, Status.INITIALIZING, Status.RUNNING, Status.FAILED, Status.STOPPED]


def insert_status_to_db(is_test, logger_service):
    status_service = StatusService(is_test)
    for status in status_list:
        msg = status_service.insert_element(status)
        logger_service.log_service(status_service_name, msg + ' - (' + status.name + ')')
