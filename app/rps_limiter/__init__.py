from collections import defaultdict, deque
from time import time
from asyncio import Lock

class RPS_limiter:
    def __init__(self, max_rps: int):
        if max_rps == 0:
            self.is_limit = self.is_non_limit
        self.max_rps = max_rps
        self.lock = Lock()
        self.req_times_by_url = defaultdict(deque)


    async def is_limit(self, rel_url: str) -> bool:
        req_time = time()
        async with self.lock:
            if len(self.req_times_by_url[rel_url]) < self.max_rps:
                self.req_times_by_url[rel_url].appendleft(req_time)
                return False
            if req_time - self.req_times_by_url[rel_url][0] < 1:
                return True
            self.req_times_by_url[rel_url].pop()
            self.req_times_by_url[rel_url].appendleft(req_time)
            return False

    async def is_non_limit(self, _: str) -> bool:
        return False