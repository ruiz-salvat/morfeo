from Database.Services.PricesService import PricesService
from Database.Services.SymbolsService import SymbolsService
from Logger.LoggerService import LoggerService
from Net.DataRetriever import DataRetriever


def DataRetrieverIntegrationTest():
    is_test = True
    logger_service = LoggerService(is_test=is_test)
    prices_service = PricesService(is_test=is_test)
    symbols_service = SymbolsService(is_test=is_test, logger_service=logger_service)
    prices_service.db_connector.drop_database()
    symbol = 'ADA/USDT'
    symbols_service.insert_element(symbol.replace('/', ''), 'ADA', 'USDT')
    data_retriever = DataRetriever(symbol, prices_service, logger_service)
    data_retriever.start()
