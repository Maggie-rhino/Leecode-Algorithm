class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        #  we can use DFS(deep first search)

        # step 1 : init two arrays
        m,n =len(heights),len(heights[0])
        # canReachP,canReachA =[[False]*n]*m,[[False]*n]*m
        canReachP = [[False] * n for _ in range(m)]
        canReachA = [[False] * n for _ in range(m)]
        
        # define dfs first, 
        def dfs(row,col, visited):
            visited[row][col] =True
            directions =[[0,1],[0,-1],[1,0],[-1,0]]
            
            for d in directions:
                x = d[0] + row
                y =d[1] +col
                if 0 <= x <m and 0 <= y< n:
                    print(x,y)
                    if not visited[x][y] and heights[x][y] >= heights[row][col]:
                        print('start recursive')
                        # dfs(x,y,visited)

        #  start from col
        for col in range(n):
            dfs(0,col,canReachP)
            dfs(m-1,col,canReachA)

        for row in range(m):
            dfs(row,0,canReachP)
            dfs(row,n-1,canReachA)
        
        res =[]

        for row in range(m):
            for col in range(n):
                if canReachP[row][col] ==True and canReachA[row][col]==True:
                    res.append([row,col])
        
        return res