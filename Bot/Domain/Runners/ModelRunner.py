from ML.Model import Model
from Util.Constants import wave_trend_pattern_id, wave_trend_simulation_results, model_refresh_event, \
    pattern_not_found, simulation_refresh_event
from Util.Observable.Observer import Observer
from Util.Observable.Target import Target


class ModelRunner(Target, Observer):

    def __init__(self, parameters_runner):
        Target.__init__(self, [parameters_runner])

    def notify(self, *args, **kwargs):
        if args[0] == simulation_refresh_event:
            if args[1] == wave_trend_pattern_id:
                model = Model(wave_trend_simulation_results, wave_trend_pattern_id)
                self.event(model_refresh_event, model)
                print(str(model.best_model) + ' model generated with R2 = ' + str(model.max_r2))
            else:
                raise Exception(pattern_not_found)
