import pandas as pd
from datetime import datetime, timedelta

results = pd.read_csv('../../Data/ResultData/ADAUSDT_7_5_wave_trend_results.csv')

results = results[results['clean_gains'] != 0]
final_df = pd.DataFrame(columns=['mean', 'std', 'skewness',	'kurtosis',	'entropy', 'ob_level', 'os_level', 'k',
                                 'clean_gains'])

start_date = results.iloc[0]['start_date']
start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
end_date = start_date + timedelta(days=7)
df = results[(results['start_date'] >= str(start_date)) & (results['end_date'] < str(end_date))]

while df.shape[0] > 0:

    df = df.sample(frac=1)
    df = df.reset_index(drop=True)

    max_gains = 0
    max_gains_row = None
    for index, row in df.iterrows():
        if row['clean_gains'] > max_gains:
            max_gains = row['clean_gains']
            max_gains_row = row

    aux_df = pd.DataFrame([[max_gains_row['mean'], max_gains_row['std'], max_gains_row['skewness'],
                            max_gains_row['kurtosis'], max_gains_row['entropy'], max_gains_row['ob_level'],
                            max_gains_row['os_level'], max_gains_row['k'], max_gains_row['clean_gains']]],
                          columns=final_df.columns)
    final_df = final_df.append(aux_df, ignore_index=True)

    start_date = end_date
    end_date = start_date + timedelta(days=7)
    df = results[(results['start_date'] >= str(start_date)) & (results['end_date'] < str(end_date))]

final_df.to_csv('../../Data/OptimizationData/ADAUSDT_7_5_wave_trend_optimizations_0steps.csv', index=False)
