import random

class Generator:
    def __init__(self):
        pass

    @staticmethod
    def generate_list(length, min_limit = 0, max_limit = 100):
        return [ int(random.randrange(min_limit, max_limit)) for i in range(length)]
