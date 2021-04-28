from Database.Services.Service import Service
from Logger.LoggerService import LoggerService
from Net.DataRetrieverPool import DataRetrieverPool


def DataRetrieverPoolIntegrationTest():
    is_test = True
    service = Service(is_test=is_test)
    service.db_connector.drop_database()
    data_retriever_pool = DataRetrieverPool(is_test=is_test, logger_service=LoggerService(is_test=is_test))
    data_retriever_pool.start_retrievers()
