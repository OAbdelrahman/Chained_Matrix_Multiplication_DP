def printMatrix(m): 
    for row in m:
        print(row)

def chainMatrix(dims):
    # Create the empty 2-D table
    n = len(dims)-1
    m = [[None for i in range(n)] for j in range(n)]

    # Creating a traceback table
    traceTable = [[None for i in range(n)] for j in range(n)] 

    # Fill in the base case values
    for i in range(n): 
        m[i][i] = 0
    # Fill in the rest of the table diagonal by diagonal
    for chainLength in range(2,n+1): 
        for i in range(n+1-chainLength):
            j = i + chainLength - 1

            # Fill in m[i][j] with the best of the recursive options
            m[i][j] = float("inf") 
            
            for k in range(i,j):
            # Two previous table values plus
            # what it cost to mult the resulting matrices
                q = m[i][k]+m[k+1][j]+dims[i]*dims[k+1]*dims[j+1] 
                if q < m[i][j]:
                    m[i][j] = q

                    # Adding values to the traceback table  
                    traceTable[i][j] = k
    printMatrix(m)
    printMatrix(traceTable)

    print(parentStr(traceTable, 0, len(dims)-2))

    return m[0][n-1]

def parentStr(traceTable, start, end):
    if start == end:
        return f"A{start}"
    
    else:    
        mid = traceTable[start][end]
        left = parentStr(traceTable, start, mid)
        right = parentStr(traceTable, mid+1, end)
    
    return f"( {left} ) ( {right} )"

if __name__ == "__main__":
    dims = [10,5,20,10,5]
    print(chainMatrix(dims))