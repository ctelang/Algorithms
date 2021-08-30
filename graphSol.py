class Graph():

    def __init__(self, adjacency_matrix):
        """ 
        Graph initialized with a weighted adjacency matrix 
        
        Attributes
        ----------
        adjacency_matrix : 2D array
            non-negative integers where adjacency_matrix[i][j] is the weight of the edge i to j,
            with 0 representing no edge

        """

        self.adjacency_matrix = adjacency_matrix

        # Add more class variables below as needed, such as n:
        self.N = len(adjacency_matrix)

    
    def Prim(self):
        """
        Use Prim-Jarnik's algorithm to find the length of the minimum spanning tree starting from node 0

        Returns
        -------
        int
            Weighted length of tree

        """
        mstWeight = 0

        vertices = [0] * self.N
        cost = [float("inf")] * self.N
        inMST = [False] * self.N

        inMST[0] = True
        newNeighbor = 0

        for i in range(self.N - 1):

            minCost = float("inf")

            for j in range(self.N):
                if not inMST[j]:
                    weight = self.adjacency_matrix[newNeighbor][j]
                    if weight != 0 and weight < cost[j]:
                        vertices[j] = newNeighbor
                        cost[j] = weight

            for j in range(self.N):
                if not inMST[j]:
                    if cost[j] < minCost:
                        newNeighbor = j
                        minCost = cost[j]

            if newNeighbor != 0:
                #print(cost[newNeighbor])
                mstWeight += cost[newNeighbor]
                inMST[newNeighbor] = True
        #print(mstWeight)
        return mstWeight


#  Example use case:

#G = Graph([[0, 10, 11, 33, 60],
            #[10, 0, 22, 14, 57],
            #[11, 22, 0, 11, 17],
            #[33, 14, 11, 0, 9],
            #[60, 57, 17, 9, 0]])
#G2 = Graph([[0, 4, 3, 0],
           [4, 0, 10, 0],
           [3, 10, 0, 7],
           [0, 0, 7, 0]])

#assert G2.Prim() == 14

