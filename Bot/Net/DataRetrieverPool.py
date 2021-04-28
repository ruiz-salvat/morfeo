from Database.Services.PricesService import PricesService
from Net.DataRetriever import DataRetriever
from Util.SymbolList import symbol_list, insert_symbols_to_db


class DataRetrieverPool:

    def __init__(self, is_test, logger_service):
        insert_symbols_to_db(is_test, logger_service)
        self.data_retriever_list = []
        for symbol in symbol_list:
            self.data_retriever_list.append(DataRetriever(symbol, PricesService(is_test=is_test), logger_service))

    def start_retrievers(self):
        for data_retriever in self.data_retriever_list:
            if data_retriever.is_alive() is False and data_retriever.kill_flag is False:
                data_retriever.start()

    def stop_retrievers(self):
        for data_retriever in self.data_retriever_list:
            if data_retriever.is_alive() is True and data_retriever.kill_flag is False:
                data_retriever.kill_flag = True

    def resume_retrievers(self):
        for data_retriever in self.data_retriever_list:
            if data_retriever.is_alive() is True and data_retriever.kill_flag is True:
                data_retriever.kill_flag = False
