import time


class ThreadPool:

    def __init__(self, pool_limit):
        self.thread_pool_array = []
        self.pool_limit = pool_limit

    def pool_size(self):
        count = 0
        for thread in self.thread_pool_array:
            if thread.is_alive():
                count += 1
        return count

    def add_thread(self, thread):
        while self.pool_size() > self.pool_limit:
            time.sleep(1)
        thread.start()
        self.thread_pool_array.append(thread)
