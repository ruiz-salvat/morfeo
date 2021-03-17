from ML.Model import generate_iterable
from Util.Constants import wave_trend_pattern_id


def Model_GenerateIterable_Equal():
    parameters = generate_iterable(wave_trend_pattern_id)
    for i in parameters:
        print(i)
