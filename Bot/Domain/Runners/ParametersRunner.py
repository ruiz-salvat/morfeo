import time
from threading import Thread
from Tests.Mock.MockMarketData import get_mock_market_data
from Util.Constants import parameters_refresh_event, parameters_updater_sleep_time, model_refresh_event
from Util.Observable.Observer import Observer
from Util.Observable.Target import Target
from Util.Summarizer import summarize


class ParametersRunner(Thread, Target, Observer):

    def __init__(self, model, indicator_ingestion):
        Thread.__init__(self)
        Target.__init__(self, [indicator_ingestion])
        self.model = model
        self.kill_flag = False

    def run(self):
        while self.kill_flag is False:
            # TODO: get most recent data from database
            values = get_mock_market_data()
            summary = summarize(values)

            parameters = self.model.predict(summary.std, summary.skewness, summary.kurtosis, summary.entropy)
            self.event(parameters_refresh_event, parameters)
            print(str(parameters) + ' parameters update completed')
            time.sleep(parameters_updater_sleep_time)

    def notify(self, *args, **kwargs):
        if args[0] == model_refresh_event:
            self.model = args[1]
