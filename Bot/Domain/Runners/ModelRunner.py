import time
from threading import Thread
from ML.Model import Model
from Util.Constants import wave_trend_pattern_name, wave_trend_simulation_results, model_refresh_event, \
    model_updater_sleep_time
from Util.Observable.Target import Target


class ModelRunner(Thread, Target):

    def __init__(self, model_name, parameters_updater):
        Thread.__init__(self)
        Target.__init__(self, [parameters_updater])  # set observer
        self.pattern_name = model_name
        if self.pattern_name == wave_trend_pattern_name:
            self.model = Model(wave_trend_simulation_results, wave_trend_pattern_name)
            print(str(self.model.best_model) + ' model initialization completed with R2 = ' + str(self.model.max_r2))
        else:
            raise Exception('Pattern name not found')
        self.kill_flag = False

    def run(self):
        if self.pattern_name == wave_trend_pattern_name:
            while self.kill_flag is False:
                self.model = Model(wave_trend_simulation_results, wave_trend_pattern_name)
                self.event(model_refresh_event, self.model)
                print(str(self.model.best_model) + ' model update completed with R2 = ' + str(self.model.max_r2))
                time.sleep(model_updater_sleep_time)
        else:
            raise Exception('Pattern name not found')
