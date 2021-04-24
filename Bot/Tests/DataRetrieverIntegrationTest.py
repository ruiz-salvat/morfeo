from Database.Services.PricesService import PricesService
from Database.Services.SymbolsService import SymbolsService
from Net.DataRetriever import DataRetriever


def DataRetrieverIntegrationTest():
    prices_service = PricesService(is_test=True)
    symbols_service = SymbolsService(is_test=True)
    prices_service.db_connector.drop_database()
    symbol = 'ADA/USDT'
    symbols_service.insert_element(symbol.replace('/', ''), 'ADA', 'USDT')
    data_retriever = DataRetriever(symbol, prices_service)
    data_retriever.start()
