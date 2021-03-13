# URLs
binance_api_url = 'https://api.binance.com'
db_url = 'mongodb://localhost:27017/'

# File Paths
wave_trend_simulation_results = '../Data/ResultData/ADAUSDT_7_5_wave_trend_results.csv'

# Model Names
wave_trend_model_name = 'wave_trend_model'

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
