from Database.Services.PricesService import PricesService
from Database.Services.SymbolsService import SymbolsService
from Tests.Mock.TestConstants import test_symbol, test_time, test_price, test_quote, test_base
from Util.Constants import insert_prices_db_msg, prices_table_name, insert_prices_db_error_msg


def PricesService_InsertElement_Equal():
    service = PricesService(is_test=True)
    symbols_service = SymbolsService(is_test=True)
    service.db_connector.drop_database()

    symbols_service.insert_element(test_symbol, test_base, test_quote)
    msg = service.insert_element(test_symbol, test_time, test_price)

    elements = service.db[prices_table_name].find({})

    assert msg == insert_prices_db_msg, 'the returned message should be correct'
    assert elements.count() == 1, 'there should be just one element with id 1 in the collection'
    assert elements[0]['price'] == test_price, 'the price should be equal as expected'


def PricesService_InsertElement_Error():
    service = PricesService(is_test=True)
    service.db_connector.drop_database()

    msg = service.insert_element(test_symbol, test_time, test_price)

    assert msg == insert_prices_db_error_msg, 'the returned message should be correct'
