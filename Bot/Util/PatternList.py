from Database.Services.PatternsService import PatternsService
from Util.Constants import patterns_service_name

pattern_list = [
    {'pattern_id': 'wave_trend',
     'pattern_name': 'Wave Trend'},
]


def insert_patterns_to_db(is_test, logger_service):
    patterns_service = PatternsService(is_test, logger_service)
    for pattern in pattern_list:
        msg = patterns_service.insert_element(pattern['pattern_id'], pattern['pattern_name'])
        logger_service.log_service(patterns_service_name, msg + ' - (' + pattern['pattern_name'] + ')')
