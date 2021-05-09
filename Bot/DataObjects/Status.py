from enum import Enum


class Status(Enum):
    NOT_INITIALIZED = 'Not initialized'
    INITIALIZING = 'Initializing'
    NOT_STARTED = 'Not started'
    RUNNING = 'Running'
    FAILED = 'Failed'
    STOPPED = 'Stopped'
