from Database.Services.SymbolsService import SymbolsService
from Logger.LoggerService import LoggerService
from Tests.Mock.TestConstants import test_symbol, test_base, test_quote
from Util.Constants import symbols_table_name, insert_symbols_db_msg


def SymbolsService_InsertElement_Equal():
    logger_service = LoggerService(is_test=True)
    service = SymbolsService(is_test=True, logger_service=logger_service)
    service.db_connector.drop_database()
    msg = service.insert_element(test_symbol, test_base, test_quote)

    elements = service.db[symbols_table_name].find({})

    assert msg == insert_symbols_db_msg, 'the returned message should be correct'
    assert elements.count() == 1, 'there should be just one element with id 1 in the collection'
    assert elements[0]['symbol'] == test_symbol, 'the symbol should be equal as expected'
