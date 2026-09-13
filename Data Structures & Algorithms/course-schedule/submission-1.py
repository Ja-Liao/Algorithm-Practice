class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        for x, y in prerequisites:
            courses[x].append(y)
        
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if courses[crs] == []:
                return True

            visiting.add(crs)
            for prereq in courses[crs]:
                if not dfs(prereq):
                    return False
            visiting.remove(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True