class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1
        if not self.stack:
            self.stack.append((price, count))
            return count
        else:
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] <= price:
                    count += self.stack[i][1]
                    self.stack.pop()
                else:
                    break
            
            self.stack.append((price, count))
            return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)