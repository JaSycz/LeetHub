class RecentCounter:

    def __init__(self):
        self.counter = []

    def ping(self, t: int) -> int:
        self.counter.append(t) 
        while(self.counter[len(self.counter)-1] - self.counter[0] > 3000):
            self.counter.pop(0)
        return len(self.counter)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)