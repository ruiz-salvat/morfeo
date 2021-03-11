import time
from threading import Thread
from ML.WaveTrendModel import WaveTrendModel
from Util.Constants import wave_trend_model_name, wave_trend_simulation_results, model_refresh_event, \
    model_updater_sleep_time
from Util.Observable.Target import Target


class ModelUpdater(Thread, Target):

    def __init__(self, model_name, parameters_updater):
        Thread.__init__(self)
        Target.__init__(self, [parameters_updater])  # set observer
        self.model_name = model_name
        if self.model_name == wave_trend_model_name:
            self.model = WaveTrendModel(wave_trend_simulation_results)
            print(str(self.model.best_model) + ' model initialization completed with R2 = ' + str(self.model.max_r2))
        else:
            raise Exception('Model not found')
        self.kill_flag = False

    def run(self):
        if self.model_name == wave_trend_model_name:
            while self.kill_flag is False:
                self.model = WaveTrendModel(wave_trend_simulation_results)
                self.event(model_refresh_event, self.model)
                print(str(self.model.best_model) + ' model update completed with R2 = ' + str(self.model.max_r2))
                time.sleep(model_updater_sleep_time)
        else:
            raise Exception('Model not found')
