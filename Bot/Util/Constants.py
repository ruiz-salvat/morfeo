import numpy as np

# URLs
binance_api_url = 'https://api.binance.com'
db_url = 'mongodb://localhost:27017/'

# Database Names
database_name = 'morfeo_db'
symbols_table_name = 'Symbols'
prices_table_name = 'Prices'
instances_table_name = 'Instances'
instance_states_table_name = 'InstanceStates'
trades_table_name = 'Trades'
customers_table_name = 'Customers'
patterns_table_name = 'Patterns'

# File Paths
wave_trend_simulation_results = '../Data/ResultData/ADAUSDT_7_5_wave_trend_results.csv'

# Pattern IDs
wave_trend_pattern_id = 1

# Parameters
wave_trend_parameters = ['ob_level', 'os_level', 'k']  # !!! the parameters order must match with the ranges order !!!!
wave_trend_parameter_ranges = [range(43, 63, 5), range(-63, -43, 5), np.arange(0.001, 0.030, 0.001)]
model_global_parameters = ['std', 'skewness', 'kurtosis', 'entropy']

# Event Names
model_refresh_event = 'model_refresh_event'
parameters_refresh_event = 'parameters_refresh_event'

# Time Intervals
model_updater_sleep_time = 300  # seconds
parameters_updater_sleep_time = 60  # seconds

# Return Messages
bot_instance_added_msg = 'Bot instance added successfully'
bot_instance_exists_msg = 'Error: bot instance already exists'
bot_instance_started_msg = 'Bot instance started successfully'
bot_instance_already_started_msg = 'Error: bot instance was already started'
bot_instance_removed_msg = 'Bot instance removed successfully'
bot_instance_stopped_msg = 'Bot instance stopped successfully'
bot_instance_not_stopped_msg = 'Error: stop instance before removing it'
bot_instance_already_stopped_msg = 'Error: the bot instance was already stopped'
instance_id_not_found_msg = 'Error: instance id not found'

# Exceptions
pattern_not_found = 'Pattern name not found'
