import numpy as np

# URLs
binance_api_url = 'https://api.binance.com'
db_url = 'mongodb://localhost:27017/'

# Database Names
database_name = 'morfeo_db'
test_database_name = 'test_db'

# Database Table Names
symbols_table_name = 'Symbols'
prices_table_name = 'Prices'
instances_table_name = 'Instances'
instance_states_table_name = 'InstanceStates'
trades_table_name = 'Trades'
customers_table_name = 'Customers'
patterns_table_name = 'Patterns'

# Primary Keys
symbols_pk = 'symbol'
instances_pk = 'instance_id'
customers_pk = 'customer_id'
patterns_pk = 'pattern_id'

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
simulation_refresh_event = 'simulation_refresh_event'

# Operation Names
buy_operation_name = 'BUY'
sell_operation_name = 'SELL'

# Time Intervals
simulation_runner_sleep_time = 300  # seconds
parameters_runner_sleep_time = 60  # seconds

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
get_instances_error_msg = 'Error getting the instances: no instances, or more than one instance was found'
insert_instance_db_msg = 'Instance inserted to database successfully'
insert_instance_db_error_msg = 'Error inserting instance to database'
update_instance_db_msg = 'Instance updated to database correctly'
update_instance_db_error_msg = 'Error updating instance to database'
delete_instance_db_msg = 'Instance deleted from database correctly'
delete_instance_db_error_msg = 'Error deleting instance from database'
get_trades_error_msg = 'Error getting trades list: no instances were found'
insert_trades_db_msg = 'Trades record inserted to database successfully'
insert_trades_db_error_msg = 'Error inserting trades record to database'
updates_trades_db_msg = 'Trades record updated to database successfully'
updates_trades_db_error_db = 'Error updating trades record to database'
delete_trades_db_msg = 'Trades record deleted from database correctly'
delete_trades_db_error_msg = 'Error deleting trades record from database'
get_instance_states_error_msg = 'Error getting instance states: no instances, or more than one instance was found'
insert_instance_states_db_msg = 'Instance states record inserted to database successfully'
insert_instance_states_db_error_msg = 'Error inserting instance states record to database'
update_instance_states_db_msg = 'Instance states record updated to database successfully'
update_instance_states_db_error_msg = 'Error updating instance states record to database'
delete_instance_states_db_msg = 'Instance states record deleted successfully from database'
delete_instance_states_db_error_msg = 'Error deleting instance states record from database'
insert_symbols_db_msg = 'Symbols inserted to database successfully'
insert_prices_db_msg = 'Prices inserted to database successfully'
insert_prices_db_error_msg = 'Error inserting prices to database'

# Exceptions
pattern_not_found = 'Pattern name not found'

# Other
seed_id = "seed_id"
