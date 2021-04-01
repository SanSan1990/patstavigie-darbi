class MyRange:

    def __init__(self, stop, start=0, step=1):
        self.current = start
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        return self

