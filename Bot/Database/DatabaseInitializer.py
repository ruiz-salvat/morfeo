from Database import DatabaseConnector


def initialize_database():
    db = DatabaseConnector.connect()

    # Generate mock objects
    symbols = []
    prices = []
    instances = []
    instance_states = []
    trades = []
    customers = []
    models = []
