class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # cap = max(weights)
        # while True: 
        #     curr_cap = cap
        #     ship = 1
        #     for w in weights:
        #         if w > curr_cap:
        #             ship += 1
        #             curr_cap = cap
        #         curr_cap -= w
                
        #     if ship <= days:
        #         return cap

        #     cap += 1
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high) // 2
            curr_cap = mid
            ships = 1
            flag = False
            for w in weights:
                if w > curr_cap:
                    ships += 1
                    if ships > days:
                        flag = True
                        break
                    curr_cap = mid
                
                curr_cap -= w
            if flag:
                low = mid + 1
            else:
                high = mid - 1

        return low



