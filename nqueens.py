def nQueens(n):
    col = set() #set of all columns that are occupied
    posDiag = set() #set of all positive diagonal elements
    negDiag = set() #set of all negative diagonal elements
 
    result = 0 #number of valid solutions
    def isValid(row):
        if row==n:
            nonlocal result
            result +=1
            return
        
        for c in range(8):
            if c in col or (row+c) in posDiag or (row-c) in negDiag:
                continue #if the Queens clash
            col.add(c) #if not, the currently occupied columns are updated
            posDiag.add(row+c) #currently invalid diagonal positions
            negDiag.add(row-c) #currently invalid diagonal positions
            isValid(r+1) #check for next row
            col.remove(c) #If the next row’s valid positions have been found, then the 3 sets can be erased as all pieces already placed are legal.
            posDiag.remove(row+c)
            negDiag.remove(row-c)
 
    isValid(0)
    return res
