import time
from concurrent.futures import Future, ThreadPoolExecutor
from threading import Thread


def patch_future(cls):
    def __iter__(self):
        if not self.done():
            yield self
            return self.result()
        cls.__iter__ = __iter__


patch_future(Future)


class Task(Future):
    def __init__(self, gen):
        super().__init__()
        self._gen = gen

    def step(self, value=None, exc=None):
        # run to the next yield
        try:
            if exc:
                fut = self._gen.throw(exc)
            else:
                fut = self._gen.send(value)
            # future comes back, when you finish, go to wakeup and give result
            fut.add_done_callback(self._wakeup)
        except StopIteration as exc:
            self.set_result(exc.value)

    def _wakeup(self, fut):
        # handling of results
        try:
            result = fut.result()
            self.step(result, None)
        except Exception as exc:
            self.step(None, exc)  # feedback loop (run to next yield)

class TaskUtils:
    @staticmethod
    def start_inline_future(fut):
        task = Task(fut)
        task.step()
        return task

    @staticmethod
    def run_inline_future(fut):
        task = TaskUtils.start_inline_future(fut)
        return task.result()





if __name__ =='__main__':
    def func(x, y):
        """Some function. Nothing too interesting"""
        import time
        time.sleep(5)
        return x + y

    def dofunc(x, y):
        result = yield pool.submit(func, x, y)
        print("got:", result)


    pool = ThreadPoolExecutor(max_workers=8)
    t = Task(dofunc(2,3))
    t.step()

    def after(delay, gen):
        yield from pool.submit(time.sleep, delay)  # only if the Future is iterable - patch_future
        yield from gen