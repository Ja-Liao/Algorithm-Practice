class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [[value, timestamp]]
        else:
            self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""

        res = ''
        n = len(self.map[key])
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if self.map[key][m][1] <= timestamp:
                l = m + 1
                res = self.map[key][m][0]
            else:
                r = m - 1

        return res

