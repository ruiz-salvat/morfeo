import pandas as pd
from Simulators.BoltSimulator import BoltSimulator
from Util.Constants import symbols
from datetime import datetime, time


def run_script(data):
    count = 0
    symbol_count = 0
    bolt_simulator = BoltSimulator(6)  # Maximum exponent is 6

    for symbol in symbols:
        symbol_count += 1
        data_symbol = data[data['symbol'] == symbol]
        day_df = pd.DataFrame(columns=data_symbol.columns)
        p = False

        for index, row in data_symbol.iterrows():
            date = datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S')

            if p is True and date.hour == time(hour=0).hour:
                bolt_simulator.simulate(day_df, symbol, 30, 1000, 10, 50)

                count += day_df.shape[0]
                print(str((count / data_symbol.shape[0]) * 100) + ' of ' + str((symbol_count / len(symbols)) * 100))

                day_df = pd.DataFrame(columns=data_symbol.columns)
                p = False

            elif p is False and date.hour != time(hour=0).hour:
                p = True

            aux_df = pd.DataFrame([row], columns=day_df.columns)
            day_df = day_df.append(aux_df, ignore_index=True)
