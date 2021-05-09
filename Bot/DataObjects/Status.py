from enum import Enum


class Status(Enum):
    NOT_STARTED = 'Not started'
    INITIALIZING = 'Initializing'
    RUNNING = 'Running'
    FAILED = 'Failed'
    STOPPED = 'Stopped'
