"""Helper module in searching package.

From https://realpython.com/python-timer/#a-python-timer-class
Changed a bit to return nanoseconds in int instead of seconds by
using perf_counter_ns()
"""
import time


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter_ns()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter_ns() - self._start_time
        return elapsed_time
