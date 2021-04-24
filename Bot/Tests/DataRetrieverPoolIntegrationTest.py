from Database.Services.Service import Service
from Net.DataRetrieverPool import DataRetrieverPool


def DataRetrieverPoolIntegrationTest():
    service = Service(is_test=True)
    service.db_connector.drop_database()
    data_retriever_pool = DataRetrieverPool(is_test=True)
    data_retriever_pool.start_retrievers()
