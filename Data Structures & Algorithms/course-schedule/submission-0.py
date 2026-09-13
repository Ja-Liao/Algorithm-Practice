class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        visit = set()

        for crs, preq in prerequisites:
            preMap[crs].append(preq)

        def dfs(crs):
            if preMap[crs] is None:
                return True

            if crs in visit:
                return False
            
            visit.add(crs)
            for preq in preMap[crs]:
                if not dfs(preq):
                    return False
            visit.remove(crs)
            preMap[crs] = []
            
            return True

        for crs, preq in prerequisites:
            if not dfs(crs):
                return False

        return True