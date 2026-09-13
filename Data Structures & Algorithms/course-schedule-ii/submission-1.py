class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        
        courses = defaultdict(list)
        for x, y in prerequisites:
            courses[x].append(y)

        visit = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in courses[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []

        return res