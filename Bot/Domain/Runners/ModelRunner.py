import time
from threading import Thread
from ML.Model import Model
from Util.Constants import wave_trend_pattern_id, wave_trend_simulation_results, model_refresh_event, \
    model_updater_sleep_time, pattern_not_found
from Util.Observable.Target import Target


class ModelRunner(Thread, Target):

    def __init__(self, model_name, parameters_updater):
        Thread.__init__(self)
        Target.__init__(self, [parameters_updater])  # set observer
        self.pattern_name = model_name
        if self.pattern_name == wave_trend_pattern_id:
            self.model = Model(wave_trend_simulation_results, wave_trend_pattern_id)
            print(str(self.model.best_model) + ' model initialization completed with R2 = ' + str(self.model.max_r2))
        else:
            raise Exception(pattern_not_found)
        self.kill_flag = False

    def run(self):
        if self.pattern_name == wave_trend_pattern_id:
            while self.kill_flag is False:
                self.model = Model(wave_trend_simulation_results, wave_trend_pattern_id)
                self.event(model_refresh_event, self.model)
                print(str(self.model.best_model) + ' model update completed with R2 = ' + str(self.model.max_r2))
                time.sleep(model_updater_sleep_time)
        else:
            raise Exception(pattern_not_found)
