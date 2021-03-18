from Tests.Mock.MockIndicator import MockIngestor
from Tests.Mock.MockPattern import MockPattern

valid_id = 1
invalid_id = -1
test_time = 999.9
updated_test_time = 1111
test_symbol = 'test_symbol'
test_time_scale = 5
test_budget = 1000
test_partition_size = 10
test_n_partition_limit = 50
test_model_name = 'test_model_name'
test_pattern = MockPattern()
test_indicator = MockIngestor(test_pattern, test_time_scale, test_budget, test_partition_size, test_n_partition_limit)
