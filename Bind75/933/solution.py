class RecentCounter:

    def __init__(self):
        self.requests =[]

    # we do not want to store all the requests, 
    # we only need to store the requests in the last 3000ms
    # [1, 100, 3001]
    def ping(self, t: int) -> int:
        self.requests.append(t)
        while (len(self.requests)>0) and (self.requests[0]< t-3000):
            self.requests.pop(0);
        return len(self.requests)
        
