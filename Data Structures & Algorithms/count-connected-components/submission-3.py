class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int: 
        # adj = [[] for _ in range(n)]
        # for u,v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        # visit = set()
        # res = 0

        # def dfs(node):
        #     for nei in adj[node]:
        #         if nei not in visit:
        #             visit.add(nei)
        #             dfs(nei)
                    

        # for u, v in edges:
        #     if u not in visit:
        #         visit.add(u)
        #         dfs(u)
        #         res += 1

        # return res
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        return res