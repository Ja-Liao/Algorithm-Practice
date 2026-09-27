class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        curr_cap = 0
        arr = [0]*(max(t[2] for t in trips)+1)
        for t in trips:
            arr[t[1]] += t[0]
            arr[t[2]] -= t[0]

        
        for item in arr:
            curr_cap += item
            if curr_cap > capacity:
                return False
        
        return True
