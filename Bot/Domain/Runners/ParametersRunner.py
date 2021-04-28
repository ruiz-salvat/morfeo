import time
from threading import Thread
from Tests.Mock.MockMarketData import get_mock_market_data
from Util.Constants import parameters_refresh_event, parameters_runner_sleep_time, model_refresh_event, \
    parameters_process_name
from Util.Observable.Observer import Observer
from Util.Observable.Target import Target
from Util.Summarizer import summarize


class ParametersRunner(Thread, Target, Observer):

    def __init__(self, instance_id, indicator_ingestion, logger_service):
        Thread.__init__(self)
        Target.__init__(self, [indicator_ingestion])
        self.model = None
        self.instance_id = instance_id
        self.logger_service = logger_service
        self.kill_flag = False

    def run(self):
        while self.kill_flag is False:
            # TODO: get most recent data from database
            values = get_mock_market_data()
            summary = summarize(values)

            parameters = self.model.predict(summary.mean, summary.std, summary.skewness, summary.kurtosis,
                                            summary.entropy)
            self.event(parameters_refresh_event, parameters)
            self.logger_service.log_bot_instance(self.instance_id, parameters_process_name,
                                                 'Parameters update completed' + str(parameters))
            time.sleep(parameters_runner_sleep_time)

    def notify(self, *args, **kwargs):
        if args[0] == model_refresh_event:
            self.model = args[1]
