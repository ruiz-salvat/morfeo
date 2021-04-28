from ML.Model import Model
from Util.Constants import wave_trend_pattern_id, wave_trend_simulation_results, model_refresh_event, \
    pattern_not_found, simulation_refresh_event, model_process_name
from Util.Observable.Observer import Observer
from Util.Observable.Target import Target


class ModelRunner(Target, Observer):

    def __init__(self, instance_id, parameters_runner, logger_service):
        Target.__init__(self, [parameters_runner])
        self.instance_id = instance_id
        self.logger_service = logger_service

    def notify(self, *args, **kwargs):
        if args[0] == simulation_refresh_event:
            if args[1] == wave_trend_pattern_id:
                model = Model(wave_trend_simulation_results, wave_trend_pattern_id)
                self.event(model_refresh_event, model)
                self.logger_service.log_bot_instance(self.instance_id, model_process_name,
                                                     'Model generated: ' + str(model.best_model) + ' with R2 = ' + str(model.max_r2))
            else:
                raise Exception(pattern_not_found)
