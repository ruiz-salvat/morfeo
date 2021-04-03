import pandas as pd
from Patterns.BoltPattern import BoltPattern

test_pattern = BoltPattern(3, 2, 2, 2)  # 11, 10
test_symbol = 'test_symbol'
test_time_scale = 1
test_budget = 100
test_partition_size = 10
test_n_partition_limit = 1
test_waves_array = [14, 13, 14, 15, 17, 16, 13, 12, 11, 12, 11, 12, 11, 12, 13, 14, 15, 13, 15, 12, 11, 9, 10, 8, 12,
                    11, 12, 11, 12, 13, 14]
test_ob_level = 53
test_os_level = -53
test_k = 0.015
test_df = pd.DataFrame([[1, 2], [2, 3], [3, 4], [4, 1]], columns=['timestamp', 'value'])
