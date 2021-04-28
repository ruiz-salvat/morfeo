from Database.Services.SymbolsService import SymbolsService
from Util.Constants import symbols_service_name

symbol_list = ['ADA/USDT', 'BTC/USDT', 'DOT/USDT']


def insert_symbols_to_db(is_test, logger_service):
    symbols_service = SymbolsService(is_test=is_test, logger_service=logger_service)
    for symbol in symbol_list:
        split_text = symbol.split('/')
        base = split_text[0]
        quote = split_text[1]
        msg = symbols_service.insert_element(symbol.replace('/', ''), base, quote)
        logger_service.log_service(symbols_service_name, msg + ' - (' + symbol + ')')
