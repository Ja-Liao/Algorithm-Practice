class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for (x, y), cnt in self.ptsCount.items():
            if (abs(py - y) != abs(px - x)) or x == px:
                continue
            c1 = self.ptsCount.get((x, py), 0)
            c2 = self.ptsCount.get((px, y), 0)
            res += c1 * c2 * cnt
            
        return res
