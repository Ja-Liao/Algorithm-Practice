class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        res = []
        connection = defaultdict(list)

        def dfs(x, y, visited):
            if x == y:
                return True

            visited.add(x)

            for destination in connection[x]:
                if destination not in visited and dfs(destination, y, visited):
                    return True
            return False

        for x, y in edges:
            visited = set()
            if x in connection and y in connection and dfs(x, y, visited):
                return [x,y]
            connection[x].append(y)
            connection[y].append(x)

        return 