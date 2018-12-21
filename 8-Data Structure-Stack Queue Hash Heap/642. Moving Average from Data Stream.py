# 642. Moving Average from Data Stream
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Example
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1 // return 1.00000
# m.next(10) = (1 + 10) / 2 // return 5.50000
# m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
# m.next(5) = (10 + 3 + 5) / 3 // return 6.00000

class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        from queue import queue
        self.queue = Queue()
        self.size = size
        self.sum = 0.0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        self.sum += val
        if self.queue.qsize() == self.size:
            self.sum -= self.queue.get()
        self.queue.put(val)
        return self.sum * 1.0 / self.queueself.qsize()
