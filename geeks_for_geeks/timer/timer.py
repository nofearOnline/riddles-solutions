import time

def timer(func):
    def timeit(*args, **kwargs):
        tic = time.perf_counter()
        result = func(*args, **kwargs)
        toc = time.perf_counter()
        print(f"This function took {toc - tic:0.4f} seconds")
        return result
    return timeit