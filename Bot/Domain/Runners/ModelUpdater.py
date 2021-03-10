from threading import Thread
from ML.WaveTrendModel import WaveTrendModel
from Util.Constants import wave_trend_model_name, wave_trend_simulation_results


class ModelUpdater(Thread):

    def __init__(self, model_name):
        Thread.__init__(self)
        self.model_name = model_name
        if self.model_name == wave_trend_model_name:
            self.model = WaveTrendModel(wave_trend_simulation_results)
        else:
            raise Exception('Model not found')
        self.kill_flag = False

    def run(self):
        if self.model_name == wave_trend_model_name:
            while self.kill_flag is False:
                self.model = WaveTrendModel(wave_trend_simulation_results)
        else:
            raise Exception('Model not found')
