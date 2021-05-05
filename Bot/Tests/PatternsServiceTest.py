from Database.Services.PatternsService import PatternsService
from Logger.LoggerService import LoggerService
from Tests.Mock.TestConstants import valid_id, test_pattern_name
from Util.Constants import patterns_table_name, insert_patterns_db_msg


def PatternsService_InsertElement_Equal():
    logger_service = LoggerService(is_test=True)
    service = PatternsService(is_test=True, logger_service=logger_service)
    service.db_connector.drop_database()
    msg = service.insert_element(valid_id, test_pattern_name)

    elements = service.db[patterns_table_name].find({})

    assert msg == insert_patterns_db_msg, 'The return message should be correct'
    assert elements.count() == 1, 'there should be just one element with id 1 in the collection'
    assert elements[0]['pattern_name'] == test_pattern_name, 'the pattern name should be equal as expected'
