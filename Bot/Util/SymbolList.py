from Database.Services.SymbolsService import SymbolsService

symbol_list = ['ADA/USDT', 'BTC/USDT', 'DOT/USDT']


def insert_symbols_to_db(is_test):
    symbols_service = SymbolsService(is_test=is_test)
    for symbol in symbol_list:
        split_text = symbol.split('/')
        base = split_text[0]
        quote = split_text[1]
        msg = symbols_service.insert_element(symbol.replace('/', ''), base, quote)
        print(msg)
    print('All symbols were inserted to database')
