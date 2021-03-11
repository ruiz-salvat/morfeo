import pandas as pd


def get_mock_market_data():
    df = pd.read_csv('../Data/test_data.csv')
    df = df[df['timestamp'] < '2020-09-19 00:01:00']
    values = df['value'].to_numpy()
    return values
