from ML.Model import generate_iterable
from Util.Constants import wave_trend_pattern_id


def Model_GenerateIterable_Equal():
    parameters_list = []
    parameters = generate_iterable(wave_trend_pattern_id)
    for i in parameters:
        parameters_list.append(i)
    assert len(parameters_list) == 464, 'there should be 465 different combinations of parameters'
